// --- Day 11: Monkey in the Middle ---

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
  
export class Monkey {
    GetNextWorry(): number {
        if (this.hasNoWorries()) {
            return NaN;
        }
        return this.worries.shift() as number;
    }

    hasNoWorries() {
        return this.worries.length === 0;
    }

    TestAndThrow(worry: number): number {
        this.inspects++
        if (worry % this.divisibleBy == 0) {
            return this.throwIfTrue
        }
        return this.throwIfFalse
    }
    RunOperation(worry: number): number{
        if (this.operation.includes('+')) {
            let [_arg1, arg2] = this.operation.split('+')
            if (arg2.trim() === 'old'){
                return Math.floor((worry + worry) / 3)
            }
            if (!isNaN(Number(arg2))) {
                return Math.floor((worry + parseInt(arg2, 10))/3)
            }
        }
        if (this.operation.includes('*')) {
            let [_arg1, arg2] = this.operation.split('*')
            if (arg2.trim() === 'old'){
                return Math.floor((worry * worry)/3)
            }
            if (!isNaN(Number(arg2))) {
                return Math.floor((worry * parseInt(arg2, 10))/3)
            }
        }

        return NaN;
    }
    throwIfFalse!: number;
    throwIfTrue!: number;
    divisibleBy!: number;
    id!: number;
    worries: number[] = [];
    operation!: string;
    inspects!: number;
    constructor(setup:string[]) {
        if (setup.length == 0) return
        this.id = this.setId(setup[0]);
        this.setItems(setup);
        this.setOperation(setup);
        this.setDivisibleBy(setup);
        this.setOutcomes(setup);
        this.inspects = 0;
    }

    private setOutcomes(setup: string[]) {
        if (setup.length > 5) {
            this.throwIfTrue = parseInt(setup[4].split(' ').pop() as string, 10);
            this.throwIfFalse = parseInt(setup[5].split(' ').pop() as string, 10);
        }
    }

    private setDivisibleBy(setup: string[]) {
        if (setup.length > 3) {
            this.divisibleBy = parseInt(setup[3].split(' ').pop() as string, 10);
        }
    }

    private setOperation(setup: string[]) {
        if (setup.length > 2) {
            let [_descr, operationStr] = setup[2].trim().split(':');
            this.operation = operationStr.split('=')[1].trim();
        }
    }

    private setItems(setup: string[]) {
        if (setup.length > 1) {
            let [_descr, list] = setup[1].trim().split(':');
            list.split(',').forEach(e => this.worries.push(parseInt(e)));
        }
    }

    private setId(setup: string) {
        let [_monkey, idString] = setup.replace(':', '').split(' ');
        return parseInt(idString);
    }
}

export class MonkeySim {
    GetMonkeyBusiness(): any {
        let inspects = this.monkeys.map((monkey) => monkey.inspects)
        inspects.sort((a, b) => b - a);
        return inspects[0] * inspects[1]
    }
    RunRound(rounds = 1) {
        for (let i = 0; i < rounds; i++) {
            this.monkeys.forEach(m => this.InspectMonkey(m))
        }
    }
    InspectMonkey(monkey: Monkey) {
        while (!monkey.hasNoWorries()) {
            let {monkey:m, worry:w} = this.Inspect(monkey);
            this.monkeys[m].worries.push(w)
        }
    }
    Inspect(monkey: Monkey) {
        let w = monkey.RunOperation(monkey.GetNextWorry());
        let m = monkey.TestAndThrow(w);

        return {monkey:m, worry:w}
       
    }

    LoadMonkeys(input: string[]) {
        let batch: string[][] = [];
        let chunk:string[] = new Array();
        input.forEach(l=>{
            if (l.length == 0) {
                batch.push(chunk);
                chunk = new Array()
            }
            else {
                chunk.push(l)
            }
        }) 
        batch.push(chunk);
        batch.forEach(m=>this.monkeys.push(new Monkey(m)))
    }

    monkeys: Monkey[];
    constructor() {
        this.monkeys = [];
    }
}