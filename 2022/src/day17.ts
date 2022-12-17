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
    height!: number;
    floor!: string;
    Height(): number {
        return this.height;
    }
    Floor(): any {
        return this.floor
    }
    lineHeight!: number;
    LineHeight(): any {
        return this.lineHeight
    }
    DownWithJet(jet: string) {
        this.lineHeight --
        if (jet === '>') this.PushRight();
        if (jet === '<') this.PushLeft();

        if (this.lineHeight == 1 && this.Floor() === '') {
            this.lineHeight = 0
            this.floor = this.line[0]
            this.height = this.line.length
            return
        }
        if (this.lineHeight == 1) {
            let fits:boolean = true;
            for (let i = 0; i < this.line[0].length; i++) {
                if (this.line[0].charAt(i) == '#' && this.floor.charAt(i) == '#') fits = false;
            }

            if (fits) {
                let result = '';
                for (let i = 0; i < this.line[0].length; i++) {
                    if (this.line[0].charAt(i) === '#' || this.floor.charAt(i) === '#') {
                        result += '#'
                    }
                    else {
                        result += ' '
                    }
                }
                this.floor = result
                this.height += this.line.length -1
            }
            else {
                this.height += this.line.length
            }
        }

    }
    PushLeft() {
        for (let i = 0; i < this.line.length; i++) {
            if (this.line[i].charAt(0) !== ' ') return
        }

        for (let i = 0; this.line[i] !== undefined && i < this.line[i].length; i++) {
            this.line[i] = this.line[i].slice(1, this.line[i].length) + ' ';
        }
    }
    PushRight() {
        for (let i = 0; i < this.line.length; i++) {
            if (this.line[i].charAt(this.line[i].length-1) !== ' ') return
        }

        for (let i = 0; this.line[i] != undefined && i < this.line[i].length; i++){
            this.line[i] = ' ' + this.line[i].slice(0, -1);
        }
    }
    line: string[] = [];
    Line(): string {
        return this.line[0]
    }
    rocks: Rock[] = [];
    current!: Rock;

    Rock(): string {
        return this.rocks[0].shape[0];
    }
    NewRock(rockNo:number = 0) {
        this.current = this.rocks[rockNo]
        this.line = new Array(this.current.shape.length)
        this.current.shape.forEach((line, index, shape) => {
            let i = shape.length-1
            if (line.length == 4) {
                this.line[i-index] = '  '+ line +' '
            }
            if (line.length == 3) {
                this.line[i-index] = '  '+ line +'  '
            }

        })
        this.lineHeight = 3
    }

    constructor() {
        this.AddRock(['####']);
        this.AddRock([' # ','###',' # '])

        this.floor = ''
    }

    AddRock(pattern: string[]) {
        this.rocks.push(new Rock(pattern));
    }
}