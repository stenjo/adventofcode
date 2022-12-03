import * as fs from 'fs';
import * as path from 'path';

export class Rucksack {
    getGroupPrioritySum(): any {
        let sum = 0
        for (let i = 0; i < this.lines.length-2; i+=3) {
            sum += this.getPriority(this.getCommonOfThree(
                [
                this.lines[i], 
                this.lines[i+1], 
                this.lines[i+2]]
                ))
        }
    
        return sum;
    }
    getCommonOfThree(items: string[]): any {

        for (let i = 0; i < items[0].length; i++) {
            let chr = items[0][i];
            if (items[1].includes(chr) && items[2].includes(chr)) {
                return chr;
            }
        }

        return ''
    }
    getPrioritySum(): any {
        let sum = 0
    
        this.lines.forEach((line) => {
            sum += this.getPriority(this.getCommonItem(line));
        })

        return sum;
    }

    lines: string[];
    load(fname: string) {
        
        let file = path.join(__dirname,fname);
        this.lines = fs.readFileSync(file, 'utf8').trim().split('\n')
    }

    getPriority(char: string): any {
        
        let code = char.charCodeAt(0) - "a".charCodeAt(0) + 1;
        if (code < 0) code += 58;
        return code;
    }
    getCommonItem(items: string): string {
        let a = items.substring(0, items.length/2);
        let b = items.substring(items.length/2, items.length);

        for (let i = 0; i <a.length; i++) {
            if (b.includes(a.charAt(i).toString())) {
                return a.charAt(i);
            }
        }
        return '';
    }
    constructor() {
        this.lines = [];
    }
}