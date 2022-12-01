
import * as fs from 'fs';
import * as path from 'path';

export class Passphrase {
    countValidPhrases(): any {
        let count = 0;
        this.lines.forEach((line) => {
            if (this.isValid(line.trim())) {
                count++;
            }
        })

        return count;
    }

    isValid(arg0: string): any {
        let parts = arg0.split(' ');
        for (let i = 0; i < parts.length-1; i++) {
            if (parts.indexOf(parts[i], i+1) !== -1) {
                return false;
            }
        }
        return true;
    }
    lines: string[];

    constructor(fname: string) {
        let filename = path.join(__dirname, fname)
        this.lines = fs.readFileSync(filename, 'utf8').trim().split('\n')
    }
}