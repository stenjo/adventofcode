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

        expect(c.mountain.length).toBeGreaterThan(0)
    })
    it('draw one vertical line of rock', () => {
        let c = new Cave(['498,4 -> 498,6'])

        expect(c.mountain.length).toBe(3)
        expect(c.RockAt(498,5)).toBe(true)
    })
    it('draw one horisontal line of rock', () => {
        let c = new Cave(['498,6 -> 496,6'])

        expect(c.mountain.length).toBe(3)
        expect(c.RockAt(497,6)).toBe(true)
    })
    it('draw two lines of rock', () => {
        let c = new Cave(['498,4 -> 498,6 -> 496,6'])

        expect(c.mountain.length).toBe(5)
        expect(c.RockAt(498,5)).toBe(true)
        expect(c.RockAt(497,6)).toBe(true)
    })
    it('draw test structures', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        expect(c.mountain.length).toBe(20)
        expect(c.RockAt(498,5)).toBe(true)
        expect(c.RockAt(497,6)).toBe(true)
        expect(c.RockAt(502,9)).toBe(true)
    })
    it('draw structures on screen', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)
        let scr = c.PrintCave()

        expect(scr.length).toBeGreaterThan(9)
    })
    it('draw real structures on screen', () => {
        let input = new LoadLines('../input/day14.txt').lines
        let c = new Cave(input)
        let scr = c.PrintCave()

        expect(scr.length).toBeGreaterThan(9)
    })
    it('drop sand until rest', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        c.DropSand()
        
        expect(c.SandResting()).toBe(1)
    })
    it('drop two sand until rest', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        c.DropSand()
        c.DropSand()

        expect(c.SandResting()).toBe(2)
        expect(c.SandAt(499,8)).toBe(true)
    })
    it('drop three sand until rest', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        c.DropSand()
        c.DropSand()
        c.DropSand()
        
        // console.log(c.PrintCave())
        expect(c.SandResting()).toBe(3)
        expect(c.SandAt(499,8)).toBe(true)
        expect(c.SandAt(501,8)).toBe(true)
    })
    it('drop sand until overflow', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        c.DropUntilOverflow()
        
        expect(c.SandResting()).toBe(24)
        expect(c.SandAt(499,8)).toBe(true)
        expect(c.SandAt(501,8)).toBe(true)
    })
    it('drop sand until overflow for real data', () => {
        let input = new LoadLines('../input/day14.txt').lines
        let c = new Cave(input)

        c.DropUntilOverflow()
        
        expect(c.SandResting()).toBe(964)
    })
    it('drop sand until overflow', () => {
        let input = new LoadLines('../test/input/day14.txt').lines
        let c = new Cave(input)

        c.DropUntilTop()
        
        expect(c.SandResting()).toBe(24)
        expect(c.SandAt(499,8)).toBe(true)
        expect(c.SandAt(501,8)).toBe(true)
    })
})