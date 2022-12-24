// --- Day 24: Blizzard Basin ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n').map(line => line.trim());
    }
}

class Pos {
    x: number;
    y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
}

export class Blizzard extends Pos {
    dir: string;
    constructor(x: number, y: number, dir:string) {
        super(x, y);
        this.dir = dir;
    }
}

export class Valley {
    valley: string[]
    width: number;
    height: number;
    start: Pos;
    end: Pos;
    blizzards: Blizzard[] = [];

    constructor(lines: string[]) {
        this.valley = []
        this.width = lines[0].length-2
        this.height = lines.length-2

        lines.forEach((line, y) =>{
            line.split('').forEach((c,x)=>{
                if (c === '>') 
                    this.blizzards.push(new Blizzard(x-1, y-1, '>'))
                if (c === 'v') 
                    this.blizzards.push(new Blizzard(x-1, y-1, 'v'))
            })
        })

        this.start = new Pos(0,-1)
        this.end = new Pos(this.width, this.height)

    }
}
