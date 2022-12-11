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
    AddWorry(w: number) {
            this.worries.push(w);
    }
    GetNextWorry(): number {
        if (this.hasWorries() == false) {
            return 0;
        }
        return this.worries.shift() as number;
    }

    hasWorries() {
        return this.worries.length > 0;
    }

    TestAndThrow(worry: number): number {
        this.inspects++
        if (worry % this.divisibleBy == 0 && worry > 0) {
            return this.throwIfTrue
        }
        return this.throwIfFalse
    }
    
    RunOperation(worry: number, releaf = true, l = 1): number {
        
        if (releaf) {
            return Math.floor(this.GetNewWorryLevel(worry, l) / 3);
        }

        return this.GetNewWorryLevel(worry, l);
    }
    GetNewWorryLevel(worry: number, lcm: number): number {
        const [argStr1, argStr2] = this.operation.split(/[+*]/).map(o => o.trim());
  
        let arg1:number = argStr1 === 'old' ? worry : NaN
        let arg2:number = argStr2 === 'old' ? worry : isNaN(Number(argStr2)) ? NaN : parseInt(argStr2, 10)

        if (this.operation.includes('+')) {
            return arg1 + arg2
        }
        if (this.operation.includes('*')) {
            if (lcm != 1)
                return arg1 % lcm * arg2 % lcm
            else
                return arg1 * arg2
        }
    
        return NaN;
    }
    private lcm(a:number,b:number): number {
        const gcd = (x:number, y:number):number => (!y ? x : gcd(y, x % y));
        const _lcm = (x:number, y:number):number => (x * y) / gcd(x, y);
        return [a,b].reduce((a, b) => _lcm(a, b));
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
    lcm: number;
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
        while (monkey.hasWorries()) {
            let w = monkey.RunOperation(monkey.GetNextWorry(), this.releaf, this.lcm);
            // let g = this.gcd(w, this.lcm)
   
            let m = monkey.TestAndThrow(w) //) / this.lcm);
            let targetMonkey = this.FindMonkey(m)
            targetMonkey.AddWorry(w)
        }
    }
    FindMonkey(m: number) {
        return this.monkeys.find(x => x.id == m) as Monkey;
    }
    Inspect(monkey: Monkey) {
        let w = monkey.RunOperation(monkey.GetNextWorry(), this.releaf);
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
        let divisors = this.monkeys.map(m=>m.divisibleBy)
        this.lcm = divisors.reduce((l, c) =>this._lcm(l,c))
    }

    releaf: boolean = true;
    monkeys: Monkey[];
    constructor() {
        this.monkeys = [];
        this.lcm = 1
    }

    private _lcm(x:number,y:number):number {
        return x * y / this.gcd(x,y)
    }
    private gcd(x:number, y:number):number {
        return !y ? x : this.gcd(y, x % y);
    }
}


// let m = new MonkeySim();
// let input = new LoadLines('../test/input/day11.txt').lines
// m.LoadMonkeys(input)

// m.releaf = false;
// m.RunRound(10000)

// console.log(m.GetMonkeyBusiness())
