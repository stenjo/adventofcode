import { Cave, LoadLines } from '../src/day15'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day15.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Cave should', () => {
    it('deploy sensor', () => {
        let c = new Cave()

        c.Deploy('Sensor at x=2, y=18: closest beacon is at x=-2, y=15')

        expect(c.sensors.length).toBeGreaterThan(0)
        expect(c.beacons.length).toBeGreaterThan(0)
    })
    it('deploy two sensors with same beacon', () => {
        let c = new Cave()

        c.Deploy('Sensor at x=12, y=14: closest beacon is at x=10, y=16')
        c.Deploy('Sensor at x=10, y=20: closest beacon is at x=10, y=16')

        expect(c.sensors.length).toBe(2)
        expect(c.beacons.length).toBe(1)
        expect(c.BeaconAt(10,16)).toBe(true)
    })
    it('deploy all sensors from test input', () => {
        let c = new Cave()
        let input = new LoadLines('../test/input/day15.txt').lines
        
        input.forEach(line => {c.Deploy(line)})

        expect(c.sensors.length).toBe(14)
        expect(c.beacons.length).toBe(6)
        expect(c.BeaconAt(10,16)).toBe(true)
    })
    it('have range calculated for sensor', () => {
        let c = new Cave()
        let input = new LoadLines('../test/input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        expect(c.GetSensorAt(8,7)?.range).toBe(9)
    })

    it('have coverage for one sensor', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=8, y=7: closest beacon is at x=2, y=10')

        expect(c.CoverageAtLine(1)).toBe(7)
        expect(c.CoverageAtLine(-2)).toBe(1)
        expect(c.CoverageAtLine(2)).toBe(9)
        expect(c.CoverageAtLine(7)).toBe(19)
    })
    it('have coverage for one long-range sensor', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=3000768, y=3333983: closest beacon is at x=2564067, y=3163630')

        expect(c.CoverageAtLine(3333983)).toBe(1214109)
    })
    it('have coverage for two sensors', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=8, y=7: closest beacon is at x=2, y=10')
        c.Deploy('Sensor at x=14, y=3: closest beacon is at x=15, y=3')

        expect(c.CoverageAtLine(4)).toBe(13)
        expect(c.CoverageAtLine(2)).toBe(10)
    })

    it('have coverage for two sensors opposite sequences', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=14, y=3: closest beacon is at x=15, y=3')
        c.Deploy('Sensor at x=8, y=7: closest beacon is at x=2, y=10')

        expect(c.CoverageAtLine(4)).toBe(13)
        expect(c.CoverageAtLine(2)).toBe(10)
    })

    it('have coverage for three sensors', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=8, y=7: closest beacon is at x=2, y=10')
        c.Deploy('Sensor at x=14, y=3: closest beacon is at x=15, y=3')
        c.Deploy('Sensor at x=0, y=11: closest beacon is at x=2, y=10')

        expect(c.CoverageAtLine(4)).toBe(13)
        expect(c.CoverageAtLine(2)).toBe(10)
    })

    it('have coverage for four sensors', () => {
        let c = new Cave()
        c.Deploy('Sensor at x=16, y=7: closest beacon is at x=15, y=3')
        c.Deploy('Sensor at x=8, y=7: closest beacon is at x=2, y=10')

        expect(c.CoverageAtLine(7)).toBe(23)
        expect(c.CoverageAtLine(6)).toBe(21)
        expect(c.CoverageAtLine(2)).toBe(10)
        expect(c.CoverageAtLine(12)).toBe(10)
    })

    it.skip('have coverage on line 10', () => {
        let c = new Cave()
        let input = new LoadLines('../test/input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        let coverage = c.CoverageAtLine(10)

        expect(coverage).toBe(26)
        expect(c.CoverageAtLine(9)).toBe(25)
        expect(c.CoverageAtLine(11)).toBe(27)
    })
    it('deploy from real input', () => {
        let c = new Cave()
        let input = new LoadLines('../input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        expect(c.sensors.length).toBeGreaterThan(1)
    })
    it.skip('have coverage on line 2000000 for real data', () => {
        let c = new Cave()
        let input = new LoadLines('../input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        let coverage = c.CoverageAtLine(2000000)

        expect(coverage).toBe(4811413)
    })
    it.skip('have tuning frequency of correct beacon for real data', () => {
        let c = new Cave()
        let input = new LoadLines('../input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        let tuningFreq = c.TuningFreq(2000000)

        expect(tuningFreq).toBe(13171855019123)
    })
})