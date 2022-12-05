// --- Day 5: Supply Stacks ---

// The expedition can depart as soon as the final supplies have been
// unloaded from the ships. Supplies are stored in stacks of marked crates,
// but because the needed supplies are buried under many other crates, the
// crates need to be rearranged.

// The ship has a giant cargo crane capable of moving crates between stacks.
// To ensure none of the crates get crushed or fall over, the crane operator
// will rearrange them in a series of carefully-planned steps. After the
// crates are rearranged, the desired crates will be at the top of each stack.

// The Elves don't want to interrupt the crane operator during this delicate
// procedure, but they forgot to ask her which crate will end up where, and
// they want to be ready to unload them as soon as possible so they can embark.

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

        return  input.split(' ')
                .filter((item) => item != '')
                .map(number => parseInt(number, 10))
                .sort()
                .pop() as number;
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