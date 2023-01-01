import { CaloriesCounter } from "../src/day01";


describe("CaloriesCounter should", () => {
    it('load lines', () => {
        let s = new CaloriesCounter('../test/input/day01.txt');

        expect(s.GetElves()).toBe(5);
    })

    it('should return higest calories', () => {
        let s = new CaloriesCounter('../test/input/day01.txt');

        expect(s.GetMaxCalories()).toBe(24000)
    })

    it('should return correct answer for Part1', () => {
        let s = new CaloriesCounter('../input/day01.txt')

        expect(s.GetMaxCalories()).toBe(67016)
    })

    it('should return top 3 calories', () => {
        let s = new CaloriesCounter('../test/input/day01.txt');

        expect(s.GetTop3Calories()).toBe(45000)
    })


    it('should return correct answer for Part2', () => {
        let s = new CaloriesCounter('../input/day01.txt')

        expect(s.GetTop3Calories()).toBe(200116)
    })


})
