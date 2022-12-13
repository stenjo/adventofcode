// --- Day 12: Hill Climbing Algorithm ---

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

export class Pos {
    isAt(x: number, y: number) {
        return this.x == x && this.y == y;
    }
    steps!: number;
    Clone(): Pos {
        return new Pos(this.x, this.y, this.elev.toString());
    }
    x: number;
    y: number;
    elev!: string;
    visited: boolean;
    constructor(x: number, y: number, elev: string) {
        this.x = x;
        this.y = y;
        this.elev = elev;
        this.steps = 0;
        this.visited = false;
    }
}

export class ElevationMap {
    GetLowestSteps(elevation: string):Pos {
        let list:Pos[] = [];
        for (let y = 0; y < this.map.length; y++) {
            for (let x = 0; x < this.map[y].length; x++) {
                if (this.map[y][x].elev == elevation && this.map[y][x].steps != 0) {
                    list.push(this.map[y][x])
                }
            }
        }
        return list.sort((a, b) =>a.steps - b.steps).shift() as Pos;
    }
    VisitPoint(point: Pos) {
        let pList = this.GetValidNeighbours(point)
        pList.forEach((p) => {
            if (p.steps > point.steps + 1 || p.steps == 0) {
                (p as Pos).steps = point.steps + 1
                this.VisitPoint(p as Pos);
                (p as Pos).visited = true
            }
        });
    }
    GetValidNeighbours(p:Pos) {
        let list:Pos[] = []
        if (this.isValidNext(p.x, p.y+1, p)) list.push(this.getAt(p.x, p.y+1) as Pos);
        if (this.isValidNext(p.x, p.y-1, p)) list.push(this.getAt(p.x, p.y-1) as Pos);
        if (this.isValidNext(p.x+1, p.y, p)) list.push(this.getAt(p.x+1, p.y) as Pos);
        if (this.isValidNext(p.x-1, p.y, p)) list.push(this.getAt(p.x-1, p.y) as Pos);

        return list
    }
    GetVisitOptions(p: Pos) {
        let list = [];
        if (this.isValidP(p.x, p.y+1, p)) list.push({x: p.x, y: p.y+1});
        if (this.isValidP(p.x, p.y-1, p)) list.push({x: p.x, y: p.y-1});
        if (this.isValidP(p.x+1, p.y, p)) list.push({x: p.x+1, y: p.y});
        if (this.isValidP(p.x-1, p.y, p)) list.push({x: p.x-1, y: p.y});

        return list
    }
    PrintRopeVisits() {
        const minY = 0
        const maxY = this.map.length
        const minX = 0
        const maxX = this.map[0].length
        for (let y = minY; y < maxY; y++) {
            let line = ''
            for (let x = minX; x < maxX; x++) {
                if (x == 0 && y == 0) {
                    line += 's'
                } else {
                    line += this.getAt(x,y)?.visited ? this.getAt(x,y)?.elev : '.'
                }
            }
            console.log(line)
        }
    }
    private isValidP(x: number, y: number, p:Pos) {
        if (y >= this.map.length
            || y < 0
            || x >= this.map[y].length
            || x < 0) 
            return false;

        let n = this.getAt(x, y) as Pos;
        let nElev = n.elev.charCodeAt(0)
        let pElev = p.elev.charCodeAt(0)
        if (n.elev == 'E') nElev = 'z'.charCodeAt(0)

        return nElev < pElev + 2 && nElev > pElev -2 && (n.steps > p.steps-1 || n.steps == 0);
    }

    end!: Pos;
    start!: Pos;
    map: Pos[][];
    current!: Pos;

    constructor(m: string[]) {
        this.map = [];
        m.forEach((l, y) => {
            this.map.push(l.split('').map((v,x) => new Pos(x,y,v)))
        })
        for (let y = 0; y < this.map.length; y++) {
            for (let x = 0; x < this.map[y].length; x++) {
                if (this.map[y][x].elev == 'E') this.end = new Pos(x,y, 'z')
                if (this.map[y][x].elev == 'S') {
                    this.start = new Pos(x,y, 'a')
                    this.current = this.start.Clone()
                }
            }
        }
    }

    getAt(x: number|undefined, y: number|undefined) {
        if ( x === undefined || y === undefined) return
        return this.map[y][x];
    }

    private isValidNext(x: number, y: number, p:Pos) {
        if (y >= this.map.length
            || y < 0
            || x >= this.map[y].length
            || x < 0) 
            return false;

        let n = this.getAt(x, y) as Pos;
        let nElev = n.elev.charCodeAt(0)
        let pElev = p.elev.charCodeAt(0)
        if (n.elev == 'E') nElev = 'z'.charCodeAt(0)

        return nElev < pElev + 2 && nElev > pElev -2
    }
}

let l = new LoadLines('../input/day12.txt').lines
let e = new ElevationMap(l)

e.VisitPoint(e.start)
e.PrintRopeVisits()

