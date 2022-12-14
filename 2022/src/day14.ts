// --- Day 14: Regolith Reservoir ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n')
        .map(line => line.trim());
    }
}
class Rock {
    x: number;
    y: number;
    constructor(x: number, y: number) { 
        this.x = x;
        this.y = y;
    }
}
export class Cave {
    structures: Rock[];

    constructor(input: string[] = ['']) {
        this.structures = []
        input.forEach(line => {
            let points:string[] = line.split(' -> ');
            let pts:number[][] = line.split(' -> ').map(point => point.split(',').map(n=>Number(n)))
            points.forEach(point => {
                let [x,y] = point.split(',').map(n=>Number(n));
                this.structures.push(new Rock(x,y));
            })
        })
    }

}