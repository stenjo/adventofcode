// --- Day 7: Internet Protocol Version 7 ---
// While snooping around the local network of EBHQ, you compile a list of
// IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd
// like to figure out which IPs support TLS (transport-layer snooping).

// An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or
// ABBA. An ABBA is any four-character sequence which consists of a pair of
// two different characters followed by the reverse of that pair, such as
// xyyx or abba. However, the IP also must not have an ABBA within any
// hypernet sequences, which are contained by square brackets.

// For example:

// abba[mnop]qrst supports TLS (abba outside square brackets).
// abcd[bddb]xyyx does not support TLS (bddb is within square brackets,
// even though xyyx is outside square brackets).
// aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior
// characters must be different).
// ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets,
// even though it's within a larger string).

// How many IPs in your puzzle input support TLS?

import * as fs from 'fs';
import * as path from 'path';

export class Ip {
    address: string;
    hypernet: string;
    supernet: string;
    constructor(address: string) {
        this.address = address
        this.hypernet = ""
        this.supernet = ""
        let part = "super"
        this.address.split("").forEach(ch => {
            if (ch == "[") {
                part = "hyper"
            }
            if (ch == "]") {
                part = "super"
            }
            if (part == "hyper") {
                this.hypernet += ch;
            }
            if (part == "super") {
                this.supernet += ch
            }
        })
    }

    supportsSSL(): boolean {
    
        let hypernetSequence = 0;
        let abas = 0

        for (let i = 0; i < this.supernet.length-2; i++) {

            // if (this.address.charAt(i) === '[') {
            //     hypernetSequence += 1
            //     continue
            // }
            // if (this.address.charAt(i) === ']') {
            //     hypernetSequence -= 1
            //     continue
            // }

            let aba = this.supernet.substring(i,i+3)
            let [x,y,z] = aba.split("");
            let flip = [y,x,y].join("");

            if (this.isABA(aba) && this.hypernet.includes(flip)) {
                // if (hypernetSequence > 0) {
                //     return false
                // }
                abas += 1
            }
        }

        return abas > 0
    }

    private isInRestOfString(i: number, substr: string) {
        return this.address.substring(i + 3, this.address.length).includes(substr);
    }

    private isABA(aba: string): boolean {
        if (aba.includes("[") || aba.includes("]")) {
            return false
        }
        return aba.charCodeAt(0) == aba.charCodeAt(2) && aba.charCodeAt(0) != aba.charCodeAt(1);
    }

    supportsTLS(): boolean {
    
        let hypernetSequence = 0;
        let abbas = 0

        for (let i = 0; i < this.address.length-2; i++) {

            if (this.address.charAt(i) === '[') {
                hypernetSequence += 1
                continue
            }
            if (this.address.charAt(i) === ']') {
                hypernetSequence -= 1
                continue
            }

            let pair = this.address.substring(i,i+2)
            let reverse = this.address.substring(i+2,i+4).split("").reverse().join("");

            if (pair == reverse && pair.charCodeAt(0) != pair.charCodeAt(1)) {
                if (hypernetSequence > 0) {
                    return false
                }
                abbas += 1
            }
        }

        return abbas > 0
    }
}

export class Snooping {
    loadlines():string[] {
        let filename = path.join(__dirname, '../../day07.txt')
        let lines = fs.readFileSync(filename, 'utf8').trim().split('\n')
        return lines;
    }

    Part1():number {

        let count = 0
        this.loadlines().forEach(line => {
            let ip = new Ip(line.trim());
            if (ip.supportsTLS()) {
                count += 1
            }
        })

        return count
    }

    Part2():number {

        let count = 0
        this.loadlines().forEach(line => {
            let ip = new Ip(line.trim());
            if (ip.supportsSSL()) {
                count += 1
            }
        })

        return count
    }
}

