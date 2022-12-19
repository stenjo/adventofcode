// --- Day 19: Not Enough Minerals ---

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
export class Robot {
    cost!: number;
    type!: string;
    count!: number;
    robots!:number;

    constructor(type: string, cost: number) {
        this.type = type;
        this.cost = cost;
        this.count = 0
        this.robots = 0
    }
}
export class Blueprint {
    Run(minutes: number) {
        this.ore.count = (minutes +1) % this.clay.cost + 1
        // this.clay.count = Math.floor((minutes - 1) / 2) * this.clay.robots
        this.clay.robots = Math.floor((minutes - 1) / this.clay.cost)
        if (minutes == 3) {
            this.clay.count = 0
            // this.clay.robots = 1
        }
        if (minutes == 4 ) {
            this.clay.count = 1
            // this.clay.robots = 1
        }
        if (minutes == 5 ) {
            this.clay.count = 2
            // this.clay.robots = 2
        }
        if (minutes == 6 ) {
            this.clay.count = 4
            // this.clay.robots = 2
        }
    }
    ore!: Robot;
    clay!: Robot;
    obsidian!: Robot;
    geode!: Robot;
    id!: number;
    constructor(def: string) {
        let [_bp, bpNo] = def.split(':')[0].split(' ')
        this.id = Number(bpNo)
        let costStrings = def.split(/ robot costs /)
        this.ore = new Robot('ore', Number(costStrings[1].split(' ')[0]))
        this.clay = new Robot('clay', Number(costStrings[2].split(' ')[0]))
        this.obsidian = new Robot('obsidian', Number(costStrings[3].split(' ')[0]))
        this.geode = new Robot('geode', Number(costStrings[4].split(' ')[0]))
    }
}

export class BlueprintHandler {
    blueprints: Blueprint[] = [];
    constructor(assortment: string[]) {
        assortment.forEach(l => this.blueprints.push(new Blueprint(l)))
    }
}