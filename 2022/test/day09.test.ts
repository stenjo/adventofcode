import {LoadLines, RopeModel} from '../src/day09'

describe('RopeModel should', () => {
    it('have tail not moving when head moves one away right', () => {
        let r = new RopeModel();

        r.MoveR()

        expect(r.tail.x).toBe(0);
        expect(r.tail.y).toBe(0)
    })
    it('have tail move one righ when head is two away right', () => {
        let r = new RopeModel();

        r.MoveR()
        r.MoveR()

        expect(r.tail.x).toBe(1);
        expect(r.tail.y).toBe(0)
        expect(r.GetTailVisits()).toBe(2)
    })
    it('have tail move one left when head is two away left', () => {
        let r = new RopeModel();

        r.MoveL()
        r.MoveL()

        expect(r.tail.x).toBe(-1);
        expect(r.tail.y).toBe(0)
        expect(r.GetTailVisits()).toBe(2)
    })
    it('have tail move one up when head is two away up', () => {
        let r = new RopeModel();

        r.MoveU()
        r.MoveU()

        expect(r.tail.x).toBe(0);
        expect(r.tail.y).toBe(1)
        expect(r.GetTailVisits()).toBe(2)
    })
    it('have tail move one down when head is two away down', () => {
        let r = new RopeModel();

        r.MoveD()
        r.MoveD()

        expect(r.tail.x).toBe(0);
        expect(r.tail.y).toBe(-1)
        expect(r.GetTailVisits()).toBe(2)
    })
    it('have tail not move when head is diagonally right and up', () => {
        let r = new RopeModel();

        r.MoveR()
        r.MoveU()

        expect(r.tail.x).toBe(0);
        expect(r.tail.y).toBe(0)
        expect(r.GetTailVisits()).toBe(1)
    })
    it('have tail move when head is diagonally right and two up', () => {
        let r = new RopeModel();

        r.MoveR()
        r.MoveU()
        r.MoveU()

        expect(r.tail.x).toBe(1);
        expect(r.tail.y).toBe(1)
        expect(r.GetTailVisits()).toBe(2)
    })

    it('RunInstruction right 4 spaces', () => {
        let r = new RopeModel();

        r.RunInstruction('R 4')

        expect(r.tail.x).toBe(3)
        expect(r.GetTailVisits()).toBe(4)
    })
    it('RunInstruction right 4 then up 4 spaces', () => {
        let r = new RopeModel();

        r.RunInstruction('R 4')
        r.RunInstruction('U 4')

        expect(r.tail.x).toBe(4)
        expect(r.tail.y).toBe(3)
        expect(r.GetTailVisits()).toBe(7)
    })
    it('produce correct result for test input', () => {
        let r = new RopeModel();
        let instr = new LoadLines('../test/input/day09.txt').lines

        instr.forEach(line => {
            r.RunInstruction(line)
        })

        expect(r.GetTailVisits()).toBe(13)
    })
    it('produce correct result for real input', () => {
        let r = new RopeModel();
        let instr = new LoadLines('../input/day09.txt').lines

        instr.forEach(line => {
            r.RunInstruction(line)
        })

        expect(r.GetTailVisits()).toBe(6339)
    })
})