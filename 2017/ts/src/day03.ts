// --- Day 3: Spiral Memory ---
// You come across an experimental new kind of memory stored on an infinite 
// two-dimensional grid.

// Each square on the grid is allocated in a spiral pattern starting at a
// location marked 1 and then counting up while spiraling outward. For
// example, the first few squares are allocated like this:

// 17  16  15  14  13
// 18   5   4   3  12
// 19   6   1   2  11
// 20   7   8   9  10
// 21  22  23---> ...

// Common files
import * as fs from 'fs';
import * as path from 'path';
// import 'Math';

function getlines(): string[] {
    let file = path.join(__dirname,'../input/day02.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}

export function manhattan(x: number, y: number): number {
    return Math.abs(x) + Math.abs(y);
}

export function getXYOfNumber(square: number): {x:number, y:number} {

    let x: number = 0;
    let y: number = 0;

    if (square === 2) {
        x = 1;
    }

    if (square === 3) {
        x = 1;
        y = 1;
    }
    return {x, y}
}