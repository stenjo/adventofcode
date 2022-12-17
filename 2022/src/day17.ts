// --- Day 17: Pyroclastic Flow ---

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

export class Rock {
    shape: string[];

    constructor(shape: string[] = []) {
        this.shape = shape;
    }
}
export class Chamber {
    Floor(): any {
        return '####   '
    }
    lineHeight!: number;
    LineHeight(): any {
        return this.lineHeight
    }
    DownWithJet(jet: string) {
        if (this.lineHeight == 1 && this.Floor() === '####   ') {
            this.lineHeight = 0
            return
        }

        this.lineHeight --
        if (jet === '>') this.PushRight();
        if (jet === '<') this.PushLeft();
    }
    PushLeft() {
        if (this.line.charAt(0) === ' ') {
            this.line = this.line.slice(1, this.line.length) + ' ';
        }
    }
    PushRight() {
        if (this.line.charAt(this.line.length-1) === ' ') {
            this.line = ' ' + this.line.slice(0, -1);
        }
    }
    line!: string;
    Line(): string {
        return this.line
    }
    rocks: Rock[] = [];
    current!: Rock;

    Rock(): string {
        return this.rocks[0].shape[0];
    }
    DropRock() {
        this.current = this.rocks[0]
        this.line = '  '+this.current.shape+' '
        this.lineHeight = 4
    }

    constructor() {
        this.rocks.push(new Rock(['####']))
    }
}