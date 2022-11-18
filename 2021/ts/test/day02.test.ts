import { parseCommand, navigate, navigateWithAim } from '../src/day02';
import * as fs from 'fs';
import * as path from 'path';

describe('Navigation tests', () => {

    test('Navigation forward 5 should return forward and 5', () => {
        expect(parseCommand('forward 5')).toStrictEqual({'command':'forward', 'value': 5});
    })

    test('Navigation forward 5 should return 5', () => {

        let result = navigate(['forward 5']);
        expect(result).toStrictEqual([5,0]);
    })

    test('Navigation forward 3 then 8 should return 11', () => {

        let result = navigate(['forward 3', 'forward 8']);
        expect(result).toStrictEqual([11,0]);
    })
    
    test('Navigation up 3 then down 8 should return depth 5', () => {

        let result = navigate(['up 3', 'down 8']);
        expect(result).toStrictEqual([0,5]);
    })

    test('Navigation testdata should return depth 150', () => {

        let result = navigate(getlines());
        expect(result[0]*result[1]).toBe(150);
    })

    test('Navigation testdata should return depth 900', () => {

        let result = navigateWithAim(getlines());
        expect(result[0]*result[1]).toBe(900);
    })

})


function getlines(): string[] {
    let file = path.join(__dirname,'input/day02.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}
