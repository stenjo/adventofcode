import * as fs from 'fs';
import * as path from 'path';

export class Triangle {
    
    a: number;
    b: number;
    c: number;
    constructor(l: string){
        let [a,b,c] = l.trim().split(/\s+/)
        this.a = parseInt(a);
        this.b = parseInt(b);
        this.c = parseInt(c);
    }
    valid():boolean {
        if (this.c === undefined || isNaN(this.c)) return false;
        if (this.a + this.b <= this.c) return false;
        if (this.a + this.c <= this.b) return false;
        if (this.b + this.c <= this.a) return false;
        return true;
    }
}

export class Possibles {
    countPossiblesInGroups(lines: string[]) {

        let count = 0;
        for (let i = 0; i < lines.length-2; i += 3) {
            let [a1,b1,c1] = lines[i].trim().split(/\s+/)
            let [a2,b2,c2] = lines[i+1].trim().split(/\s+/)
            let [a3,b3,c3] = lines[i+2].trim().split(/\s+/)
            let t = new Triangle([a1,a2,a3].join(' '));
            if (t.valid()) count++;
            t = new Triangle([b1,b2,b3].join(' '));
            if (t.valid()) count++;
            t = new Triangle([c1,c2,c3].join(' '));
            if (t.valid()) count++;
        }

        return count
    }
    countPossibles(lines:string[]):number {
        let count = 0;
        lines.forEach(line => {
            let t = new Triangle(line);
            if (t.valid()) count++;
        })
        return count
    }

    loadlines():string[] {
        let filename = path.join(__dirname, '../../day03.txt')
        let lines = fs.readFileSync(filename, 'utf8').trim().split('\n')
        return lines
    }
}

export class Part1 {
    solution() { 
        let p = new Possibles()
        return p.countPossibles(p.loadlines())
    }
}

export class Part2 {
    solution() { 
        let p = new Possibles()
        return p.countPossiblesInGroups(p.loadlines())
    }
}

