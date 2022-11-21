
// --- Day 1: Not Quite Lisp ---
// Santa is trying to deliver presents in a large apartment building, but he
// can't find the right floor - the directions he got are a little confusing.
// He starts on the ground floor (floor 0) and then follows the instructions
// one character at a time.

// An opening parenthesis, (, means he should go up one floor, and a closing
// parenthesis, ), means he should go down one floor.

// The apartment building is very tall, and the basement is very deep; he will
// never find the top or bottom floors.

// For example:

// (()) and ()() both result in floor 0.
// ((( and (()(()( both result in floor 3.
// ))((((( also results in floor 3.
// ()) and ))( both result in floor -1 (the first basement level).
// ))) and )())()) both result in floor -3.
// To what floor do the instructions take Santa?

export function findFloor(directions: string):number {

    let floor = 0;
    for (let i = 0; i < directions.length; i++) {
        if (directions[i] == '(') {
            floor += 1;
        }
        if (directions[i] == ')') {
            floor -= 1;
        }
    }
    return floor;
}

export function part1(): number { 
    return findFloor(getInput());
}

import * as fs from 'fs';
import * as path from 'path';
function getInput(): string {

    let filename = path.join(__dirname + '../../../day01.txt')
    let input = fs.readFileSync(filename, 'utf8').trim();

    return input
}