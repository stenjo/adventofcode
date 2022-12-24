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
    Move():number {

        if (this.proposedDirection == Direction.None) {
            return 0;
        }

        if (this.proposedDirection == Direction.North) {
            this.y -= 1
        }
        if (this.proposedDirection == Direction.South) {
            this.y += 1
        }
        if (this.proposedDirection == Direction.West) {
            this.x -= 1
        }
        if (this.proposedDirection == Direction.East) {
            this.x += 1
        }
        this.proposedDirection = Direction.None
        return 1
    }
    direction: Direction
    proposedDirection!: Direction;
    constructor(x: number, y: number) {
        super(x, y);
        this.direction = Direction.North
        this.proposedDirection = Direction.None
    }

    SetNextDirection() {
        this.direction += 1;
        this.direction %= 4;
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
    Spaces(): number {
        let minX = this.elves.map(c=> c.x).sort((a, b) => b - a).pop() as number
        let minY = this.elves.map(c=> c.y).sort((a, b) => b - a).pop() as number
        let maxX = this.elves.map(c=> c.x).sort((a, b) => a - b).pop() as number
        let maxY = this.elves.map(c=> c.y).sort((a, b) => a - b).pop() as number

        return (maxX-minX+1)*(maxY-minY+1) - this.elves.length

    }
    MoveAll() {
        let moves = 0
        this.elves.forEach(e => {
            if (this.ProposesAt(e.x, e.y, e.proposedDirection) == 1)
                moves += e.Move();

            e.SetNextDirection()
        });
        return moves;
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
        this.proposes = [];
        this.elves.forEach(e => {

            if (!this.isElvesAround(e.x, e.y)) return

            let dir = e.direction
            let pX = this.proposeX(e.x, dir)
            let pY = this.proposeY(e.y, dir)

            for (let i = 0; i < 4; i++) {
                if (!this.isAnyElvesInDirection(e.x, e.y, dir)) {
                    this.addProposal(pX, pY);
                    e.proposedDirection = dir;
                    return
                }
                dir = (dir + 1) % 4
                pX = this.proposeX(e.x, dir)
                pY = this.proposeY(e.y, dir)
            }
        });
    }
    isElvesAround(x: number, y: number) {
        return this.IsElfAt(x-1, y-1)   || this.IsElfAt(x, y-1) || this.IsElfAt(x+1, y-1)
            || this.IsElfAt(x-1, y)     || this.IsElfAt(x+1,y)
            || this.IsElfAt(x-1, y+1)   || this.IsElfAt(x, y+1) || this.IsElfAt(x+1, y+1)
    }
    private isAnyElvesInDirection(x:number, y:number, dir: Direction):boolean {
        if (dir == Direction.North) {
            y -= 1
            return this.IsElfAt(x-1, y) || this.IsElfAt(x, y) || this.IsElfAt(x+1, y)
        }
        if (dir == Direction.South) {
            y += 1
            return this.IsElfAt(x-1, y) || this.IsElfAt(x, y) || this.IsElfAt(x+1, y)
        }
        if (dir == Direction.West) {
            x -= 1
            return this.IsElfAt(x, y-1) || this.IsElfAt(x, y) || this.IsElfAt(x, y+1)
        }
        if (dir == Direction.East) {
            x += 1
            return this.IsElfAt(x, y-1) || this.IsElfAt(x, y) || this.IsElfAt(x, y+1)
        }
        return false
    }
    private proposeX(x: number, direction: Direction) {
        if (direction == Direction.West) {
            return x - 1
        }
        if (direction == Direction.East) {
            return x + 1
        }
        return x
    }
    private proposeY(y: number, direction: Direction) {
        if (direction == Direction.North) {
            return y - 1
        }
        if (direction == Direction.South) {
            return y + 1
        }
        return y
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
