// --- Day 6: Tuning Trouble ---
// The preparations are finally complete; you and the Elves leave camp on
// foot and begin to make your way toward the star fruit grove.

// As you move through the dense undergrowth, one of the Elves gives you a
// handheld device. He says that it has many fancy features, but the most
// important one to set up right now is the communication system.

export class Communicator {
    FindMarker(dataStream: string, len: number):number {
        let stream = dataStream.split('');
        for (let i = len; i < stream.length; i++) {
            if (this.isValidMarker(stream.slice(i-len, i), len)) {
                return i;
            }
        }
        return dataStream.length
    }

    isValidMarker(marker: string[], len: number): boolean {
        return marker.filter((s, n, arr) => !arr.slice(0, n).includes(s)).length == len;
    }

    constructor() {
    }
}

import * as fs from 'fs';
import * as path from 'path';

export class FileInput {

    data: string;

    constructor(fname: string) {
        let file = path.join(__dirname,fname);
        this.data = fs.readFileSync(file, 'utf8').trim()
    }
}