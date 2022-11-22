import { Matchsticks, Part1, Part2 } from '../src/day08'

const m = new Matchsticks();
describe('Matchsticks', () => {
    it('should count zero caracters', ()=>{
        
        let chars = m.CountChars('""');

        expect(chars).toBe(0);
    })

    it('should count 3 caracters', ()=>{
        
        let chars = m.CountChars('"abc"');

        expect(chars).toBe(3);
    })

    it('should count 7 caracters from escaped char in string', ()=>{
        
        let chars = m.CountChars('"aaa\\"aaa"');

        expect(chars).toBe(7);
    })

    it('should count 1 caracter from ascii char in string', ()=>{
        
        let chars = m.CountChars('"\\x27"');

        expect(chars).toBe(1);
    })

    it('should count encoded empty string', ()=>{

        let encodedChars = m.CountEncodedChars('""');

        expect(encodedChars).toBe(6);
    })

    it('should count 3 in encoded "abc"', ()=>{

        let encodedChars = m.CountEncodedChars('"abc"');

        expect(encodedChars).toBe(9);
    })

    it('should count 16 in encoded "aaa\\"aaa"', ()=>{

        let encodedChars = m.CountEncodedChars('"aaa\\"aaa"');

        expect(encodedChars).toBe(16);
    })

    it('should count 11 in encoded "\\x27"', ()=>{

        let encodedChars = m.CountEncodedChars('"\\x27"');

        expect(encodedChars).toBe(11);
    })
})

describe('Solutions', ()=>{
    it('Part 1 should return answer to real data', ()=>{
        expect(Part1()).toBe(1371)
    })
    it('Part 2 should return answer to real data', ()=>{
        expect(Part2()).toBe(2117)
    })
})
