import {LoadLines, Monkey, MonkeyYeller } from '../src/day21'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day21.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Monkey should', () => {
    it('load config', () => {
        let m = new Monkey('root: pppw + sjmn')

        expect(m.Left()).toBe('pppw')
        expect(m.Right()).toBe('sjmn')
        expect(m.Name()).toBe('root')
        expect(m.Op()).toBe('+')
    })
    it('load config of number only', () => {
        let m = new Monkey('dbpl: 5')

        expect(m.Left()).toBe(5)
        expect(m.Name()).toBe('dbpl')
    })
})

describe('MonkeyYeller should', () => {
    it('load list of monkey configs', () => {

        let configs = new LoadLines('../test/input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.monkeys.length).toBe(15)
    })
    it('get yell from single monkey', () => {

        let configs = new LoadLines('../test/input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.Monkey('hmdt').Yell()).toBe(32)
    })
    it('get yell from monkey with two children', () => {

        let configs = new LoadLines('../test/input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.Monkey('drzm').Yell()).toBe(30)
    })
    it('get yell from monkey with multiply and uneven children tree', () => {

        let configs = new LoadLines('../test/input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.Monkey('sjmn').Yell()).toBe(150)
    })
    it('get yell from root', () => {

        let configs = new LoadLines('../test/input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.Monkey('root').Yell()).toBe(152)
    })
    it('get yell from root from live data', () => {

        let configs = new LoadLines('../input/day21.txt').lines
        let my = new MonkeyYeller(configs)

        expect(my.Monkey('root').Yell()).toBe(379578518396784)
    })
})