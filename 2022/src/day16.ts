// --- Day 16: Proboscidea Volcanium ---

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

export class Valve {
    PressureRelease(time:number): any {
        return time * this.rate * (this.open ? 1 : 0);
    }
    Open() {
        this.open = true
    }
    id: any;
    rate!: number;
    leads: string[] = [];
    open: boolean = false;
    children: Valve[] = [];

    constructor(input: string) {

        if (input.length == 0) return

        // Valve BB has flow rate=13; tunnels lead to valves CC, AA
        let [_v,iDs,_h,_f,rateStr] = input.split(' ',5);
        this.id = iDs;
        this.rate = Number(rateStr.split('=')[1].split(';')[0])
        this.leads = input.split(/(valves|valve)/)[2].trim().split(', ').map(v => v.trim())

    }
}

export class ValveStructure {

    GetPressureReleased(valve: string, minutes: number, depth: number):number {
        if (depth -- < 1) return 0
        if (minutes <= 0) return 0
        let sum = 0
        let v = this.GetById(valve)
        v.Open()
        sum = v.PressureRelease(minutes - 2)
        for (let i = 0; i < v.leads.length; i++) {
            if (this.GetById(v.leads[i]).open == false) {
                sum += this.GetPressureReleased(v.leads[i], minutes - 2 - 2 * i, depth)
            }
        }
        return sum
    }
    GetById(vs: string): Valve {
        return this.valves.find(v => v.id == vs) as Valve
    }
    valves: Valve[] = [];
    constructor(input:string[]) {
        input.forEach(v => this.valves.push(new Valve(v)))
        this.valves.forEach(v => {
            v.leads.forEach(l => v.children.push(this.GetById(l)))
        })
    }
}