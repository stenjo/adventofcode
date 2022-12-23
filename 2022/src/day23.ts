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
    SouthWest, 
    None = 100
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
    Move() {

        if (this.direction == Direction.North) {
            this.y -= 1
        }
        if (this.direction == Direction.South) {
            this.y += 1
        }
        if (this.direction == Direction.West) {
            this.x -= 1
        }
        if (this.direction == Direction.East) {
            this.x += 1
        }

        this.direction += 1
        this.direction %= 4
    }
    direction: Direction
    constructor(x: number, y: number) {
        super(x, y);
        this.direction = Direction.North
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
    MoveAll() {
        this.elves.forEach(e => {
            if (this.ProposesAt(e.x, e.y, e.direction) == 1)
                e.Move();
        });
    }
    ProposesAt(x: number, y: number, dir:Direction = Direction.None): number {
        if (dir == Direction.North) {
            y -= 1
        }
        if (dir == Direction.South) {
            y += 1
        }
        if (dir == Direction.West) {
            x -= 1
        }
        if (dir == Direction.East) {
            x += 1
        }
        let p = this.proposes.find(p => p.x === x && p.y === y)
        if (p !== undefined) {
            return ( p as Proposal).count;
        }
        return 0
    }
    Propose() {
        this.elves.forEach(e => {

            let pX = e.x
            let pY = e.y - 1

            if (!this.IsElfAt(pX, pY)) {
                this.addProposal(pX, pY);
                return
            }
            
            pY = e.y + 1
            if (!this.IsElfAt(pX, pY)) {
                this.addProposal(pX, pY);
                return
            }
        });
    }
    private addProposal(x: number, y: number) {

        if (this.ProposesAt(x, y) > 0) {
            (this.proposes.find(p => p.x === x && p.y === y) as Proposal).count++;
            return
        }

        this.proposes.push(new Proposal(x, y));
    }

    IsElfAt(x: number, y: number): boolean {
        let elf = this.elves.find(e => e.x === x && e.y === y)
        if (elf != undefined) {
            return true
        }
        return false;
    }
    GetElfAt(x: number, y: number): Elf | undefined {
        let elf = this.elves.find(e => e.x === x && e.y === y)
        if (elf != undefined) {
            return elf
        }
        return undefined;
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