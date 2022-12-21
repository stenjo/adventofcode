// --- Day 21: Monkey Math ---

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
    name!: string;
    left!: string;
    op!: string;
    right!: string;
    leftMonkey: Monkey | undefined;
    rightMonkey: Monkey | undefined;

    Yell(): number {
        if (this.op !== undefined) {
            if (this.op == '-') {
                return this.LeftMonkey().Yell() - this.RightMonkey().Yell();
            }
        }
        return this.Left() as number;
    }
    RightMonkey(): Monkey {
        if (this.rightMonkey == undefined) {
            throw new Error('Right Monkey does not exist')
        }
        return this.rightMonkey as Monkey;
    }
    LeftMonkey(): Monkey {
        if (this.leftMonkey == undefined) {
            throw new Error('Left Monkey does not exist')
        }
        return this.leftMonkey as Monkey;
    }
    Op(): string {
        return this.op
    }
    Name(): string {
        return this.name
    }
    Right(): string {
        return this.right
    }
    Left(): string | number {
        if (Number.isNaN(Number(this.left)) === false) {
            return Number(this.left);
        }
        return this.left
    }

    constructor(config: string) {
        // Parse pattern
        if (config.length == 0) return
        this.name = config.split(':')[0]
        this.left = config.split(': ')[1]
        if (this.left.split(' ').length > 1) {
            this.op = this.left.split(' ')[1]
            this.right = this.left.split(' ')[2]
            this.left = this.left.split(' ')[0]
        }
    }
}

export class MonkeyYeller {
    Monkey(monkeyId: string): Monkey {
        let monkey = this.monkeys.find(m => m.name == monkeyId);
        if (monkey == undefined) {
            return new Monkey('')
        }
        return monkey as Monkey
    }
    monkeys!: Monkey[];

    constructor(config: string[]) {
        this.monkeys = [];
        config.forEach(c => this.monkeys.push(new Monkey(c)));
        for (let i = 0; i < this.monkeys.length;i++) {
            if (typeof this.monkeys[i].Left() == 'string') {
                this.monkeys[i].leftMonkey = this.Monkey(this.monkeys[i].left);
            }
            if (typeof this.monkeys[i].Right() == 'string') {
                this.monkeys[i].rightMonkey = this.Monkey(this.monkeys[i].right);
            }
        }
    }
}