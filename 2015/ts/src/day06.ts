// --- Day 6: Probably a Fire Hazard ---
// Because your neighbors keep defeating you in the holiday house decorating
// contest year after year, you've decided to deploy one million lights in a
// 1000x1000 grid.

// Furthermore, because you've been especially nice this year, Santa has
// mailed you instructions on how to display the ideal lighting configuration.

// Lights in your grid are numbered from 0 to 999 in each direction; the
// lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The
// instructions include whether to turn on, turn off, or toggle various
// inclusive ranges given as coordinate pairs. Each coordinate pair represents
// opposite corners of a rectangle, inclusive; a coordinate pair like
// 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights
// all start turned off.

// To defeat your neighbors this year, all you have to do is set up your
// lights by doing the instructions Santa sent you in order.

// For example:

// turn on 0,0 through 999,999 would turn on (or leave on) every light.
// toggle 0,0 through 999,0 would toggle the first line of 1000 lights,
// turning off the ones that were on, and turning on the ones that were
// off.
// turn off 499,499 through 500,500 would turn off (or leave off) the
// middle four lights.
// After following the instructions, how many lights are lit?

class Light {
    x:number = 0;
    y:number = 0;
    light:boolean = false;
    brightness:number = 0;
    constructor(x:number, y:number) {
        this.x = x;
        this.y = y;
    }
}

class Rectangle {
    x1: number = 0;
    y1: number = 0;
    x2: number = 0;
    y2: number = 0;

    constructor(x1: number, y1: number, x2: number, y2: number) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
}

import * as fs from 'fs';
import * as path from 'path';

export class Lights {
    RunLights() {
        let lines = this.LoadLines();

        lines.forEach(element => {
            let [cmd, x1, y1, x2, y2] = this.ParseLine(element)
            if (cmd === "on") {
                this.TurnOn(x1, y1, x2, y2)
            }
            if (cmd === "off") {
                this.TurnOff(x1, y1, x2, y2)
            }
            if (cmd === "toggle") {
                this.Toggle(x1, y1, x2, y2)
            }
        });
    }
    Brightness() {
        let brightness = 0;
        for (let i = 0; i < this.grid.length; i++) {
            if (this.grid[i].brightness) {
                brightness += this.grid[i].brightness;
            }
        }
        return brightness;
    }

    LoadLines(): string[] {

        let filename = path.join(__dirname, '../../day06.txt');
        let lines = fs.readFileSync(filename, 'utf8').trim().split('\n');

        return lines.map(line => line.trim())
    }

    ParseLine(instruction: string): [string, number, number, number, number] {
        
        let [lastCorner, through, firstCorner, command, dummy] = instruction.split(' ').reverse();

        let x2 = parseInt(lastCorner.split(',')[0]);
        let y2 = parseInt(lastCorner.split(',')[1]);

        let x1 = parseInt(firstCorner.split(',')[0]);
        let y1 = parseInt(firstCorner.split(',')[1]);
        
        return [command, x1, y1, x2, y2]
    }
    TurnOff(x1: number, y1: number, x2: number, y2: number) {
        for (let i = x1; i <= x2; i++) {
            for (let j = y1; j <= y2; j++) {
                this.grid[i*this.dimension + j].light = false;
                if (this.grid[i*this.dimension + j].brightness > 0)
                    this.grid[i*this.dimension + j].brightness -= 1;
            }
        }
    }
    Toggle(x1: number, y1: number, x2: number, y2: number) {
        for (let i = x1; i <= x2; i++) {
            for (let j = y1; j <= y2; j++) {
                this.grid[i*this.dimension + j].light = !this.grid[i*this.dimension + j].light;
                this.grid[i*this.dimension + j].brightness += 2;
            }
        }
    }

    TurnOn(x1: number, y1: number, x2: number, y2: number) {
        for (let i = x1; i <= x2; i++) {
            for (let j = y1; j <= y2; j++) {
                this.grid[i*this.dimension + j].light = true;
                this.grid[i*this.dimension + j].brightness += 1;
            }
        }
    }

    On() {

        let lightsOn = 0;
        for (let i = 0; i < this.grid.length; i++) {
            if (this.grid[i].light) {
                lightsOn += 1;
            }
        }
        return lightsOn;
    }

    grid:Light[] = [];
    dimension: number = 0;

    constructor(dimension: number) {

        this.dimension = dimension;
        for (let i = 0; i < dimension; i++) {
            for (let j = 0; j < dimension; j++) {
                this.grid.push(new Light(i, j))
            }
        }
    }

}

export function Part1() {

    let l = new Lights(1000);
    l.RunLights()

    return l.On();
}
export function Part2() {

    let l = new Lights(1000);
    l.RunLights()

    return l.Brightness();
}