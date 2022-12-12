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
    Move() {
        let x = this.current.x;
        let y = this.current.y;

        let options = this.GetMoveOptions(this.current).shift()
        this.updateCurrent(this.getAt(options?.x, options?.y));
    }
    GetMoveOptions(current: Pos) {
        let list = [];
        if (this.isValidNext(current.x, current.y+1)) list.push({x: current.x, y: current.y+1});
        if (this.isValidNext(current.x, current.y-1)) list.push({x: current.x, y: current.y-1});
        if (this.isValidNext(current.x+1, current.y)) list.push({x: current.x+1, y: current.y});
        if (this.isValidNext(current.x-1, current.y)) list.push({x: current.x-1, y: current.y});


        let result = list.sort( (a, b) => {
            let diff = (this.getAt(a.x, a.y) as Pos).steps - (this.getAt(b.x, b.y) as Pos).steps
            if ((this.getAt(a.x, a.y) as Pos).steps > 0 ) diff += 100

            return diff
        });

        let stepList = result.map((p) => (this.getAt(p.x, p.y) as Pos).steps);

        return result
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

    private getAt(y: number|undefined, x: number|undefined) {
        if ( x === undefined || y === undefined) return
        return this.map[y][x];
    }

    private updateCurrent(next: Pos|undefined) {
        if (next === undefined) return
        this.current.elev = next.elev;
        this.current.x = next.x;
        this.current.y = next.y;
        this.current.steps++;
        if (next.steps > this.current.steps || next.steps == 0) {
            next.steps = this.current.steps;
        }
        else {
            this.current.steps = next.steps;
        }
    }

    private isValidNext(y: number, x: number) {
        return y < this.map.length
        && y >= 0
        && x < this.map[y].length
        && x >= 0
        && this.map[y][x].elev.charCodeAt(0) < this.current.elev.charCodeAt(0) + 2 
        && this.map[y][x].elev.charCodeAt(0) > this.current.elev.charCodeAt(0) - 2;
    }
}