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
        this.crt.DrawPixel(this.regX)
    }
    regX: number;
    cycles: number;
    signalStrength: SignalStrength[];
    crt: Crt;

    constructor() {
        this.regX = 1;
        this.cycles = 0;
        this.signalStrength = []
        this.crt = new Crt();
    }
}

export class Crt {
    DrawPixel(spritePos:number) {
        this.spritePos = spritePos
        if (this.isWithinSprite()) {
            this.screen += '#'
        } else {
            this.screen += '.'
        }
        this.pixelPos ++

    }
    screen: string;
    spritePos: number;
    pixelPos: number;
    constructor() {
        this.screen = ''
        this.spritePos = 1
        this.pixelPos = 0
    }

    private isWithinSprite() {
        return this.pixelPos % 40 <= this.spritePos + 1 && this.pixelPos % 40 >= this.spritePos - 1;
    }
}
  
