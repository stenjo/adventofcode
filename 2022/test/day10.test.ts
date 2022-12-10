import {Cpu, Crt, LoadLines} from '../src/day10'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day10.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('CPU should', () => {
    it('start with X = 1', () => {
        let cpu = new Cpu();

        expect(cpu.regX).toBe(1)
    })

    it('have run one cycle from executing noop', () => {
        let cpu = new Cpu();

        cpu.Run('noop')

        expect(cpu.regX).toBe(1)
        expect(cpu.cycles).toBe(1)
    })
    it('have run three cycles from executing noop and addx 3', () => {
        let cpu = new Cpu();

        cpu.Run('noop')
        cpu.Run('addx 3')

        expect(cpu.regX).toBe(4)
        expect(cpu.cycles).toBe(3)
    })
    it('have run five cycles from executing noop, addx 3 and addx -5', () => {
        let cpu = new Cpu();

        cpu.Run('noop')
        cpu.Run('addx 3')
        cpu.Run('addx -5')

        expect(cpu.regX).toBe(-1)
        expect(cpu.cycles).toBe(5)
    })
    it('have run five cycles wiwth correct signals', () => {
        let cpu = new Cpu();

        cpu.Run('noop')
        cpu.Run('addx 3')
        cpu.Run('addx -5')

        expect(cpu.regX).toBe(-1)
        expect(cpu.cycles).toBe(5)
        expect(cpu.SignalStrength(1)).toBe(1)
        expect(cpu.SignalStrength(2)).toBe(2)
        expect(cpu.SignalStrength(3)).toBe(3)
        expect(cpu.SignalStrength(4)).toBe(16)
        expect(cpu.SignalStrength(5)).toBe(20)

    })
    it('have 420 as signal strength at cycle 20', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(20)).toBe(420)
    })
    it('have 420 as signal strength at cycle 20', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(20)).toBe(420)
    })

    it('have 1140 as signal strength at cycle 60', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(60)).toBe(1140)
    })
    it('have 1800 as signal strength at cycle 100', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(100)).toBe(1800)
    })
    it('have 2940 as signal strength at cycle 140', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(140)).toBe(2940)
    })
    it('have 2880 as signal strength at cycle 180', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)
        // console.log(cpu.signalStrength)
        expect(cpu.SignalStrength(180)).toBe(2880)
    })
    it('have 3960 as signal strength at cycle 220', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.SignalStrength(220)).toBe(3960)
    })
    it('have sum of selected signal strengths to be 13140', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)
        let sum = cpu.SignalStrength(20) 
        + cpu.SignalStrength(60)
        + cpu.SignalStrength(100)
        + cpu.SignalStrength(140)
        + cpu.SignalStrength(180)
        + cpu.SignalStrength(220)

        expect(sum).toBe(13140)
    })
    it('have sum of selected signal strengths of real input', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../input/day10.txt').lines

        cpu.RunProgram(instructions)
        let sum = cpu.SignalStrength(20) 
        + cpu.SignalStrength(60)
        + cpu.SignalStrength(100)
        + cpu.SignalStrength(140)
        + cpu.SignalStrength(180)
        + cpu.SignalStrength(220)

        expect(sum).toBe(14320)
    })

    it('draw image', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)

        expect(cpu.crt.screen).toContain('##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.')
    })
    it('draw image and have correct last line', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../test/input/day10.txt').lines

        cpu.RunProgram(instructions)
        console.log(cpu.crt.screen)
        const regex = new RegExp(`.{1,40}`, 'g');
        let crtLines = cpu.crt.screen.match(regex) as string[];

        console.log(crtLines)

        expect(cpu.crt.screen).toContain('##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.')
        expect(crtLines[5]).toContain('#######.......#######.......#######.....')
    })    
    it('draw image from real data', () => {
        let cpu = new Cpu();
        let instructions = new LoadLines('../input/day10.txt').lines

        cpu.RunProgram(instructions)
        const regex = new RegExp(`.{1,40}`, 'g');
        let crtLines = cpu.crt.screen.match(regex) as string[];

        console.log(crtLines)

        // PCPBKAPJ
        expect(crtLines[5]).toBe('#.....##..#....###..#..#.#..#.#.....##..')
    })

})

describe('CRT should', () => {
    it('be initalized', () => {
        let crt = new Crt()

        expect(crt.spritePos).toBe(1)
    })
    it('draw # on first cycle', () => {
        let crt = new Crt()

        crt.DrawPixel(1)

        expect(crt.pixelPos).toBe(1)
        expect(crt.screen).toContain('#')
    })
    it('draw ## on second cycle', () => {
        let crt = new Crt()

        crt.DrawPixel(1)
        crt.DrawPixel(1)

        expect(crt.pixelPos).toBe(2)
        expect(crt.screen).toContain('##')
    })
    it('draw ##. on third cycle', () => {
        let crt = new Crt()

        crt.DrawPixel(1)
        crt.DrawPixel(1)
        crt.DrawPixel(16)

        expect(crt.pixelPos).toBe(3)
        expect(crt.screen).toContain('##.')
    })
    it('draw ##.. on fourth cycle', () => {
        let crt = new Crt()

        crt.DrawPixel(1)
        crt.DrawPixel(1)
        crt.DrawPixel(16)
        crt.DrawPixel(16)

        expect(crt.pixelPos).toBe(4)
        expect(crt.screen).toContain('##..')
    })
})