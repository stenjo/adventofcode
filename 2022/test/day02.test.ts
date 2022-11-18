import { parseCommand } from '../src/day02';
import * as fs from 'fs';
import * as path from 'path';

describe('Navigation tests', () => {

    test('Navigation forward 5 should return forward and 5', () => {
        expect(parseCommand('forward 5')[0]).toBe('forward');
        expect(parseCommand('forward 5')[1]).toBe(5);
    })

    test('Navigation backward 5 should return', () => {
        
    })
})


function getlines(): string[] {
    let file = path.join(__dirname,'../input/day01.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}
