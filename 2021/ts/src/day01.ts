// --- Day 1: Sonar Sweep ---

// You're minding your own business on a ship at sea when the overboard alarm 
// goes off! You rush to see if you can help. Apparently, one of the Elves 
// tripped and accidentally sent the sleigh keys flying into the ocean!

// Before you know it, you're inside a submarine the Elves keep ready for 
// situations like this. 

// As the submarine drops below the surface of the ocean, it automatically 
// performs a sonar sweep of the nearby sea floor. On a small screen, the 
// sonar sweep report (your puzzle input) appears: each line is a measurement 
// of the sea floor depth as the sweep looks further and further away from 
// the submarine.

// For example, suppose you had the following report:

// 199
// 200
// 208
// 210
// 200
// 207
// 240
// 269
// 260
// 263
// This report indicates that, scanning outward from the submarine, the sonar 
// sweep found depths of 199, 200, 208, 210, and so on.
// The first order of business is to figure out how quickly the depth 
// increases, just so you know what you're dealing with - you never know if 
// the keys will get carried into deeper water by an ocean current or a fish 
// or something.
// To do this, count the number of times a depth measurement increases from 
// the previous measurement.

import * as fs from 'fs';
import * as path from 'path';

function getlines(): string[] {
    let file = path.join(__dirname,'../input/day01.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}

// Part 1

export function depthscan(lines: string[]): number { 

    let depts = lines.map(line => parseInt(line));

    let increases = 0;
    let previous = depts[0];
    for (let i = 0; i < depts.length; i++) {
        if (depts[i] > previous) {
            increases ++;
        }
        previous = depts[i];
    }
    return increases;
}
let result = depthscan(getlines());
console.log('Part 1: ', result);


// Part 2

export function depthsweep(lines: string[]): number {
    let depts = lines.map(line => parseInt(line));

    let increases = 0;
    let previous = depts[0]+depts[1]+ depts[2];
    for (let i = 0; i < depts.length + 2; i++) {
        let sum = depts[i + 1] + depts[i + 2] + depts[i];
        if (sum > previous) {
            increases ++;
        }
        previous = sum;
    }
    return increases;
}

result = depthsweep(getlines());
console.log('Part 2: ', result);
