import { depthscan, depthsweep } from "../src/day01";
import * as fs from 'fs';
import * as path from 'path';

describe("test depthscan", () => {
    test("depthscan", () => {
        expect(depthscan(getlines())).toBe(7);
    });
})

describe('testing depthsweep', () => {
    test('depthsweep', () => {
        let result = depthsweep(getlines());

        expect(result).toBe(5)
    })

})

function getlines(): string[] {
    let file = path.join(__dirname,'../input/day01.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}
