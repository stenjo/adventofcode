// --- Day 25: Full of Hot Air ---
// https://adventofcode.com/2022/day/25

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

export class Snafu {
    toNum(snafu:string): number {
        let digit = snafu.split('')
        let num = 0
        for (let i = 0; i < digit.length; i++) {
            num *= 5
            num += getValue(digit[i])
        }        
        return num

        function getValue(digit: string) {
            return digit === '=' ? -2 : digit === '-' ? -1 : Number(digit);
        }
    }
    numbers: string[] = [];
    constructor(snafu: string[] = []) {
        snafu.forEach(s => this.numbers.push(s))
    }
}