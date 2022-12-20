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
    has: string = ''
    constructor(x: number, y: number, z: number) {
        this.x = x
        this.y = y
        this.z = z
    }
}

export class Scanner {

    ObsidianMap() {
        let obsMap: string[][][] = []
        let minX = this.cubes.map(c=> c.x).sort((a, b) => b - a).pop() as number
        let minY = this.cubes.map(c=> c.y).sort((a, b) => b - a).pop() as number
        let minZ = this.cubes.map(c=> c.z).sort((a, b) => b - a).pop() as number
        let maxX = this.cubes.map(c=> c.x).sort((a, b) => a - b).pop() as number
        let maxY = this.cubes.map(c=> c.y).sort((a, b) => a - b).pop() as number
        let maxZ = this.cubes.map(c=> c.z).sort((a, b) => a - b).pop() as number

        let gaps = this.GapCubes()
        // Get lava and air cubes
        for (let x = 0; x < maxX - minX + 1; x++) {
            obsMap[x] = new Array(maxX - minX + 1)
            for (let y = 0; y < maxY - minY + 1; y++) {
                obsMap[x][y] = new Array(maxY - minY + 1)
                for (let z = 0; z < maxZ - minZ + 1; z++) {
                    obsMap[x][y][z] = '.'
                    if (gaps.findIndex(g=> g.x === x + minX && g.y === y + minY && g.z === z + minZ) > -1) {
                        obsMap[x][y][z] = ' '
                    }
    
                    if (this.cubes.findIndex(c=>c.x == x+minX && c.y == y+minY && c.z == z+minZ) > -1) {
                        obsMap[x][y][z] = 'X'
                    }
                }
            }
        }

        return obsMap
    }
    PrintMap(m: string[][][]) {
        let map = []

        for (let x = 0; x < m.length; x++) {
            let block = ''
            for (let y = 0; y < m[x].length; y++) {
                block += m[x][y].join('')+'\n'
            }
            map.push(block)
        }

        return map
    }

    ExternalExposedSides(): any {
        let commonGapSides = this.GapCubes().map(g => {
            let common: number = 0;
            [g.x-1, g.x, g.x+1].forEach(x=> {
                [g.y-1, g.y, g.y+1].forEach(y=> {
                    [g.z-1, g.z, g.z+1].forEach(z=>{
                        let cube = this.cubes.findIndex(c=>c.x==x && c.y==y && c.z==z)
                        if (cube > -1) {
                            if (this.hasOneGapSideCommon(cube, g))
                                common += 1
                        }
                    })
                })
            })
            return common
        })
        let sides = commonGapSides.reduce((acc, s) => acc + s)

        return this.ExposedSides() - sides
    }
    GapCubes():Cube[] {
        let gapCubes:Cube[] = []
        let minX = this.cubes.map(c=> c.x).sort((a, b) => b - a).pop() as number
        let minY = this.cubes.map(c=> c.y).sort((a, b) => b - a).pop() as number
        let maxX = this.cubes.map(c=> c.x).sort((a, b) => a - b).pop() as number
        let maxY = this.cubes.map(c=> c.y).sort((a, b) => a - b).pop() as number

        for (let x = minX+1; x < maxX; x++) {
            for (let y = minY+1; y < maxY; y++) {
                let cubesInZ:Cube[] = this.cubes.filter(c => c.x == x && c.y == y)
                let minZ = cubesInZ.map(c=> c.z).sort((a, b) => b - a).pop() as number
                let maxZ = cubesInZ.map(c=> c.z).sort((a, b) => a - b).pop() as number
                for (let z = minZ+1; z < maxZ; z++) {
                    let notFound = cubesInZ.findIndex(c=> c.z == z) < 0;
                    if (notFound) {
                        gapCubes.push(new Cube(x,y,z))
                    }
                }
            }
        }

        return gapCubes
    }
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

    private hasOneGapSideCommon(c1: number, gap: Cube): boolean {
        return (Math.abs(this.cubes[c1].x - gap.x)
            + Math.abs(this.cubes[c1].y - gap.y)
            + Math.abs(this.cubes[c1].z - gap.z)) == 1;
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