import { LoadLines, Valve, ValveStructure } from '../src/day16'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day16.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Valve should', ()=>{
    it('be loadable', ()=>{
        let v = new Valve('')

        expect(v).not.toBeNull()
    })

    it('load one valve', () => {
        let v = new Valve('Valve BB has flow rate=13; tunnels lead to valves CC, AA')

        expect(v.id).toBe('BB')
        expect(v.rate).toBe(13)
        expect(v.leads[0]).toBe('CC')
        expect(v.leads[1]).toBe('AA')
    })
    it('open', () => {
        let v = new Valve('Valve BB has flow rate=13; tunnels lead to valves CC, AA')

        v.Open()

        expect(v.open).toBe(true)
    })
    it('give pressure release for 10 minutes when open', () => {
        let v = new Valve('Valve BB has flow rate=13; tunnels lead to valves CC, AA')

        expect(v.open).toBe(false)
        expect(v.PressureRelease(10)).toBe(0)
        v.Open()
        expect(v.PressureRelease(10)).toBe(130)
        expect(v.open).toBe(true)
    })
})

describe('ValveStructure should', () => {
    it('load valves', () => {
        let input = new LoadLines('../test/input/day16.txt').lines.filter(l => l.length > 0)
        let vs = new ValveStructure(input)

        expect(vs.valves.length).toBe(10)
        expect(vs.GetById('AA').children.length).toBe(3)
    })
    it('get pressure release one level', () => {
        let input = new LoadLines('../test/input/day16.txt').lines.filter(l => l.length > 0)
        let vs = new ValveStructure(input)

        let released = vs.GetPressureReleased('BB',10, 1)
        expect(released).toBe(104)
    })
    it('get pressure release two levels', () => {
        let input = new LoadLines('../test/input/day16.txt').lines.filter(l => l.length > 0)
        let vs = new ValveStructure(input)

        let released = vs.GetPressureReleased('AA',10, 2)
        expect(released).toBe(146)
    })
    
    it('get pressure release three levels', () => {
        let input = new LoadLines('../test/input/day16.txt').lines.filter(l => l.length > 0)
        let vs = new ValveStructure(input)

        let released = vs.GetPressureReleased('AA',10, 3)
        expect(released).toBe(154)
    })
})