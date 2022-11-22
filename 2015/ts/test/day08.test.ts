import { Matchsticks, Part1 } from '../src/day08'

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
})

describe('Part 1', ()=>{
    it('should return answer to real data', ()=>{
        expect(Part1()).toBe(1371)
    })
})
