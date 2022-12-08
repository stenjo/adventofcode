
// --- Day 8: Treetop Tree House ---

export class TreeGrid {
    MaxScenicScore(): number {
        let bestScore: number = 0;
        for (let y = 1; y <= this.treeGrid.length; y++) {
            for (let x = 1; x <= this.treeGrid[y-1].length; x++) {
                let score = this.TreeScenicScore(x,y)
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
        if (y == this.treeGrid.length) return 0;
        let count = 0;
        let height = this.TreeAt(x,y)
        for (let i = y+1; i <= this.treeGrid.length; i++) {
            count += 1
            if (this.TreeAt(x,i) > height) {
                return count;
            }
            height = this.TreeAt(x,i)
        }
        return count
    }
    TreeCountRight(x: number, y: number): number {
        const maxX = this.treeGrid[0].length
        if (x == maxX) return 0
        if (x == maxX-1) return 1
        let count = 1;
        let height = this.TreeAt(x+1,y)
        for (let i = x+2; i <= maxX; i++) {
            if (this.TreeAt(i,y) < height) {
                return count;
            }
            count++
            height = this.TreeAt(i,y)
        }
        return count;
    }
    TreeCountLeft(x: number, y: number): number {
        if (x == 1) return 0
        if (x == 2) return 1
        let count = 0;
        let height = this.TreeAt(x-1,y)
        for (let i = x-2; i >= 1; i--) {
            count += 1
            if (this.TreeAt(i,y) < height) {
                return count;
            }
            height = this.TreeAt(i,y)
        }
        return count;
    }
    TreeCountUp(x: number, y: number): number {
        if (y == 1) return 0
        if (y == 2) return 1

        let count = 0;
        let height = this.TreeAt(x,y-1)
        for (let i = y-2; i >= 1; i--) {
            count += 1
            if (this.TreeAt(x,i) < height) {
                return count;
            }
            height = this.TreeAt(x,i)
        }

        return count;
    }
    CountVisibleTops(): number {

        let count: number = 0;
        for (let x = 1; x <= this.treeGrid[1].length; x++) {
            for (let y = 1; y <= this.treeGrid.length; y++) {
                if (this.VisibleTop(x,y)
                 || this.VisibleBottom(x,y)
                 || this.VisibleLeft(x,y) 
                 || this.VisibleRight(x,y)) {
                    count += 1
                }
            }
        }

        return count
    }
    VisibleRight(x: number, y: number): boolean {
        for (let i = x+1; i <= this.treeGrid[y-1].length; i++) {
            if (this.TreeAt(i,y) >= this.TreeAt(x,y)) {
                return false;
            }
        }
        return true;
    }
    VisibleBottom(x: number, y: number): boolean {
        for (let i = y+1; i <= this.treeGrid.length; i++) {
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
        this.lines = fs.readFileSync(file, 'utf8').trim().split('\n')
    }
}