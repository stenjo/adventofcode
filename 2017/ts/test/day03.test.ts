// --- Day 3: Spiral Memory ---
// Tests

import {getXYOfNumber, manhattan} from '../src/day03'

describe('Manhattan Distance', () => {
    it('should give 5 for 3,2', () => {
        let result = manhattan(3,2);

        expect(result).toEqual(5);
    })
    it('should give 7 for -3,4', () => {
        let result = manhattan(-3,4);

        expect(result).toEqual(7);
    })
    it('should give 5 for -3,-2', () => {
        let result = manhattan(-3,-2);

        expect(result).toEqual(5);
    })
})

describe('Get XY from square', () => {

    it('should return 0,0 for 1', () => {
        expect(getXYOfNumber(1)).toStrictEqual({"x":0,"y":0});
    })
    it('should return 1,0 for 2', () => {
        expect(getXYOfNumber(2)).toStrictEqual({"x":1,"y":0});
    })
    it('should return 1,1 for 3', () => {
        expect(getXYOfNumber(3)).toStrictEqual({"x":1,"y":1});
    })
})