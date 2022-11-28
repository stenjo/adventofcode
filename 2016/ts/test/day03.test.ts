import {Part1, Part2, Possibles, Triangle} from '../src/day03'

describe('Triangle should', ()=> {
    it('valid triangle for 10, 5, 12', ()=> {
        let t = new Triangle("10 5 12")

        expect(t.valid()).toBe(true)
    })

    it('invalid triangle for 10, 5, 25', ()=> {
        let t = new Triangle("10 5 25")

        expect(t.valid()).toBe(false)
    })
})

describe('Possibles should', () => {
    it('load all lines', () => {
        let p = new Possibles()
        
        expect(p.loadlines().length).toBeGreaterThan(10)
    })
    it('return 1 for 2 lines', () => {
        let p = new Possibles()
        expect(p.countPossibles(["10  5 12", "10  5 25", ""])).toBe(1)
    })
})

describe('Part 1 should', () => {
    it('return correct answer', () => {
        let p1 = new Part1()
        expect(p1.solution()).toBe(862)
    })
})

describe('Part 2 should', () => {
    it('return correct answer', () => {
        let p1 = new Part2()
        expect(p1.solution()).toBe(1577)
    })
})