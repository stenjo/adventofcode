import * as fs from 'fs';
import * as path from 'path';

export class Bathroom {
    GetKey(arg0: string): any {

        for (let i = 0; i < arg0.length; i++) {
            this.Move(arg0[i]);
        }
        return this.IsAt();
    }
    location : number = 5;

    Move(direction: any) {
        if (direction == 'U') {
            if (this.location > 3) {
                this.location -= 3;
            }
        }
        if (direction === 'L') {
            if (notAtLeftEdge(this.location)) {
                this.location -= 1;
            }
        }
        if (direction === 'R') {
            if (notAtRightEdge(this.location)) {
                this.location += 1;
            }
        }
        if (direction === 'D') {
            if (this.location < 7) {
                this.location += 3;
            }
        }

        function notAtRightEdge(l:number): boolean {
            return l !== 3 && l !== 6 && l !== 9;
        }

        function notAtLeftEdge(l: number): boolean {
            return l > 1 && l !== 4 && l !== 7;
        }
    }

    IsAt(): number {
        return this.location;    
    }

    Part1(lines: string[]): number {

        let code = 0;
        for (let i = 0; i < lines.length; i++) {
            code = code * 10 + this.GetKey(lines[i]);
        }
        return code;

    }

    LoadLines():string[] {
        let filename = path.join(__dirname, '../../day02.txt')
        let lines = fs.readFileSync(filename, 'utf8').trim().split('\n')
        return lines
    }

}
