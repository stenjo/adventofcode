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
        if (this.facing == Facing.Down) {
            let wallRow = this.getDownWallRow();
            this.row += Math.min(pos, wallRow-pos-1)
        }
        if (this.facing == Facing.Right) {
            let walColumn = this.getRightWallColumn()
            if (walColumn > 0) {
                this.column = this.column + Math.min(pos, walColumn-this.column-1)
                this.updateDirection(rotate); 
                return
            }
            if (this.column + pos > this.map[this.row-1].length) {
                walColumn = this.map[this.row-1].indexOf('#')+1
                if (walColumn > 0) {
                    let remaining = this.getRightRowRemaining();
                    this.column = Math.min(pos - remaining + 1, walColumn-1)
                }
            }
        }
        this.updateDirection(rotate);  
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

    private getRightRowRemaining() {
        let remaining = this.map[this.row - 1].length - this.column + 1;
        remaining = remaining % this.map[this.row - 1].length;
        return remaining;
    }

    private getDownWallRow() {
        return this.map.map(r => r.charAt(this.column - 1)).join().indexOf('#', this.row - 1) + 1;
    }

    private getRightWallColumn() {
        return this.map[this.row - 1].indexOf('#', this.column - 1) + 1;
    }

    private updateDirection(rotate: string) {
        this.facing = (rotate == 'R' ? this.facing + 1 : this.facing + 3) % 4;
    }

    Print() {
        console.log(this.map);
    }
}