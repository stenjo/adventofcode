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
    RockResting(): boolean {
        return this.floor.length == 1;
    }
    height!: number;
    floor!: string[];
    Height(): number {
        return this.height;
    }
    Floor(): string {
        return this.floor[0]
    }
    rockHeight!: number;
    LineHeight(): any {
        return this.rockHeight
    }
    DownWithJet(jetStream: string) {
        let jets = jetStream.split('')
        jets.forEach(jet => {
            if (jet === '>') this.PushRight();
            if (jet === '<') this.PushLeft();
            
            let floorTop = this.floor.length - 1

            if (this.rockHeight <= floorTop) {
                if (this.fitsFloor(this.rockHeight-1)) {
                    this.rockHeight --
                    return
                }
                else {
                    
                }
            }
            this.rockHeight--
            return
            if (this.rockHeight == 1 && this.Floor() === '') {
                this.rockHeight = 0
                this.floor[0] = this.line[0]
                this.height = this.floor.length
                return
            }
            if (this.rockHeight == 1) {
    
                if (this.fitsFloor(0)) {
                    this.mergeLines(0);
                    for (let i = 1; i < this.line.length; i++) {
                        if (this.floor.length < i + 1) {
                            this.floor.push(this.line[i]);
                        }
                    }
                    this.height += this.line.length -1
                }
                else {
    
                    this.height += this.line.length
                }
            }
        })
    }
    private fitsFloor(lineNo: number): boolean {
        for (let i = 0; i < this.line[lineNo].length; i++) {
            if (this.line[lineNo].charAt(i) == '#' && this.floor[lineNo].charAt(i) == '#')
                return false;
        }
        return true;
    }

    private mergeLines(lineNo: number): void {
        let result = '';
        for (let i = 0; i < this.line[lineNo].length; i++) {
            if (this.line[lineNo].charAt(i) === '#' || this.floor[lineNo].charAt(i) === '#') {
                result += '#';
            }
            else {
                result += ' ';
            }
        }
        this.floor[lineNo] = result;
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
        this.rockHeight = 3 + this.floor.length
    }

    constructor() {
        this.AddRock(['####']);
        this.AddRock([' # ','###',' # '])
        this.AddRock(['  #','  #','###'])

        this.floor = ['       ']
    }

    AddRock(pattern: string[]) {
        this.rocks.push(new Rock(pattern));
    }
}