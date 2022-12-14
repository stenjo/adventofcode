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
export class Cave {
    RockAt(arg0: number, arg1: number): boolean {
        return this.structures.find(r => r.x == arg0 && r.y == arg1) !== undefined
    }
    structures: Rock[];

    constructor(input: string[] = ['']) {
        this.structures = []
        input.forEach(line => {
            let pts:number[][] = line.split(' -> ').map(point => point.split(',').map(n=>Number(n)))

            for (let i = 0; i < pts.length - 1; i++) {
                let start = pts[i]
                let end = pts[i + 1]

                this.createRockRange(start, end).forEach(r => {if (!this.RockAt(r.x,r.y)) this.structures.push(r)} )
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
            let yes = [...Array(yLength + 1)].map((_, i) => startY + i * incr);
            yes.forEach(y => rocks.push(new Rock(startX, y)));
        }

        let xLength = Math.abs(endX - startX);
        if (xLength > 0) {
            let incr = xLength / (endX - startX);
            let xes = [...Array(xLength + 1)].map((_, i) => startX + i * incr);
            xes.forEach(x => rocks.push(new Rock(x, startY)));
        }

        return rocks
    }
}