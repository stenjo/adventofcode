// --- Day 23: Unstable Diffusion ---

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

export enum Direction {
    North = 0,
    South,
    West,
    East,
    NorthEast,
    NorthWest,
    SouthEast,
    SouthWest 
}

class Pos {
    x: number;
    y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
}

export class Elf extends Pos {
    constructor(x: number, y: number) {
        super(x, y);
    }
}

export class Proposal extends Pos {
    count: number;
    constructor(x: number, y: number) {
        super(x, y);
        this.count = 1;
    }
}

export class Grove {
    ProposesAt(x: number, y: number): any {
        let p = this.proposes.find(p => p.x === x && p.y === y)
        if (p !== undefined) {
            return ( p as Proposal).count;
        }
        return 0
    }
    Propose() {
        this.elves.forEach(e => {

            let proposeX = e.x
            let proposeY = e.y - 1

            if (!this.elfAt(proposeX, proposeY)) {
                if (this.ProposesAt(proposeX, proposeY)) {
                    (this.proposes.find(p => p.x === proposeX && p.y === proposeY) as Proposal).count++
                }
                else 
                    this.proposes.push(new Proposal(proposeX, proposeY));
                return
            }
            
            proposeY = e.y + 1
            if (!this.elfAt(proposeX, proposeY)) {
                if (this.ProposesAt(proposeX, proposeY)) {
                    (this.proposes.find(p => p.x === proposeX && p.y === proposeY) as Proposal).count++
                }
                else 
                    this.proposes.push(new Proposal(proposeX, proposeY));
                return
            }
        });
    }
    elfAt(x: number, y: number): boolean {
        let elf = this.elves.find(e => e.x === x && e.y === y)
        if (elf != undefined) {
            return true
        }
        return false;
    }
    elves: Elf[] = [];
    proposes: Proposal[] = [];

    constructor(elves:string[] = []) {
        elves.forEach((l,y)=> {
            for (let x = 0; x < l.length; x++) {
                if (l.charAt(x) == '#') {
                    this.elves.push(new Elf(x, y));
                }
            }
        })
    }
}