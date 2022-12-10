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

    constructor(cycle: number, x: number) {
        this.cycle = cycle;
        this.level = x * cycle;
        this.x = x;
    }
  }

  export class Cpu {
    SignalStrength(cycle: number): number {
        let result = this.signalStrength.find(c => cycle === c.cycle);
        return result ? result.level : 0;
    }
    RunProgram(instructions: string[]) {
        instructions.forEach(line => this.Run(line));
    }
    Run(instruction: string) {
        const [inst, arg] = instruction.split(' ');
        this.cycles ++
        this.UpdateSignal()
        if (inst === 'addx') {
            this.cycles ++
            this.UpdateSignal()
            this.regX += parseInt(arg)

            return
        }
    }
    UpdateSignal() {
        if (this.cycles % 20 === 0 
            || (this.cycles < 10 && this.cycles > 0)
            ) {
            this.signalStrength.push(new SignalStrength(this.cycles, this.regX))
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

    PrintScreen() {
        const regex = new RegExp(`.{1,40}`, 'g');
        let crtLines = this.screen.match(regex) as string[];
        console.log(crtLines.join('\n'));
    }

    private isWithinSprite() {
        return this.pixelPos % 40 <= this.spritePos + 1 && this.pixelPos % 40 >= this.spritePos - 1;
    }
}
  
