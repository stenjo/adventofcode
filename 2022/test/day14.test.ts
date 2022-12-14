import { Cave, LoadLines } from '../src/day14'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day14.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Cave should', () => {
    it('not be null', () => {
        let c = new Cave()

        expect(c).not.toBeNull()
    })

    it('initialize', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        expect(c.structures.length).toBeGreaterThan(0)
    })
    it('draw one vertical line of rock', () => {
        let c = new Cave(['498,4 -> 498,6'])

        expect(c.structures.length).toBe(3)
        expect(c.RockAt(498,5)).toBe(true)
    })
    it('draw one horisontal line of rock', () => {
        let c = new Cave(['498,6 -> 496,6'])

        expect(c.structures.length).toBe(3)
        expect(c.RockAt(497,6)).toBe(true)
    })
    it('draw two lines of rock', () => {
        let c = new Cave(['498,4 -> 498,6 -> 496,6'])

        expect(c.structures.length).toBe(5)
        expect(c.RockAt(498,5)).toBe(true)
        expect(c.RockAt(497,6)).toBe(true)
    })
    it('draw test structures', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        expect(c.structures.length).toBe(20)
        expect(c.RockAt(498,5)).toBe(true)
        expect(c.RockAt(497,6)).toBe(true)
        expect(c.RockAt(502,9)).toBe(true)
    })
})