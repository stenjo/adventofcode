// --- Day 9: Rope Bridge ---

export class Pos {
    x: number;
    y: number;
    constructor(x:number, y:number) {
        this.x = x;
        this.y = y;
    }
}
export class RopeModel {
    MoveHeadR() {
        this.head.x += 1;
        if (Math.abs(this.head.x - this.tail.x) > 1) {
            this.tail.x += 1
            this.TailVisit(this.tail)
        }
    }
    TailVisit(tail: Pos) {
        const extist = this.tailLocations.find((l) => {
            return l.x === tail.x && l.y === tail.y;
        })

        if (!extist) {
            this.tailLocations.push(tail)
        }
    }
    head: Pos;
    tail: Pos;
    tailLocations: Pos[];

    constructor() {
        this.head = new Pos(0,0)
        this.tail = new Pos(0,0)
        this.tailLocations = []
        this.tailLocations.push(this.tail)
    }

}

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
        let file = path.join(__dirname,fname);
        this.lines = fs.readFileSync(file, 'utf8').trim().split('\n').map(line => line.trim())
    }
}

