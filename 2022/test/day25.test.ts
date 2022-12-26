import { LoadLines, Snafu} from '../src/day25'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day25.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Snafu should', () => {
    it('load', () =>{
        let s = new Snafu()

        expect(s).not.toBeNull()
    })

    it('convert 1 to 1', () =>{
        let s = new Snafu()

        expect(s.toNum('1')).toBe(1)
    })
    it('convert 1 to snafu 1', () =>{
        let s = new Snafu()

        expect(s.toSnafu(1)).toBe('1')
    })
    it('convert 2 to 2', () =>{
        let s = new Snafu()

        expect(s.toNum('2')).toBe(2)
    })
    it('convert 2 to snafu 2', () =>{
        let s = new Snafu()

        expect(s.toSnafu(2)).toBe('2')
    })
    it('convert 1= to 3', () =>{
        let s = new Snafu()

        expect(s.toNum('1=')).toBe(3)
    })
    it('convert 3 to snafu 1=', () =>{
        let s = new Snafu()

        expect(s.toSnafu(3)).toBe('1=')
    })
    it('convert 1- to 4', () =>{
        let s = new Snafu()

        expect(s.toNum('1-')).toBe(4)
    })
    it('convert 4 to snafu 1-', () =>{
        let s = new Snafu()

        expect(s.toSnafu(4)).toBe('1-')
    })
    it('convert 10 to 5', () =>{
        let s = new Snafu()

        expect(s.toNum('10')).toBe(5)
    })
    it('convert 5 to snafu 10', () =>{
        let s = new Snafu()

        expect(s.toSnafu(5)).toBe('10')
    })

})