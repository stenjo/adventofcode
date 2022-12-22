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
    oreCost!: number;
    clayCost!: number;
    type!: string;
    count!: number;
    robots!:number;
    obsidianCost!: number;

    constructor(type: string, oreCost: number, clayCost: number = 0, obsidianCost:number = 0) {
        this.type = type;
        this.oreCost = oreCost;
        this.clayCost = clayCost;
        this.obsidianCost = obsidianCost;
        this.count = 0
        this.robots = 0
    }
}
export class Blueprint {
    Run(minutes: number) {
        for (let i = 0; i < minutes; i++) {

            this.geode.count += this.geode.robots
            if (this.ore.count >= this.geode.oreCost && this.obsidian.count >= this.geode.obsidianCost) {
                this.geode.robots ++
                this.obsidian.count -= this.geode.obsidianCost
                this.ore.count -= this.geode.oreCost
            }
            
            this.obsidian.count += this.obsidian.robots
            if (this.clay.count >= this.obsidian.clayCost && this.ore.count >= this.obsidian.oreCost) {
                this.obsidian.robots ++
                this.clay.count -= this.obsidian.clayCost
                this.ore.count -= this.obsidian.oreCost
            }

            this.clay.count += this.clay.robots
            if (this.ore.count >= this.clay.oreCost && (this.clay.robots < 3) || false ) {
                this.ore.count -= this.clay.oreCost
                this.clay.robots ++
            }

            this.ore.count ++
        }
        return
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
        this.obsidian = new Robot('obsidian', Number(costStrings[3].split(' ')[0]), Number(costStrings[3].split(' ')[3]))
        this.geode = new Robot('geode', Number(costStrings[4].split(' ')[0]), 0, Number(costStrings[4].split(' ')[3]))
    }
}

export class BlueprintHandler {
    blueprints: Blueprint[] = [];
    constructor(assortment: string[]) {
        assortment.forEach(l => this.blueprints.push(new Blueprint(l)))
    }
}