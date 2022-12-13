// --- Day 13: Distress Signal ---

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
        let startIndex = i;
        for (let j = i + 1; j < content.length; j++) {
            if (content.charAt(j) === '[') {
                startIndex = i;
                nesting++;
            }
            if (content.charAt(j) === ']') {
                if (nesting > 0) {
                    nesting--;
                }
                else {
                    let sub = content.substring(startIndex, j + 1);
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
    constructor(p1:string, p2:string) {

    }
}