// --- Day 14: Regolith Reservoir ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n')
        .map(line => line.trim());
    }
}
class Rock {
    x: number;
    y: number;
    constructor(x: number, y: number) { 
        this.x = x;
        this.y = y;
    }
}
class Sand {
    x: number;
    y: number;
    resting: boolean = false;
    constructor(x: number, y: number) { 
        this.x = x;
        this.y = y;
    }
}
export class Cave {
    DropUntilTop() {
        while(!this.SandAt(500,0)) {
            this.DropSand(true)
        }
    }
    DropUntilOverflow() {
        let sands = -1
        while (this.SandResting() != sands) {
            sands = this.SandResting()
            this.DropSand()
        }
    }
    sand: Sand[] = [];
    SandResting(): number {
        if (this.sand.length == 0) { return 0}
        return this.sand.length
    }
    DropSand(floor:boolean = false) {
        let s = new Sand(500, 0)
        let maxY = this.mountain.map(r => r.y).sort((a, b) => a - b).pop() as number + 2

        while (s.resting == false && s.y < maxY) {
            if (floor && s.y >= maxY-1) {
                s.resting = true
            }
            else if (!this.RockAt(s.x, s.y + 1) && !this.SandAt(s.x, s.y + 1)) {
                s.y++
            }
            else if (!this.RockAt(s.x - 1, s.y + 1) && !this.SandAt(s.x - 1, s.y + 1)) {
                s.x--
                s.y++
            }
            else if (!this.RockAt(s.x + 1, s.y + 1) && !this.SandAt(s.x + 1, s.y + 1)) {
                s.x++
                s.y++
            }
            else {
                s.resting = true
            }
        }
        if (s.y < maxY || (s.y < maxY + 1) && floor) this.sand.push(s)
    }
    PrintCave():string[] {

        let minXRock = this.mountain.map(r => r.x).sort((a, b) => a - b).shift() as number
        let minXSand = this.sand.map(r => r.x).sort((a, b) => a - b).shift() as number
        let minX = Math.min(minXRock, minXSand)

        let maxXRock = this.mountain.map(r => r.x).sort((a, b) => a - b).pop() as number
        let maxXSand = this.sand.map(r => r.x).sort((a, b) => a - b).pop() as number
        let maxX = Math.max(maxXRock, maxXSand)

        let minY = 0
        let maxY = this.mountain.map(r => r.y).sort((a, b) => a - b).pop() as number + 2

        let line = ''
        let map:string[] = []
        for (let y = minY; y <= maxY; y++) {
            line = y + ' '
            if (y < 10) line = ' ' + line
            for (let x = minX; x <= maxX; x++) {
                if (y == 0 && x == 500) {
                    line += '+'
                    continue
                }
                if (this.SandAt(x, y)) {
                    line += 'o'
                } else if (this.RockAt(x,y)) {
                    line += '#'
                }
                else {
                    line += '.'
                }
            }
            map.push(line)
        }
        return map
    }
    SandAt(x: number, y: number): boolean {
        return this.sand.find(r => r.x == x && r.y == y) !== undefined
    }
    RockAt(x: number, y: number): boolean {
        return this.mountain.find(r => r.x == x && r.y == y) !== undefined
    }
    mountain: Rock[];

    constructor(input: string[] = ['']) {
        this.mountain = []
        input.forEach(line => {
            let pts:number[][] = line.split(' -> ').map(point => point.split(',').map(n=>Number(n)))

            for (let i = 0; i < pts.length - 1; i++) {
                let start = pts[i]
                let end = pts[i + 1]

                this.createRockRange(start, end)
                .forEach(r => {
                    if (!this.RockAt(r.x,r.y)) {
                        this.mountain.push(r)
                    }
                })
            }
        })
    }
     
    private createRockRange(start: number[], end: number[]): Rock[] {
        let startX = start[0];
        let startY = start[1];
        let endX = end[0];
        let endY = end[1];
        let rocks: Rock[] = [];

        let yLength = Math.abs(endY - startY);
        if (yLength > 0) {
            let incr = yLength / (endY - startY);
            let yCoords = [...Array(yLength + 1)].map((_, i) => startY + i * incr);
            yCoords.forEach(y => rocks.push(new Rock(startX, y)));
        }

        let xLength = Math.abs(endX - startX);
        if (xLength > 0) {
            let incr = xLength / (endX - startX);
            let xCoords = [...Array(xLength + 1)].map((_, i) => startX + i * incr);
            xCoords.forEach(x => rocks.push(new Rock(x, startY)));
        }

        return rocks
    }
}
