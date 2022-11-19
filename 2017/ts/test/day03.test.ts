// --- Day 3: Spiral Memory ---
// Tests

import {getXYOfSquare, manhattan} from '../src/day03'

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
        expect(getXYOfSquare(1)).toStrictEqual({"x":0,"y":0});
    })
    it('should return 1,0 for 2', () => {
        expect(getXYOfSquare(2)).toStrictEqual({"x":1,"y":0});
    })
    it('should return 1,1 for 3', () => {
        expect(getXYOfSquare(3)).toStrictEqual({"x":1,"y":1});
    })
    it('should return 0,1 for 4', () => {
        expect(getXYOfSquare(4)).toStrictEqual({"x":0,"y":1});
    })
    it('should return -1,1 for 5', () => {
        expect(getXYOfSquare(5)).toStrictEqual({"x":-1,"y":1});
    })
    it('should return -1,0 for 6', () => {
        expect(getXYOfSquare(6)).toStrictEqual({"x":-1,"y":0});
    })
    it('should return -1,-1 for 7', () => {
        expect(getXYOfSquare(7)).toStrictEqual({"x":-1,"y":-1});
    })
    it('should return 0,-1 for 8', () => {
        expect(getXYOfSquare(8)).toStrictEqual({"x":0,"y":-1});
    })
    it('should return 1,-1 for 9', () => {
        expect(getXYOfSquare(9)).toStrictEqual({"x":1,"y":-1});
    })
    it('should return 2,-1 for 10', () => {
        expect(getXYOfSquare(10)).toStrictEqual({"x":2,"y":-1});
    })
    it('should return 2,0 for 11', () => {
        expect(getXYOfSquare(11)).toStrictEqual({"x":2,"y":0});
    })
    it('should return 2,1 for 12', () => {
        expect(getXYOfSquare(12)).toStrictEqual({"x":2,"y":1});
    })
})