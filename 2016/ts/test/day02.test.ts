import {Bathroom} from '../src/day02'


describe('Bathroom should', () => {
    it('start at 5', () => {
        let b = new Bathroom();
        expect(b.IsAt()).toBe(5);
    })
    it('be at 2 when UP', () => {
        let b = new Bathroom();
        b.Move("U");
        expect(b.IsAt()).toBe(2);
    })
})