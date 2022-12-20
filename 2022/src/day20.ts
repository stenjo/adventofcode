// --- Day 20: Grove Positioning System ---

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

export class Decryptor {
    GroveCoordinateSum(): any {
        return this.NumAt(1000) + this.NumAt(2000) + this.NumAt(3000);
    }
    NumAt(pos: number): any {
        let pos0 = this.numbers.indexOf(0)
        return this.numbers[(pos0+pos)%(this.numbers.length)];
    }
    Mix() {
        let origin:number[];
        origin = this.numbers.map(n => n as number);
        for (let i = 0; i < origin.length; i++) {
            this.numbers = this.Move(origin[i], this.numbers);
        }
    }
    Move(num: number, list:number[]):number[] {
        let pos = list.indexOf(num)
        list.splice(pos, 1);
        let len = list.length
        let newPos = (len + pos+num) % len
        if (newPos == 0) {
            list.push(num)
            return list
        }
        let first = list.slice(0, newPos)
        let second = list.slice(newPos)
        return first.concat(num, second)
    }
    Print(list:number[] = []): string {
        if (list.length === 0) return this.numbers.join(',');
        return list.join(',')
    }
    numbers: number[];
    constructor(numStr: string[]) {
        this.numbers = []
        numStr.forEach(n => this.numbers.push(Number(n)));
    }

}