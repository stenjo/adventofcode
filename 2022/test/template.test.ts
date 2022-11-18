import { part1, part2 } from '../src/template';
import * as fs from 'fs';
import * as path from 'path';

describe('Navigation tests', () => {

    test('Always true test should always be green', () => {
        expect(true).toBe(true);
    })

    test('Should return part1', () => {

        let result = part1(['forward 5']);
        expect(result).toStrictEqual([0,0]);
    })

    test('Should return part2', () => {

        let result = part2(getlines());
        expect(result[0]*result[1]).toBe(0);
    })

})


function getlines(): string[] {
    let file = path.join(__dirname,'input/day02.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}
