// --- Day 22: Monkey Map ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trimEnd()
        .split('\n').map(line => line.trimEnd());
    }
}

export enum Facing {
    Right = 0,
    Down,
    Left,
    Up
}
export class MonkeyMap {
    Move(pos: number, rotate: string) {

        let walColumn = this.map[this.row-1].indexOf('#')+1
        this.column += Math.min(pos, walColumn-this.column-1)
        this.facing = Facing.Down
    }

    column: number;
    facing: Facing;
    row: number;
    map: string[];
    directions: string;
    constructor(instructions: string[]) {
        this.map = [];
        this.directions = instructions.pop() as string
    
        instructions.forEach(l => { if (l.length > 0) this.map.push(l)});

        this.row = 1
        this.column = this.map[0].indexOf('.') + 1
        this.facing = Facing.Right

    }

    Print() {
        console.log(this.map);
    }
}