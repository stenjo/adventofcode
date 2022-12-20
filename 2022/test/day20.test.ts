import { Decryptor, LoadLines } from '../src/day20'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day19.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Decryptor should', () => {
    it('load numbers', () => {
        let nums = new LoadLines('../test/input/day20.txt').lines
        let d = new Decryptor(nums)

        expect(d.numbers.length).toBe(7)
    })
    it('verify numbers', () => {
        let nums = new LoadLines('../test/input/day20.txt').lines
        let d = new Decryptor(nums)

        expect(d.Print()).toBe('1,2,-3,3,-2,0,4')
    })
    it('move number 1', () => {
        let d = new Decryptor('4, 5, 6, 1, 7, 8, 9'.split(', '))

        let result = d.Move(1, d.numbers)

        expect(d.Print(result)).toBe('4,5,6,7,1,8,9')
    })
    it('move number -2 back and wrapping around', () => {
        let d = new Decryptor('4, -2, 5, 6, 7, 8, 9'.split(', '))

        let result = d.Move(-2, d.numbers)

        expect(d.Print(result)).toBe('4,5,6,7,8,-2,9')
    })
    it('4 moves between -3 and 0', () => {
        let d = new Decryptor('1, 2, -3, 0, 3, 4, -2'.split(', '))

        let result = d.Move(4, d.numbers)

        expect(d.Print(result)).toBe('1,2,-3,4,0,3,-2')
    })
    it('-2 moves between 4 and 1', () => {
        let d = new Decryptor('1, 2, -2, -3, 0, 3, 4'.split(', '))

        let result = d.Move(-2, d.numbers)

        expect(d.Print(result)).toBe('1,2,-3,0,3,4,-2')
    })
    it('0 does not move', () => {
        let d = new Decryptor('1, 2, -3, 0, 3, 4, -2'.split(', '))

        let result = d.Move(0, d.numbers)

        expect(d.Print(result)).toBe('1,2,-3,0,3,4,-2')
    })
    it('8 moves between 1 and 2', () => {
        let d = new Decryptor('1, 2, -3, 0, 3, 4, 8'.split(', '))

        let result = d.Move(8, d.numbers)

        expect(d.Print(result)).toBe('1,8,2,-3,0,3,4')
    })
    it('7 does not move', () => {
        let d = new Decryptor('1, 2, -3, 7, 3, 4, -2'.split(', '))

        let result = d.Move(7, d.numbers)

        expect(d.Print(result)).toBe('1,2,-3,7,3,4,-2')
    })
    it('mix numbers', () => {
        let nums = new LoadLines('../test/input/day20.txt').lines
        let d = new Decryptor(nums)

        d.Mix()

        expect(d.Print()).toBe('1,2,-3,4,0,3,-2')
        expect(d.NumAt(1000)).toBe(4)
        expect(d.NumAt(2000)).toBe(-3)
        expect(d.NumAt(3000)).toBe(2)
        expect(d.GroveCoordinateSum()).toBe(3)
    })
    it('give coordinates for real data', () => {
        let nums = new LoadLines('../input/day20.txt').lines
        let d = new Decryptor(nums)

        d.Mix()

        expect(d.GroveCoordinateSum()).toBe(17490)
    })
})