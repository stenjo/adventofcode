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
    PushLeft() {
        if (this.floor.charAt(0) === ' ') {
            this.floor += ' '
            this.floor = this.floor.slice(1, this.floor.length);
        }
    }
    PushRight() {
        if (this.floor.charAt(this.floor.length-1) === ' ') {
            this.floor = ' ' + this.floor
            this.floor = this.floor.slice(0, -1);
        }
    }
    floor!: string;
    Floor(): string {
        return this.floor
    }
    rocks: Rock[] = [];
    current!: Rock;

    Rock(): string {
        return this.rocks[0].shape[0];
    }
    DropRock() {
        this.current = this.rocks[0]
        this.floor = '  '+this.current.shape+' '
    }

    constructor() {
        this.rocks.push(new Rock(['####']))
    }
}