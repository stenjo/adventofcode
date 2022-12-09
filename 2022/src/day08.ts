
// --- Day 8: Treetop Tree House ---

export class TreeGrid {
    MaxScenicScore(): number {
        const maxY = this.treeGrid.length
        const maxX = this.treeGrid[0].length
        let bestScore: number = 0;
        for (let y = 1; y <= maxY; y++) {
            for (let x = 1; x <= maxX; x++) {
                let score = this.TreeScenicScore(x,y)
                // console.log('['+x+','+y+']:'+score)
                if (score > bestScore) {
                    bestScore = score
                }
            }
        }
        return bestScore
    }
    TreeScenicScore(x: number, y: number): number {
        return this.TreeCountDown(x, y) 
        * this.TreeCountUp(x, y) 
        * this.TreeCountLeft(x, y) 
        * this.TreeCountRight(x, y)
    }
    TreeCountDown(x: number, y: number): number {
        const maxY = this.treeGrid.length

        if (y == maxY) return 0;

        let row: number[] = [this.TreeAt(x,y)];
        for (let i = y+1; i <= maxY; i++) {
            row.push(this.TreeAt(x,i));
        }
        return this.countVisible(row);
    }
    TreeCountRight(x: number, y: number): number {
        const maxX = this.treeGrid[0].length

        if (x == maxX) return 0
        let row: number[] = [this.TreeAt(x,y)];
        for (let i = x+1; i <= maxX; i++) {
            row.push(this.TreeAt(i,y));
        }
        return this.countVisible(row);
    }
    TreeCountLeft(x: number, y: number): number {
        if (x == 1) return 0

        let row: number[] = [this.TreeAt(x,y)];
        for (let i = x-1; i >= 1; i--) {
            row.push(this.TreeAt(i,y));
        }
        return this.countVisible(row);
    }
    TreeCountUp(x: number, y: number): number {
        if (y == 1) return 0

        let row: number[] = [this.TreeAt(x,y)];
        for (let i = y-1; i >= 1; i--) {
            row.push(this.TreeAt(x,i));
        }
        return this.countVisible(row);
    }
    countVisible(row:number[]):number {
        // console.log(row)
        if (row.length == 0 || row.length == 1) return 0
        let count = 1
        for (let i = 1; i < row.length-1; i++) {
            if (row[i] < row[0]) {
                count ++
            }
            else {
                return count
            }
        }
        return count
    } 
    CountVisibleTops(): number {
        const maxX = this.treeGrid[0].length
        const maxY = this.treeGrid.length

        let count: number = 0;
        for (let x = 1; x <= maxX; x++) {
            for (let y = 1; y <= maxY; y++) {
                if (this.VisibleTop(x,y)
                 || this.VisibleBottom(x,y)
                 || this.VisibleLeft(x,y) 
                 || this.VisibleRight(x,y)) {
                    count += 1
                // console.log('['+x+','+y+']:'+this.treeGrid[y-1].length)
            }
            }
        }

        return count
    }
    VisibleRight(x: number, y: number): boolean {
        const maxX = this.treeGrid[0].length
        if (x == maxX) return true;
        for (let i = x+1; i <= maxX; i++) {
            if (this.TreeAt(i,y) >= this.TreeAt(x,y)) {
                return false;
            }
        }
        return true;
    }
    VisibleBottom(x: number, y: number): boolean {
        const maxY = this.treeGrid.length
        if (y == maxY) return true;
        for (let i = y+1; i <= maxY; i++) {
            if (this.TreeAt(x,i) >= this.TreeAt(x,y)) {
                return false;
            }
        }
        return true;
    }
    VisibleTop(x: number, y: number): any {
        if (y == 1) return true;
        for (let i = y-1; i >= 1; i--) {
            if (this.TreeAt(x,i) >= this.TreeAt(x,y)) {
                return false;
            }
        }
        return true;
    }
    VisibleLeft(x: number, y: number): any {
        if (x == 1) return true;
        for (let i = x-1; i >= 1; i--) {
            if (this.TreeAt(i,y) >= this.TreeAt(x,y)) {
                return false;
            }
        }
        return true;
    }
    TreeAt(x: number, y: number): any {
        return this.treeGrid[y-1][x-1]
    }
    treeGrid: number[][];

    constructor(grid:string[]) {
        this.treeGrid = []
        grid.forEach(tree => {
            let treerow = tree.split('').map(t => parseInt(t))
            this.treeGrid.push(treerow);
        })
    }
}

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
        let file = path.join(__dirname,fname);
        this.lines = fs.readFileSync(file, 'utf8').trim().split('\n').map(line => line.trim())
    }
}