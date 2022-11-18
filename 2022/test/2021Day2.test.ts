import { parseCommand } from '../src/2021Day2';

describe('Navigation tests', () => {

    test('Navigation forward 5 should return forward and 5', () => {
        expect(parseCommand('forward 5')[0]).toBe('forward');
        expect(parseCommand('forward 5')[1]).toBe(5);
    })

    test('Navigation backward 5 should return', () => {
        
    })
})