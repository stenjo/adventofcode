import {LoadLines, Pos, RopeModel} from '../src/day09'

describe('Loadlines should', () => {
    it('have test running', () => {
        expect(true).toBe(true)
    })

    it('load from file', () => {
        let f = new LoadLines('../input/day01.txt');

        expect(f).not.toBeNull()
        expect(f.lines.length).toBeGreaterThan(0)
    })
})

describe('Pos should', () => {
    it('initialise to start', () => {
        let p = new Pos(0,0)

        expect(p.x).toBe(0)
        expect(p.y).toBe(0)
    })
})

describe('RopeModel should', () => {
    it('initialise to start for head and tail', () => {
        let r = new RopeModel()

        expect(r.head.x).toBe(0)
        expect(r.head.y).toBe(0)
        expect(r.tail.x).toBe(0)
        expect(r.tail.y).toBe(0)
        expect(r.tailLocations.length).toBe(1)
    })
    it('should not move tail when head is one away from tail', () => {
        let r = new RopeModel()
        r.MoveHeadR()

        expect(r.tail.x).toBe(0)
        expect(r.tailLocations.length).toBe(1)
    })
    it('should move tail one position when head is two away from tail', () => {
        let r = new RopeModel()
        r.MoveHeadR()
        r.MoveHeadR()

        expect(r.tail.x).toBe(1)
    })
})