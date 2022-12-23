import {Grove, LoadLines} from '../src/day23'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day23.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Grove should', () => {
    it('load', () => {
        let g = new Grove();

        expect(g).not.toBeNull()
    })
    it('load elves', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);

        expect(g.elves.length).toBe(5)
    })
    it('propose new position', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);

        g.Propose()

        expect(g.proposes.length).toBe(5)
    })
    it('propose new position north', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);

        g.Propose()

        expect(g.ProposesAt(2,0)).toBe(1)
    })
    it('propose new position south if north taken', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '...#.',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);

        g.Propose()

        expect(g.ProposesAt(2,3)).toBeGreaterThan(0)
        expect(g.ProposesAt(3,5)).toBeGreaterThan(0)
    })
    it('propose 2 new positions, one north and one south', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);

        g.Propose()

        expect(g.ProposesAt(2,3)).toBe(2)
    })
})
