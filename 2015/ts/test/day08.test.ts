import { Matchsticks } from '../src/day08'

const m = new Matchsticks();
describe('Matchsticks', () => {
    it('should count zero caracters', ()=>{
        
        let chars = m.CountChars('""');

        expect(chars).toBe(0);
    })
})