import { Cube, LoadLines, Scanner } from '../src/day18'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day18.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Cube should', () => {
    it('be created', () => {
        let c = new Cube(1,2,3)

        expect(c).not.toBeNull()
    })
})

describe('Scanner should', () => {
    it('be created', () => {
        let s = new Scanner()

        expect(s).not.toBeNull()

    })
    it('load cubes', () => {
        let s = new Scanner()
        let lines = new LoadLines('../test/input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.cubes.length).toBe(13)

    })
    it('get exposed sides of one cube', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(6)
    })
    it('get exposed sides of two adjasing cubes', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '2,1,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(10)
    })
    it('get exposed sides of two non-adjasing cubes', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '3,1,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(12)
    })
    it('get exposed sides of three adjasing cubes', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '2,1,1',
            '2,2,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(14)
    })
    it('get exposed sides of three adjasing cubes in different order', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '2,2,1',
            '2,1,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(14)
    })
    it('get exposed sides of four adjasing cubes in different order', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '2,2,1',
            '2,1,1',
            '1,2,1'
        ]
        s.LoadCubes(cubes)

        expect(s.ExposedSides()).toBe(16)
    })
    it('get exposed sides for test data', () => {
        let s = new Scanner()
        let lines = new LoadLines('../test/input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.ExposedSides()).toBe(64)

    })
    it('get exposed sides for real data', () => {
        let s = new Scanner()
        let lines = new LoadLines('../input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.ExposedSides()).toBe(4504)

    })
    it('get air pockets cubes given max and min cubes', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '1,4,1'
        ]
        s.LoadCubes(cubes)

        expect(s.GapCubes().length).toBe(0)
    })
    it('get air pocket cubes in 3 directions', () => {
        let s = new Scanner()
        const cubes = [
            '1,1,1',
            '2,1,1',
            '3,1,1',
            '1,2,1',
            '2,2,1',
            '3,2,1',
            '1,3,1',
            '2,3,1',
            '3,3,1',
            '1,1,2',
            '2,1,2',
            '3,1,2',
            '1,2,2',
            '3,2,2',
            '1,3,2',
            '2,3,2',
            '3,3,2',
            '1,1,3',
            '2,1,3',
            '3,1,3',
            '1,2,3',
            '2,2,3',
            '3,2,3',
            '1,3,3',
            '2,3,3',
            '3,3,3',
            '1,1,3',
            '2,1,3',
            '3,1,3',
            '1,2,3',
            '2,2,3',
            '3,2,3',
            '1,3,3',
            '2,3,3',
            '3,3,3'
        ]
        s.LoadCubes(cubes)

        expect(s.GapCubes().length).toBe(1)
    })
    it('get exposed sides of four adjasing cubes in different order', () => {
        let s = new Scanner()
        let lines = new LoadLines('../test/input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.GapCubes().length).toBe(1)
    })
    it('get externally exposed sides for test data', () => {
        let s = new Scanner()
        let lines = new LoadLines('../test/input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.ExternalExposedSides()).toBe(58)

    })
    it.skip('get externally exposed sides for real data', () => {
        let s = new Scanner()
        let lines = new LoadLines('../input/day18.txt').lines

        s.LoadCubes(lines)

        expect(s.ExternalExposedSides()).toBe(2556)

    })
    it('print map', () => {
        let s = new Scanner()
        let lines = new LoadLines('../test/input/day18.txt').lines

        s.LoadCubes(lines)

        console.log(s.PrintMap(s.ObsidianMap()))

    })
})