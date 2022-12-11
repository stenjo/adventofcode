
// --- Day 9: Rope Bridge ---

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
  
export class Knot {
    Clone(): Knot {
        return new Knot(this.x,this.y)
    }
    x: number;
    y: number;
    count: number;

    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
        this.count = 1;
    }
}

export class RopeModel {
    RopeAt(x: number, y: number): boolean {
        let knot = this.rope.find(k => k.x === x && k.y === y)
        if (knot != null) {
            return true
        }
        return false
    }
    KnotNumber(x: number, y: number): number {
        let knot = this.rope.find(k => k.x === x && k.y === y)
        return this.rope.indexOf(knot as Knot)
    }
    RunInstruction(instr: string) {
        const [dir, countStr] = instr.split(' ')
        const count = parseInt(countStr)

        for (let i = 0; i < count; i++) {
            if (dir === 'R') {
                this.MoveR()
            }
            if (dir === 'U') {
                this.MoveU()
            }
            if (dir === 'L') {
                this.MoveL()
            }
            if (dir === 'D') {
                this.MoveD()
            }
        }
    }
    UpdateTail(head: Knot, tail: Knot) {

        if (Math.abs(head.y - tail.y) > 1) {
            if (head.y < tail.y) tail.y -= 1
            if (head.y > tail.y) tail.y += 1
            tail.x = head.x
        }

        if (Math.abs(head.x - tail.x) > 1) {
            if (head.x < tail.x) tail.x -= 1
            if (head.x > tail.x) tail.x += 1
            tail.y = head.y
        }

        this.Visit(this.tail)
    }
    MoveD() {
        this.head.y -= 1
        this.UpdateTail(this.head, this.tail)
        this.UpdateKnots(this.head)
    }
    MoveU() {
        this.head.y += 1
        this.UpdateTail(this.head, this.tail)
        this.UpdateKnots(this.head)
    }
    MoveL() {
        this.head.x -= 1
        this.UpdateTail(this.head, this.tail)
        this.UpdateKnots(this.head)
    }
    MoveR() {
        this.head.x += 1
        this.UpdateTail(this.head, this.tail)
        this.UpdateKnots(this.head)
    }
    UpdateKnots(head: Knot) {

        this.rope[0].x = head.x
        this.rope[0].y = head.y
        for (let i = 1; i < this.rope.length; i++) {
            this.UpdateTail(this.rope[i-1], this.rope[i])
        }

        this.VisitRope(this.rope[this.rope.length-1])
    }
    GetRopeVisits(): number {
        return this.ropeVisits.length
    }
    VisitRope(tail: Knot) {
        if (!this.ropeVisits.some(t => t.x === tail.x && t.y === tail.y)) {
            this.ropeVisits.push(tail.Clone());
        }
    }
    GetTailVisits(): number {
        return this.tailVisits.length
    }
    Visit(tail: Knot) {
        if (!this.tailVisits.some(t => t.x === tail.x && t.y === tail.y)) {
          this.tailVisits.push(tail.Clone());
        }
    }

    PrintRopeVisits() {
        const minY = -35
        const maxY = 35
        const minX = -35
        const maxX = 35
        for (let y = maxY; y >= minY; y--) {
            let line = ''
            for (let x = minX; x <= maxX; x++) {
                if (x == 0 && y == 0) {
                    line += 's'
                } else {
                    line += this.RopeVisitAt(x,y) ? '#' : '.'
                }
            }
            console.log(line)
        }
    }
    RopeVisitAt(x: number, y: number):boolean {
        let knot = this.ropeVisits.find(k => k.x === x && k.y === y)
        if (knot != null) {
            return true
        }
        return false
    }

    PrintRope() {
        const minY = -5
        const maxY = 15
        const minX = -11
        const maxX = 15
        for (let y = maxY; y >= minY; y--) {
            let line = ''
            for (let x = minX; x <= maxX; x++) {
                if (x == 0 && y == 0) {
                    line += 's'
                } else if (this.rope[0].x == x && this.rope[0].y == y) {
                    line += 'H'
                } else {
                    line += this.RopeAt(x,y) ? this.KnotNumber(x,y) : '.'
                }
            }
            console.log(line)
        }
    }

    head: Knot;
    tail: Knot;
    tailVisits: Knot[];
    ropeVisits: Knot[];
    rope: Knot[];

    constructor(ropelength: number = 3) {
        this.head = new Knot(0,0);
        this.tail = new Knot(0,0);
        this.tailVisits = [];
        this.tailVisits.push(this.tail.Clone());
        this.rope = []
        for (var i = 0; i < ropelength; i++) {
            this.rope.push(new Knot(0,0))
        }
        this.ropeVisits = [];
        this.ropeVisits.push(new Knot(0,0));
    }
}

let r = new RopeModel(10)

let instr = new LoadLines('../test/input/day09-large.txt').lines

instr.forEach(line => {
    r.RunInstruction(line)
    // console.log('\n== ' + line + ' ==')
    // r.PrintRope()
})

console.log('\n== ' + 'Rope tail track' + ' ==')
r.PrintRopeVisits()
// console.log(r.ropeVisits)