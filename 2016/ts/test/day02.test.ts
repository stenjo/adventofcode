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

    it('decode RRDDD to 9 given ULL', () => {
        let b = new Bathroom();
        b.GetKey("ULL")
        expect(b.GetKey("RRDDD")).toBe(9);
    })

    it('decode LURDL to 8 given ULL and RRDDD', () => {
        let b = new Bathroom();
        b.GetKey("ULL")
        b.GetKey("RRDDD")
        expect(b.GetKey("LURDL")).toBe(8);
    })

    it('decode UUUUD to 5 given ULL, RRDDD and LURDL', () => {
        let b = new Bathroom();
        b.GetKey("ULL")
        b.GetKey("RRDDD")
        b.GetKey("LURDL")
        expect(b.GetKey("UUUUD")).toBe(5);
    })

    it('let Part 1 return 1985 given ULL, RRDDD, LURDL and UUUUD', () => {
        let b = new Bathroom();
        expect(b.Part1(["ULL", "RRDDD", "LURDL", "UUUUD"])).toBe(1985)
    })

    it('let Part 1 return solution for real data', () => {
        let b = new Bathroom();
        expect(b.Part1(b.LoadLines())).toBe(73597)
    })
})