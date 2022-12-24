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

        expect(g.proposes.length).toBe(4)
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

        // expect(g.ProposesAt(2,3)).toBeGreaterThan(0)
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
    it('move all elves according to propsed', () => {
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
        g.MoveAll()

        expect(g.IsElfAt(2,0)).toBe(true)
        expect(g.IsElfAt(3,0)).toBe(true)
        expect(g.IsElfAt(2,2)).toBe(true)
        expect(g.IsElfAt(3,3)).toBe(true)
        expect(g.IsElfAt(2,4)).toBe(true)
    })
    it('move all elves according to propsed two rounds', () => {
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
        g.MoveAll()
        g.Propose()
        g.MoveAll()

        expect(g.IsElfAt(2,1)).toBe(true)
        expect(g.IsElfAt(3,1)).toBe(true)
        expect(g.IsElfAt(1,2)).toBe(true)
        expect(g.IsElfAt(4,3)).toBe(true)
        expect(g.IsElfAt(2,5)).toBe(true)
    })
    it('move all elves according to propsed three rounds', () => {
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
        g.MoveAll()
        g.Propose()
        g.MoveAll()
        g.Propose()
        g.MoveAll()

        expect(g.IsElfAt(2,0)).toBe(true)
        expect(g.IsElfAt(4,1)).toBe(true)
        expect(g.IsElfAt(0,2)).toBe(true)
        expect(g.IsElfAt(4,3)).toBe(true)
        expect(g.IsElfAt(2,5)).toBe(true)
    })
    it('move all elves according to propsed four rounds', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);
        let moves = 0

        for (let i = 0; i < 4; i++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(moves).toBe(0)
        expect(g.Spaces()).toBe(25)
    })
    it('move all elves according to propsed 10 rounds', () => {
        const elves = [
            '..............',
            '..............',
            '.......#......',
            '.....###.#....',
            '...#...#.#....',
            '....#...##....',
            '...#.###......',
            '...##.#.##....',
            '....#..#......',
            '..............',
            '..............',
            '..............',
        ]
        let g = new Grove(elves);
        let moves = 0

        for (let i = 0; i < 10; i++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(g.Spaces()).toBe(110)
    })
    it('move all elves according to propsed 10 rounds with test data', () => {
        const elves = new LoadLines('../test/input/day23.txt').lines
        let g = new Grove(elves);
        let moves = 0

        for (let i = 0; i < 10; i++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(g.Spaces()).toBe(110)
    })
    it('move all elves according to propsed 10 rounds with live data', () => {
        const elves = new LoadLines('../input/day23.txt').lines
        let g = new Grove(elves);
        let moves = 0

        for (let i = 0; i < 10; i++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(g.Spaces()).toBe(4254)
    })
    it('move all elves according to propsed 10 rounds with test data', () => {
        const elves = [
            '.....',
            '..##.',
            '..#..',
            '.....',
            '..##.',
            '.....'
        ]
        let g = new Grove(elves);
        let moves = 1
        let rounds = 0
        for (rounds = 0; rounds < 1000 && moves != 0; rounds++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(rounds).toBe(4)
        expect(g.Spaces()).toBe(25)
    })
    it('move all elves according to propsed 10 rounds with test data', () => {
        const elves = new LoadLines('../test/input/day23.txt').lines
        let g = new Grove(elves);
        let moves = 1
        let rounds = 0
        for (rounds = 0; rounds < 1000 && moves != 0; rounds++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(rounds).toBe(20)
        // expect(g.Spaces()).toBe(110)
    })
    it.skip('move all elves according to propsed 10 rounds with test data', () => {
        const elves = new LoadLines('../input/day23.txt').lines
        let g = new Grove(elves);
        let moves = 1
        let rounds = 0
        for (rounds = 0; rounds < 10000 && moves != 0; rounds++) {
            g.Propose()
            moves = g.MoveAll()
        }

        expect(rounds).toBe(992)
        // expect(g.Spaces()).toBe(110)
    })
})
