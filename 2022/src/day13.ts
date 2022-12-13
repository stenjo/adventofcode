// --- Day 13: Distress Signal ---

import * as fs from 'fs';
import * as path from 'path';
export class LoadLines {
    lines: string[];
    pairs: string[][];
    constructor(fname: string) {
      this.lines = fs
        .readFileSync(path.join(__dirname, fname), 'utf8')
        .trim()
        .split('\n')
        .map(line => line.trim());
        this.pairs = []

        let pair:string[] = []
        this.lines.forEach(line => {
            if (line == '' && pair.length > 0) {
                this.pairs.push(pair)
                pair = []
            }
            else {
                pair.push(line)
            }
        })
        if (pair.length > 0) {
            this.pairs.push(pair)
        }
    }
}

export class Packet {
    packet: (Packet | number) []
    constructor(ps: string) {
        this.packet = []
        if (ps.length > 2) {
            let start = ps.indexOf('[')
            let end = ps.lastIndexOf(']')
            let content = ps.substring(start+1,end)
            let numString = ''
            for (let i = 0; i < content.length; i++) {
                if (content.charAt(i) === '[') {
                    i = this.subPacket(i, content);
                }
                if (content.charAt(i) === ',') {
                    if (numString.length > 0) {
                        this.packet.push(Number(numString))
                        numString = ''
                    }
                }
                else {
                    numString += content.charAt(i)
                }
            }
            if (numString.length > 0) {
                this.packet.push(Number(numString))
                numString = ''
            }
        }
    }

    private subPacket(i: number, content: string) {
        let nesting = 0;
        for (let j = i + 1; j < content.length; j++) {
            if (content.charAt(j) === '[') {
                nesting++;
            }
            if (content.charAt(j) === ']') {
                if (nesting > 0) {
                    nesting--;
                }
                else {
                    let sub = content.substring(i, j + 1);
                    this.packet.push(new Packet(sub));
                    i = j + 1;
                    j = content.length;
                    continue;
                }
            }
        }
        return i;
    }
}
export class Comparator {
    ComparePair(pair: string[]) {
        let p1 = new Packet(pair[0])
        let p2 = new Packet(pair[1])
        return this.compare(p1, p2);
    }
    compare(val1:Packet | number, val2: Packet | number):string {
        if (typeof val1 === 'number' && typeof val2 === 'number') {
            if (val1 === val2) return 'same'
            if (val1 < val2) return 'right'
            if (val1 > val2) return 'wrong'
        }

        if (typeof val1 === 'number') {
            val1 = new Packet('['+val1+']')
        }
        if (typeof val2 === 'number') {
            val2 = new Packet('['+val2+']')
        }
        for (let i = 0; i < Math.min(val1.packet.length, val2.packet.length); i++) {
            let r = this.compare(val1.packet[i], val2.packet[i])
            console.log(r)
            if (!r.includes('same')) return r
        }
        if (val1.packet.length < val2.packet.length) return 'right'
        if (val1.packet.length > val2.packet.length) return 'wrong'
        return 'same'
    }
    constructor() {
    }
}