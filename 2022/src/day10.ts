// --- Day 10: Cathode-Ray Tube ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n')
        .map(line => line.trim());
    }
  }

  class SignalStrength{
    cycle: number;
    level: number;
    x: number;
    inst: string;

    constructor(cycle: number, x: number, inst = "") {
        this.cycle = cycle;
        this.level = x * cycle;
        this.x = x;
        this.inst = inst;

    }
  }

  export class Cpu {
    SignalStrength(cycle: number): number {
        let result = this.signalStrength.find((c)=> { return cycle === c.cycle; });
        if (result === undefined) {
            return 0;
        }
        return result.level
    }
    RunProgram(instructions: string[]) {
        instructions.forEach(line => this.Run(line));
    }
    Run(instruction: string) {
        const [inst, arg] = instruction.split(' ');
        if (inst === 'addx') {
            this.cycles ++
            this.UpdateSignal('v')
            this.cycles ++
            this.UpdateSignal(instruction)
            this.regX += parseInt(arg)

            return
        }
        if (inst === 'noop') {
            this.cycles ++
            this.UpdateSignal('noop')
        }
    }
    UpdateSignal(inst = '') {
        if (this.cycles % 20 === 0 
            || (this.cycles < 10 && this.cycles > 0)
            ) {
            this.signalStrength.push(new SignalStrength(this.cycles, this.regX, inst))
        }
    }
    regX: number;
    cycles: number;
    signalStrength: SignalStrength[];

    constructor() {
        this.regX = 1;
        this.cycles = 0;
        this.signalStrength = []
    }
}

export class Crt {
    DrawPixel(spritePos = this.spritePos) {
        this.spritePos = spritePos
        if (this.screen.length < 1) {
            this.screen.push('#')
            this.pixelPos ++
            return
        }
        if (this.pixelPos <= this.spritePos + 1 && this.pixelPos >= this.spritePos - 1) {
            this.screen[0] += '#'
            this.pixelPos ++
            return
        }
        this.screen[0] += '.'
        this.pixelPos ++

    }
    screen: string[];
    spritePos: number;
    pixelPos: number;
    constructor() {
        this.screen = []
        this.spritePos = 1
        this.pixelPos = 0
    }
}
  
