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
            let cotent = ps.substring(start+1,end)
            if (cotent.includes('[')) {
                this.packet.push(new Packet(cotent))
                return
            }
            ps.substring(start+1,end).split(',').forEach(n => this.packet.push(Number(n)))
        }
    }
}
export class Comparator {
    constructor(p1:string, p2:string) {

    }
}