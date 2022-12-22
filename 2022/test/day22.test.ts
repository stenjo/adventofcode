import { LoadLines, MonkeyMap} from '../src/day22'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day22.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('MonkeyMap should', () => {
    it('load map', () => {

        let lines = new LoadLines('../test/input/day22.txt').lines
        let mp = new MonkeyMap(lines)

        expect(mp.map.length).toBe(12)
    })
    
    it('get starting position', () => {
        let lines = new LoadLines('../test/input/day22.txt').lines
        let mp = new MonkeyMap(lines)

        expect(mp.row).toBe(1)
        expect(mp.column).toBe(9)
        expect(mp.facing).toBe(0)

    })

    it('move left hitting wall and stop', () => {
        let lines = new LoadLines('../test/input/day22.txt').lines
        let mp = new MonkeyMap(lines)

        mp.Move(10,'R')

        expect(mp.row).toBe(1)
        expect(mp.column).toBe(11)
        expect(mp.facing).toBe(1)

    })
})