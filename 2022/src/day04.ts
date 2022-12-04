import * as fs from 'fs';
import * as path from 'path';

export class Assignments {
    GetOverlappingPairs(data: string[]): any {
        let count = 0;

        data.forEach(pair => {
            let [first, second] = pair.split(',')
            if (this.OneOverlapsOther(first,second)) {
                count ++;
            }
        })

        return count;

    }
    OneOverlapsOther(first: string, second: string):boolean {
        let firstRange = this.GetRange(first);
        let secondRange = this.GetRange(second);
        if (firstRange.length >= secondRange.length) {
            let common = secondRange.filter(value => firstRange.includes(value));
            return common.length > 0
        }
        if (secondRange.length > firstRange.length) {
            let common = firstRange.filter(value => secondRange.includes(value));
            return common.length > 0
    
        }
        return false;
    }
    GetContainingPairs(data: string[]): any {
        let count = 0;

        data.forEach(pair => {
            let [first, second] = pair.split(',')
            if (this.OneContainsOther(first,second)) {
                count ++;
            }
        })

        return count;

    }
    OneContainsOther(first: string, second: string): boolean {
        let firstRange = this.GetRange(first);
        let secondRange = this.GetRange(second);
        if (firstRange.length >= secondRange.length) {
            let common = secondRange.filter(value => firstRange.includes(value));
            return common.length == secondRange.length
        }
        if (secondRange.length > firstRange.length) {
            let common = firstRange.filter(value => secondRange.includes(value));
            return common.length == firstRange.length
    
        }
        return false;
    }

    constructor() {

    }

    GetRange(rangeString: string):number[] {
        let [first, last] = rangeString.split('-');
        let as = parseInt(first);
        let ae = parseInt(last);
        let range: number[] = [];
        for (let i = as; i <= ae; i++) {
            range.push(i);
        }

        return range;
    }

    GetLines(fname: string): string[] {
        let file = path.join(__dirname,fname);
        let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

        return lines
    }
}