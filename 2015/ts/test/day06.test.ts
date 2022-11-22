import {Lights, Rectangle, Part1, Part2} from "../src/day06";

describe('Probably a fire Hazard', () => {
    it('should have no lights on', () => {
        let l = new Lights(10);

        let numberOfLightsOn = l.On();

        expect(numberOfLightsOn).toBe(0);
    })
    it('should have 1 lights on when set', () => {
        let l = new Lights(10);
        l.TurnOn(new Rectangle(0, 0, 0, 0));

        let numberOfLightsOn = l.On();

        expect(numberOfLightsOn).toBe(1);
    })

    it('should have all lights on when set', () => {
        let l = new Lights(10);
        l.TurnOn(new Rectangle(0, 0, 9, 9));

        let numberOfLightsOn = l.On();

        expect(numberOfLightsOn).toBe(100);
    })

    it('should have 90 lights on when toggle top row', () => {
        let l = new Lights(10);
        l.TurnOn(new Rectangle(0, 0, 9, 9));
        l.Toggle(new Rectangle(0,0,9,0));

        let numberOfLightsOn = l.On();

        expect(numberOfLightsOn).toBe(90);
    })

    it('should have 86 lights on toggled top row and turned 4 off', () => {
        let l = new Lights(10);
        l.TurnOn(new Rectangle(0, 0, 9, 9));
        l.Toggle(new Rectangle(0,0,9,0));
        l.TurnOff(new Rectangle(4,4,5,5));

        let numberOfLightsOn = l.On();

        expect(numberOfLightsOn).toBe(86);
    })

    it('should parse "turn on 0,0 through 9,9"', () => {
        let l = new Lights(10);

        let [cmd, r] = l.ParseLine("turn on 0,0 through 999,999")

        expect(cmd).toBe("on");
        expect(r.x1).toBe(0);
        expect(r.y1).toBe(0);
        expect(r.x2).toBe(999);
        expect(r.y2).toBe(999);

    })

    it('should parse "toggle 0,0 through 999,0"', () => {
        let l = new Lights(10);

        let [cmd, r] = l.ParseLine("toggle 0,0 through 999,0")

        expect(cmd).toBe("toggle");
        expect(r.x1).toBe(0);
        expect(r.y1).toBe(0);
        expect(r.x2).toBe(999);
        expect(r.y2).toBe(0);

    })

    it('should parse "turn off 499,499 through 500,500"', () => {
        let l = new Lights(10);

        let [cmd, r] = l.ParseLine("turn off 499,499 through 500,500")

        expect(cmd).toBe("off");
        expect(r.x1).toBe(499);
        expect(r.y1).toBe(499);
        expect(r.x2).toBe(500);
        expect(r.y2).toBe(500);

    })

    it('should have 86 lights on toggled top row and turned 4 off', () => {
        let l = new Lights(1000);
        l.TurnOn(new Rectangle(0, 0, 0, 0));
        l.Toggle(new Rectangle(0,0,999,999));

        let brightness = l.Brightness();

        expect(brightness).toBe(2000001);
    })

})

describe('Part 1', () => {
    it('should return answer to real data', () => {
        let lights = Part1();
        expect(lights).toBe(400410)
    })
})

describe('Part 2', () => {
    it('should return answer to real data', () => {
        let brightness = Part2();
        expect(brightness).toBe(15343601)
    })
})
