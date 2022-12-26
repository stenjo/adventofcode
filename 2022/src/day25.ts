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
    SumSnafu(): any {
        return this.toSnafu(this.Sum())
    }
    Sum(): number {
        
        return this.numbers.map(n => this.toNum(n)).reduce((sum, n) => sum + n)
    }

    toSnafu(num: number): string {
        const translate:string[] = ['0', '1', '2', '=', '-']
        let snafu = ''

        while (num > 0) {
            let digit = num % 5

            snafu = translate[digit] + snafu
            num += digit === 3 ? 2 : digit === 4 ? 1 : 0
            num = Math.floor(num/5)
        }

        return snafu
    }
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
        this.numbers = snafu
    }
}