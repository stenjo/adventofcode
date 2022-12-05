// --- Day 5: Supply Stacks ---

export class CrateStack {
    RemoveCrate():string {
        return this.stack.pop() as string;
    }

    Top(): string {
        return this.stack[this.stack.length - 1];
    }

    AddCrate(crate: string) {
        this.stack.push(crate);
    }

    stack: string[];
    constructor(crateStrings: string[]) {

        this.stack = [];
    }
}

export class CrateMover {
    RunCraneMultiple(commands: string[]) {
        commands.forEach(c => { this.DoMoveMultiple(c) })
    }
    DoMoveMultiple(commandString: string) {
        let { items, to, from } = this.parseCommand(commandString);
        let batch:string[] = []
        for (let i = 0; i < items; i++) {
            batch.push(this.crateStacks[from-1].RemoveCrate())
        }
        for (let i = 0; i < items; i++) {
            this.crateStacks[to-1].AddCrate(batch.pop() as string)
        }
    }
    RunCrane(commands: string[]) {
        commands.forEach(c => { this.DoMove(c) })
    }
    TopString(): string {
        let topString = ''
        this.crateStacks.forEach((crate) => topString += crate.Top());
        return topString;
    }
    DoMove(commandString: string) {
        let { items, to, from } = this.parseCommand(commandString);
        for (let i = 0; i < items; i++) {
            this.crateStacks[to-1].AddCrate(this.crateStacks[from-1].RemoveCrate())
        }
    }
    private parseCommand(command: string) {
        let [_move, itemsString, _from, fromStack, _to, toStack] = command.split(' ');
        let items = parseInt(itemsString);
        let from = parseInt(fromStack);
        let to = parseInt(toStack);

        return { items, to, from };
    }

    Top(stackNumber: number): any {
        return this.crateStacks[stackNumber-1].Top();
    }

    GetCrates(input: string): string[] {

        let commaString = input.split('')
        for (let i = 3; i < commaString.length; i+=4) {
            commaString[i] = ','
        }
        for (let i = commaString.length-1; i >= 0; i -=2) {
            commaString.splice(i,1)
        }
        return commaString.join('').split(',')
    }
    StackCount(): any {
        return this.crateStacks.length;
    }
    
    crateStacks: CrateStack[];

    constructor(crates: string[]) {
        this.crateStacks = [];
        if (crates.length == 0) return

        this.parseCratesSpec(crates);
        
    }

    private parseCratesSpec(crates: string[]) {
        let inputStrings = crates.reverse();

        inputStrings.forEach(line => {
            let crates = this.GetCrates(line)
            for (let i = 0; i < crates.length; i++) {
                if (this.crateStacks.length <= i) {
                    this.crateStacks.push(new CrateStack([]))
                }
                if (crates[i] != ' ') {
                    this.crateStacks[i].AddCrate(crates[i])
                }
            }
        })
    }

}

import * as fs from 'fs';
import * as path from 'path';

export class FileInput {
    Commands() {

        return this.lines.slice(this.lines.indexOf('')+1,this.lines.length)
    }
    Stacks():string[] {

        return this.lines.slice(0, this.lines.indexOf(''))
    }

    lines: string[];

    constructor(fname: string) {
        let filename = path.join(__dirname, fname);
        this.lines = fs.readFileSync(filename, 'utf8').split('\n');
    }
}