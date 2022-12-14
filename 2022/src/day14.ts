// --- Day 14: Regolith Reservoir ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    pairs: string[][];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n')
        .map(line => line.trim());
        this.pairs = []

        let pair:string[] = []
        this.lines.forEach(line => {
            if (line == '' && pair.length > 0) {
                this.pairs.push(pair)
                pair = []
            }
            else {
                pair.push(line)
            }
        })
        if (pair.length > 0) {
            this.pairs.push(pair)
        }
    }
}
