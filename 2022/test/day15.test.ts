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

        expect(c.SensorAt(8,7)?.range).toBe(9)
    })

    it('have coverage on line 10', () => {
        let c = new Cave()
        let input = new LoadLines('../test/input/day15.txt').lines
        input.forEach(line => {c.Deploy(line)})

        let coverage = c.CoverageAtLine(10)

        expect(coverage).toBe(26)
    })
})