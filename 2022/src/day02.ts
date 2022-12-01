// --- Day 2: 

import fs from 'fs';
import path from 'path';

export class Scan {

    constructor(fname: string) {
        let filename = path.join(__dirname, fname);
        let lines = fs.readFileSync(filename, 'utf8').trim().split('\n');
    }
}