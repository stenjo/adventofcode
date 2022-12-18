// --- Day 18: Boiling Boulders ---

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

export class Cube {
    x: number
    y: number
    z: number
    constructor(x: number, y: number, z: number) {
        this.x = x
        this.y = y
        this.z = z
    }
}

export class Scanner {
    ExposedSides(): number {

        if (this.cubes.length === 0) {return 0}
        if (this.cubes.length === 1) {return 6}

        let sides = 0
        for (let i = 0; i < this.cubes.length; i++) {
            let cubeSides = 6
            for (let j = 0; j < this.cubes.length; j++) {
                if (i !== j && this.hasOneSideCommon(i,j)) {
                    cubeSides -= 1
                }
            }
            
            sides += cubeSides

        }
        return sides
    }

    private hasOneSideCommon(c1: number, c2: number): boolean {
        return (Math.abs(this.cubes[c1].x - this.cubes[c2].x)
            + Math.abs(this.cubes[c1].y - this.cubes[c2].y)
            + Math.abs(this.cubes[c1].z - this.cubes[c2].z)) == 1;
    }

    LoadCubes(lines: string[]) {
        lines.forEach(l => {
            let [x,y,z] = l.split(',').map(n=> Number(n))
            this.cubes.push(new Cube(x,y,z))
        })
    }
    cubes:Cube[] = []

    constructor() {
        this.cubes = []
    }
}