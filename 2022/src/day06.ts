// --- Day 6: Tuning Trouble ---

export class Communicator {
    FindMessageMarker(dataStream: string) {
        let stream = dataStream.split('');
        for (let i = 14; i < stream.length; i++) {
            let marker = stream.slice(i-14, i);

            if(this.startOfMessage(marker)) {
                return i;
            }

        }
    }
    FindPacketMarker(dataStream: string) {
        let stream = dataStream.split('');
        for (let i = 4; i < stream.length; i++) {
            let marker = stream.slice(i-4, i);

            if(this.startOfPacket(marker)) {
                return i;
            }

        }
    }

    startOfPacket(marker: string[]) {
        return marker.filter((s, n, arr) => !arr.slice(0, n).includes(s)).length == 4;
    }

    startOfMessage(marker: string[]) {
        return marker.filter((s, n, arr) => !arr.slice(0, n).includes(s)).length == 14;
    }
    constructor() {

    }
}

import * as fs from 'fs';
import * as path from 'path';
export class FileInput {
    lines: string;

    constructor(fname: string) {
        let file = path.join(__dirname,fname);
        this.lines = fs.readFileSync(file, 'utf8').trim()
    }
}