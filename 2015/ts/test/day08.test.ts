import { Matchsticks } from '../src/day08'

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
})
