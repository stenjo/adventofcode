
import * as fs from 'fs';
import * as path from 'path';

export class Passphrase {
    countValidPart2Phrases(): any {
        let count = 0;
        this.lines.forEach((line) => {
            if (this.isValid(line.trim()) && !this.hasAnagram(line)) {
                count++;
            }
        })

        return count;
    }
    hasAnagram(passPhrase: string): boolean {

        let parts = passPhrase.split(' ');
        for (let i = 0; i < parts.length-1; i++) {
            for (let j = i+1; j < parts.length; j++) {
                if (this.isAnagram(parts[i], parts[j])) {
                    return true;
                }
            }
        }
        return false;
    }
    isAnagram(first: string, second: string): boolean {
        let x = getSortedString(first);
        let y = getSortedString(second);

        return x == y;

        function getSortedString(s:string):string {
            return s.split('').sort((a, b) => {
                if (a > b)
                    return -1;
                if (a < b)
                    return 1;
                return 0;
            }).join('');
        }
    }
 
    countValidPhrases(): any {
        let count = 0;
        this.lines.forEach((line) => {
            if (this.isValid(line.trim())) {
                count++;
            }
        })

        return count;
    }

    isValid(passPhrase: string): any {
        let parts = passPhrase.split(' ');
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