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

export function getXYOfSquare(square: number): {x:number, y:number} {

    let x: number = 0;
    let y: number = 0;

    if ((square >= 2 && square < 4)
     || square == 9
     || square == 14
     || square == 24) {
        x = 1;
    }
    if (square >= 10 && square < 14) {
        x = 2;
    }
    if ((square >= 5 && square < 8) 
    || square == 16
    || square == 22) {
        x = -1;
    }
    if ((square >= 17 && square <= 21)) {
        x = -2;
    }

    if ((square >= 3 && square < 6) 
    || (square >= 12 && square < 19) 
    ) {
        y = 1;
    }
    if (square >= 13 && square < 18) {
        y = 2;
    }
    if ((square >= 7 && square < 11)
    || (square >= 20)) {
        y = -1;
    }
    if (square >= 21) {
        y = -2;
    }

    return {x, y}
}

export function getSteps(square: number): number {

    // Get largest odd ^2 higher than n
    let largeN = 1
    while (largeN ** 2 < square) largeN += 2
    // Get alternating vary count of 'layer'
    let vary = Math.floor(largeN / 2)
    // Starting is largeN - 1
    let start = largeN - 1
    // Starting vary value
    let doReduce = -vary
    // Difference from largeN**2 to our n
    const diff = largeN ** 2 - square
    for (let i = 0; i < diff; ++i) {
        // Loop diff times
        const sign = doReduce > 0 ? 1 : -1
        start += sign
        if (doReduce > 0) doReduce--
        else if (doReduce < 0) doReduce++

        if (doReduce === 0) doReduce = vary * sign * -1
    }
    return start;
}

export function getSqaresInCircle(circle:number): number {
    if (circle == 1) {
        return 1
    }
    let width = (1+2*(circle-1));
    return width*width-(width-2)*(width-2);
}

export function getRingLevel(square: number): number {
    let i = 0;
    let ring = 0;
    let sum = 1;
    let lengthOfRing = 0;

    while(sum < square){
        ring++;
        i++;
        sum = sum + 8 * ring;
        lengthOfRing = 8 * ring;
    }

    return ring;
}
