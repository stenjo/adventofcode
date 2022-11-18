import { depthscan, depthsweep } from "../src/2021Day1";

describe("test depthscan", () => {
    test("depthscan", () => {
        expect(depthscan('../test/input/day01.txt')).toBe(7);
    });
})

describe('testing depthsweep', () => {
    test('depthsweep', () => {
        let result = depthsweep('../test/input/day01.txt');

        expect(result).toBe(5)
    })

})