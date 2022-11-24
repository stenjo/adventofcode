import { Taxicab } from '../src/day01'

describe('Taxicab should', () => {
    it('return null for null', () => {
        expect(null).toBe(null);
    })
    it('return 2 for R2', () => {
        let t = new Taxicab();
        expect(t.Blocks("R2")).toBe(2)
    })
    it('return 3 for L3', () => {
        let t = new Taxicab();
        expect(t.Blocks("L3")).toBe(3)
    })
    it('return 5 for R2, R3', () => {
        let t = new Taxicab();
        expect(t.Blocks("R2, L3")).toBe(5)
    })
    it('leave you 2 blocks away for R2, R2, R2', () => {
        let t = new Taxicab();
        expect(t.Blocks("R2, R2, R2")).toBe(2)
    })
    it('leave you 12 blocks away for R5, L5, R5, R3', () => {
        let t = new Taxicab();
        expect(t.Blocks("R5, L5, R5, R3")).toBe(12)
    })
    it('leave you 22 blocks away for R15, L5, R5, R3', () => {
        let t = new Taxicab();
        expect(t.Blocks("R15, L5, R5, R3")).toBe(22)
    })
})

describe('Part 1 should', () => {
    it('give correct answer', () => {
        let t = new Taxicab();
        expect(t.Blocks(t.LoadLines())).toBe(307)
    })
})