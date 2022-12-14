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

        e.VisitPoint(e.start)
        let p = e.getAt(0,1)

        expect(p?.elev).toBe('a')
        expect(p?.steps).toBe(1)
    })
    it('move 2 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(1,1)

        expect(p?.elev).toBe('b')
        expect(p?.steps).toBe(2)
    })
    it('move 3 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(1,2)


        expect(p?.elev).toBe('c')
        expect(p?.steps).toBe(3)
    })
    it('move 4 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(2,2)


        expect(p?.elev).toBe('c')
        expect(p?.steps).toBe(4)
    })
    it('move 5 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(2,3)


        expect(p?.elev).toBe('c')
        expect(p?.steps).toBe(5)
    })
    it('move 6 positions', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(2,4)


        expect(p?.elev).toBe('d')
        expect(p?.steps).toBe(6)
    })
    it('find path to E', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(e.end.x, e.end.y)

        expect(p?.elev).toBe('z')
        expect(p?.steps).toBe(31)
    })
    
    it.skip('find path to E for real data', () => {
        let l = new LoadLines('../input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.start)
        let p = e.getAt(e.end.x, e.end.y)

        expect(p?.elev).toBe('E')
        expect(p?.steps).toBe(412)
    })
    it.only('find shortest path to a', () => {
        let l = new LoadLines('../test/input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.end)
        let p = e.GetLowestSteps('a')

        e.PrintVisits()
        expect(p?.elev).toBe('a')
        expect(p?.steps).toBe(29)
    })
    it.skip('find shortest path to a for real data', () => {
        let l = new LoadLines('../input/day12.txt').lines
        let e = new ElevationMap(l)

        e.VisitPoint(e.end)
        let p = e.GetLowestSteps('a')

        expect(p?.elev).toBe('a')
        expect(p?.steps).toBe(402)
    })
})
