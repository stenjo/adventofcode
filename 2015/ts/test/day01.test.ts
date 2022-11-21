import {findFloor, part1, part2} from '../src/day01';

describe('Finding correct floor', () => {
    it('Should give 0 for "(())"', () => {
        expect(findFloor("(())")).toBe(0);
    })
    it('Should give 0 for "()()"', () => {
        expect(findFloor("()()")).toBe(0);
    })
    it('Should give 3 for "((("', () => {
        expect(findFloor("(((")).toBe(3);
    })
    it('Should give 3 for "(()(()("', () => {
        expect(findFloor("(()(()(")).toBe(3);
    })
    it('Should give -1 for "())"', () => {
        expect(findFloor("())")).toBe(-1);
    })
    it('Should give -1 for "))("', () => {
        expect(findFloor("))(")).toBe(-1);
    })
    it('Should give -3 for ")))"', () => {
        expect(findFloor(")))")).toBe(-3);
    })
    it('Should give -3 for ")())())"', () => {
        expect(findFloor(")())())")).toBe(-3);
    })
})

describe('Part 1', () => {
    it(`Should give 138 for actual data`, () => {
        expect(part1()).toBe(138);
    })
})
describe('Part 2', () => {
    it(`Should give 1771 for actual data`, () => {
        expect(part2()).toBe(1771);
    })
})