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
    it('draw one line of rock', () => {
        let c = new Cave(['498,4 -> 498,6'])

        expect(c.structures.length).toBe(3)
    })
})