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
    it.skip('return 2 for R2, R2, R2', () => {
        let t = new Taxicab();
        expect(t.Blocks("R2, R2, R2")).toBe(2)
    })
})