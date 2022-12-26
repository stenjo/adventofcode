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
            if (digit[i] === '=') {
                num -= 2
                continue
            }
            if (digit[i] === '-') {
                num -= 1
                continue
            }
            num += Number(digit[i])
        }        
        return num
    }
    numbers: string[] = [];
    constructor(snafu: string[] = []) {
        snafu.forEach(s => this.numbers.push(s))
    }
}