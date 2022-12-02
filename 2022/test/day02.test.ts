import { RPSGame } from '../src/day02';

describe('RPS Game should', () => {
    it('load data', () => {
        let day = new RPSGame('../test/input/day02.txt');

        expect(true).toBe(true)
    })

    it('play with score', () => {
        let g = new RPSGame('../test/input/day02.txt')

        expect(g.Play('A Y')).toBe(8)
        expect(g.Play('A X')).toBe(4)
        expect(g.Play('B Y')).toBe(5)
        expect(g.Play('C Z')).toBe(6)
    })
    it('play with total score', () => {
        let g = new RPSGame('../test/input/day02.txt')

        expect(g.getScore()).toBe(15)
    })

    it('get score for part1', () => {
        let g = new RPSGame('../input/day02.txt')

        expect(g.getScore()).toBe(10404)
    })
    it('play with total strategy score', () => {
        let g = new RPSGame('../test/input/day02.txt')

        expect(g.getStrategyScore()).toBe(12)
    })

    it('get score for part2', () => {
        let g = new RPSGame('../input/day02.txt')

        expect(g.getStrategyScore()).toBe(10334)
    })
})
