// --- Day 3: Spiral Memory ---
// Tests

import {getSqaresInCircle, getSteps, getXYOfSquare, manhattan} from '../src/day03'

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
    it('should return 2,2 for 13', () => {
        expect(getXYOfSquare(13)).toStrictEqual({"x":2,"y":2});
    })
    it('should return 1,2 for 14', () => {
        expect(getXYOfSquare(14)).toStrictEqual({"x":1,"y":2});
    })
    it('should return 0,2 for 15', () => {
        expect(getXYOfSquare(15)).toStrictEqual({"x":0,"y":2});
    })
    it('should return -1,2 for 16', () => {
        expect(getXYOfSquare(16)).toStrictEqual({"x":-1,"y":2});
    })
    it('should return -2,2 for 17', () => {
        expect(getXYOfSquare(17)).toStrictEqual({"x":-2,"y":2});
    })
    it('should return -2,1 for 18', () => {
        expect(getXYOfSquare(18)).toStrictEqual({"x":-2,"y":1});
    })
    it('should return -2,0 for 19', () => {
        expect(getXYOfSquare(19)).toStrictEqual({"x":-2,"y":0});
    })
    it('should return -2,-1 for 20', () => {
        expect(getXYOfSquare(20)).toStrictEqual({"x":-2,"y":-1});
    })
    it('should return -2,-2 for 21', () => {
        expect(getXYOfSquare(21)).toStrictEqual({"x":-2,"y":-2});
    })
    it('should return -1,-2 for 22', () => {
        expect(getXYOfSquare(22)).toStrictEqual({"x":-1,"y":-2});
    })
    it('should return 0,-2 for 23', () => {
        expect(getXYOfSquare(23)).toStrictEqual({"x":0,"y":-2});
    })
    it('should return 1,-2 for 24', () => {
        expect(getXYOfSquare(24)).toStrictEqual({"x":1,"y":-2});
    })
})

describe('Get steps', () => {
    it('should return 0 for square 1', () => {
        expect(getSteps(1)).toBe(0);
    })
    it('should return 3 for square 12', () => {
        expect(getSteps(12)).toBe(3);
    })
    it('should return 2 for square 23', () => {
        expect(getSteps(23)).toBe(2);
    })
    it('should return 31 for square 1024', () => {
        expect(getSteps(1024)).toBe(31);
    })
    it('should return 369 for square 368078', () => {
        expect(getSteps(368078)).toBe(371);
    })

})

describe('Get number of squares in circle given circle number', () => {
    it('should return 1 for circle 1', () => {
        expect(getSqaresInCircle(1)).toBe(1);
    })
    it('should return 8 for circle 2', () => {
        expect(getSqaresInCircle(2)).toBe(8);
    })
    it('should return 16 for circle 3', () => {
        expect(getSqaresInCircle(3)).toBe(16);
    })
    it('should return 24 for circle 4', () => {
        expect(getSqaresInCircle(4)).toBe(24);
    })
    it('should return 32 for circle 5', () => {
        expect(getSqaresInCircle(5)).toBe(32);
    })
    it('should return 40 for circle 6', () => {
        expect(getSqaresInCircle(6)).toBe(40);
    })
})

