// --- Day 3: Binary Diagnostic ---
import * as fs from 'fs';
import * as path from 'path';

function getlines(): string[] {
    let file = path.join(__dirname,'../input/day03.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}

// 011110011100
// 010001010101
// 111111110000
// 011101100011
// 000111100100

// Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
// The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
// The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
// So, the gamma rate is the binary number 10110, or 22 in decimal.


// Part 1

export function getMostCommonBit(line: string): number {

    let zeros = 0;
    let ones = 0;

    for (let i = 0; i < line.length; i++) {

        if (line.charAt(i) === '0') {
            zeros += 1;
        }
        if (line.charAt(i) === '1') {
            ones += 1;
        }
    }

    if (zeros > ones) {
        return 0;
    }
    return 1;
}

export function getLeastCommonBit(line: string): number {

    let zeros = 0;
    let ones = 0;

    for (let i = 0; i < line.length; i++) {

        if (line.charAt(i) === '0') {
            zeros += 1;
        }
        if (line.charAt(i) === '1') {
            ones += 1;
        }
    }

    if (zeros <= ones) {
        return 0;
    }
    return 1;
}

export function getBitSlice(lines: string[], position: number):string {

    let slice = "";

    for (let i = 0; i < lines.length; i++) {
        slice += lines[i][position];
    }
    return slice;
}
export function getMostCommonBits(lines: string[]):string {

    let mostCommonBits = "";
    for (let i = 0; i < lines[0].trim().length; i++) {
        let bit = getMostCommonBit(getBitSlice(lines, i));
        if (bit === 0) {
            mostCommonBits += '0';
        }
        if (bit === 1) {
            mostCommonBits += '1';
        }
    }

    return mostCommonBits;
}

export function getLeastCommonBits(lines: string[]):string {

    let leastCommonBits = "";
    for (let i = 0; i < lines[0].trim().length; i++) {
        let bit = getLeastCommonBit(getBitSlice(lines, i));
        if (bit === 0) {
            leastCommonBits += '0';
        }
        if (bit === 1) {
            leastCommonBits += '1';
        }
    }

    return leastCommonBits;
}

export function getBinaryValue(line: string):number {

    let value = 0;
    for (let i = 0; i < line.trim().length; i++) {
        value *= 2;
        if (line.charAt(i) === '1') {
            value += 1;
        }
    }
    return value;
}

export function getPowerConsumption(lines: string[]): number {

    let gammaRate = getBinaryValue(getMostCommonBits(lines));
    let epsilonRate = getBinaryValue(getLeastCommonBits(lines));

    return gammaRate * epsilonRate;

}

// let result = getPowerConsumption(getlines());
// console.log('Part 1: ', result);

// Part 2

export function filterList(lines: string[], pattern: string): string[] {

    let result = [];
    for (let i = 0; i < lines.length; i++) {
        if (lines[i].startsWith(pattern)) {
            result.push(lines[i]);
        }
    }

    return result;
}

export function getOxygenRating(lines: string[]): number {
    let rate = 0;
    let pos = 0;
    let pattern = "";
    while (lines.length > 1) {
        let bit = getMostCommonBit(getBitSlice(lines, pos));
        pattern += bit.toString();
        lines = filterList(lines, pattern);
        pos++;
    }
    // 
    rate = getBinaryValue(lines[0]);

    return rate;
}

export function getCo2ScrubberRating(lines: string[]): number {
    let rate = 0;
    let pos = 0;
    let pattern = "";
    while (lines.length > 1) {
        let bit = getLeastCommonBit(getBitSlice(lines, pos));
        pattern += bit.toString();
        lines = filterList(lines, pattern);
        pos++;
    }
    // 
    rate = getBinaryValue(lines[0]);

    return rate;
}

export function getLifeSupportRating(lines: string[]): number {

    let oxygenRate = getOxygenRating(lines);
    let co2Rating = getCo2ScrubberRating(Object.assign([],lines));
 
    return oxygenRate * co2Rating;
}

// result = getLifeSupportRating(getlines());
// console.log('Part 2: ', result);

