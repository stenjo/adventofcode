
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
    GetRopeVisits(): number {
        return this.ropeVisits.length
    }
    RopeAt(x: number, y: number): number {
        let knot = this.knotMap.find(k => k.x === x && k.y === y)
        if (knot != null) {
            return knot.count
        }
        return 0
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
    UpdateTail(head: Knot) {

        if (Math.abs(head.y - this.tail.y) > 1) {
            if (head.y < this.tail.y) this.tail.y -= 1
            if (head.y > this.tail.y) this.tail.y += 1
            this.tail.x = head.x
        }

        if (Math.abs(this.head.x - this.tail.x) > 1) {
            if (head.x < this.tail.x) this.tail.x -= 1
            if (head.x > this.tail.x) this.tail.x += 1
            this.tail.y = head.y
        }

        this.Visit(this.tail)
    }
    MoveD() {
        this.head.y -= 1
        this.UpdateTail(this.head)
    }
    MoveU() {
        this.head.y += 1
        this.UpdateTail(this.head)
    }
    MoveL() {
        this.head.x -= 1
        this.UpdateTail(this.head)
    }
    MoveR() {
        this.head.x += 1
        this.UpdateRope(this.head)
        this.UpdateTail(this.head)
    }
    UpdateRope(head: Knot) {
        let latest = this.knotMap.reverse()[0]

        if (latest.y < head.y) {
        }

        this.knotMap[0].count--;
        if (this.knotMap[0].count === 0) {
            this.ropeVisits.push(this.knotMap[1].Clone())
        }
        let knot = head.Clone();
        knot.count = 1
        this.knotMap.push(knot);
    }
    GetTailVisits(): number {
        return this.tailVisits.length
    }
    Visit(tail: Knot) {
        if (!this.tailVisits.some(t => t.x === tail.x && t.y === tail.y)) {
          this.tailVisits.push(tail.Clone());
        }
    }

    head: Knot;
    tail: Knot;
    tailVisits: Knot[];
    knotMap: Knot[];
    ropeVisits: Knot[];

    constructor(ropelength: number = 3) {
        this.head = new Knot(0,0);
        this.tail = new Knot(0,0);
        this.tailVisits = [];
        this.tailVisits.push(this.tail.Clone());
        this.knotMap = [];
        this.knotMap.push(new Knot(0,0));
        this.knotMap[0].count = ropelength;
        this.ropeVisits = [];
        this.ropeVisits.push(new Knot(0,0));
    }
}