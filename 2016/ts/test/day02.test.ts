import {Bathroom} from '../src/day02'


describe('Bathroom should', () => {
    it('start at 5', () => {
        let b = new Bathroom();
        expect(b.IsAt()).toBe(5);
    })
    it('be at 2 when UP', () => {
        let b = new Bathroom();
        b.Move('U');
        expect(b.IsAt()).toBe(2);
    })
    it('be at 1 when UP and LEFT', () => {
        let b = new Bathroom();
        b.Move('U');
        b.Move('L');
        expect(b.IsAt()).toBe(1);
    })
    it('be at 1 when UP and LEFT and LEFT', () => {
        let b = new Bathroom();
        b.Move('U');
        b.Move('L');
        b.Move('L');
        expect(b.IsAt()).toBe(1);
    })

    it('decod ULL to 1', () => {
        let b = new Bathroom();
        expect(b.GetKey("ULL")).toBe(1);
    })

    it('decode RRDDD to 9 given ULL to 1', () => {
        let b = new Bathroom();
        b.GetKey("ULL")
        expect(b.GetKey("RRDDD")).toBe(9);
    })
})