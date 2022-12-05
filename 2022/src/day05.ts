

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
        commands.forEach(c => {
            this.DoMoveMultiple(c)
        })
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
        commands.forEach(c => {
            this.DoMove(c)
        })
    }
    TopString(): string {
        let topString = ''
        this.crateStacks.forEach((crate) => topString += crate.Top());
        return topString;
    }
    DoMove(commandString: string) {
        if (commandString.trim().length == 0) return
        let { items, to, from } = this.parseCommand(commandString);
        for (let i = 0; i < items; i++) {
            this.crateStacks[to-1].AddCrate(this.crateStacks[from-1].RemoveCrate())
        }
        
    }
    private parseCommand(command: string) {
        let [_move, numOfItems, _from, fromStack, _to, toStack] = command.split(' ');
        let items = parseInt(numOfItems);
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

        let inputStrings = crates.reverse()
        let stacks = this.getStackRangeFromInput(inputStrings[0]);
        for (let i = 0; i < stacks; i++) {
            this.crateStacks.push(new CrateStack([]))
        }

        inputStrings.splice(0,1)

        inputStrings.forEach(line => {
            let crates = this.GetCrates(line)
            for (let i = 0; i < this.StackCount(); i++) {
                if (crates[i] != ' ') {
                    this.crateStacks[i].AddCrate(crates[i])
                }
            }
        })
        
    }

    private getStackRangeFromInput(input: string): number {
        let splitString = input.split(' ');
        let filteredString = splitString.filter((item) => item != '');
        let numbers = filteredString.map(number => parseInt(number, 10));
        let sorted = numbers.sort();
        return sorted.pop() as number;
    }
}

import * as fs from 'fs';
import * as path from 'path';
export class FileInput {
    Commands() {
        let commands: string[] = [];
        let belowStacks = false;
        for (let i = 0; i < this.lines.length; i++)  {
            if (belowStacks) commands.push(this.lines[i])
            if (this.lines[i] == '') belowStacks = true;
        }
        return commands;
    }
    Stacks():string[] {
        let stacks: string[] = [];
        for (let i = 0; i < this.lines.length; i++)  {
            if (this.lines[i] == '') return stacks
            stacks.push(this.lines[i])
        }
        return stacks;
    }
    lines: string[];
    constructor(fname: string) {
        let filename = path.join(__dirname, fname);
        this.lines = fs.readFileSync(filename, 'utf8').split('\n');
    }
}