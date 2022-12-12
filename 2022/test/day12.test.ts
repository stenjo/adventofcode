import {ElevationMap, LoadLines} from '../src/day12'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day12.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('ElevationMap should', () => {
    it('load map from file', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        expect(e.map.length).toBeGreaterThan(0)
    })
    it('find start and end in map', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        expect(e.start).not.toBeNull()
        expect(e.end).not.toBeNull()
    })
    it('find start and end in map for real data', () => {
        let l = new LoadLines('../input/day12.txt').lines
        let e = new ElevationMap(l)

        expect(e.start).not.toBeNull()
        expect(e.end).not.toBeNull()
    })
    it('move position to next', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.Move()

        expect(e.current.elev).toBe('a')
        expect(e.current.steps).toBe(1)
    })
    it('move 2 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.Move()
        e.Move()

        expect(e.current.elev).toBe('b')
        expect(e.current.steps).toBe(2)
    })
    it('move 3 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.Move()
        e.Move()
        e.Move()

        expect(e.current.elev).toBe('c')
        expect(e.current.steps).toBe(3)
    })
    it('find path to E', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        let i = 0
        while (!e.current.isAt(e.end.x, e.end.y) && i < 1000) {
            e.Move()
            i++
        }
        expect(e.current.elev).toBe('z')
        expect(e.current.steps).toBe(31)
    })
    
})
