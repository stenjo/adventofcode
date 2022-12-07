// --- Day 7: No Space Left On Device ---

export class FileElement {
    fileName: string;
    fileSize: number;
    children: FileElement[];
    isDirectory: boolean;
    parent: FileElement|null;

    constructor(fileName: string, fileSize: number, dir: boolean = false) { 
        this.fileName = fileName;
        this.fileSize = fileSize;
        this.children = [];
        this.isDirectory = dir;
        this.parent = null;
    }
}


export class Cli {
    GetDeletCandidateSize(): any {
        let deleteCandidates: number[] = []
        const totalSize: number = 70000000
        const needed: number = 30000000
        const unused: number = totalSize - this.GetCurrentDirSize()
        const minimum: number = needed - unused

        let dirSizes:number[] = []
        this.GetDirSizez(dirSizes);
        

    }
    GetDirSizez(dirSizes: number[]) {
        
    }
    GetDirSizeSumMax100K(f:FileElement = this.root): any {
        let sum = 0;
        if (f.isDirectory) {
            if (f.fileSize <= 100000) sum = f.fileSize;
            f.children.forEach(child => {
                sum += this.GetDirSizeSumMax100K(child)
            })
        }
        return sum;
    }
    ParseLine(line: string) {
        let [p, cmd, params] = line.split(' ');
        if (p == '$') {
            this.listmode = false;
            if (cmd == 'cd') {
                this.ChangeDir(params)
            }

            if (cmd == 'ls') {
                this.listmode = true;
            }
            return
        }
        if (this.listmode && p == 'dir') {
            this.AddDir(cmd)
            return
        }
        if (this.listmode && !isNaN(+p)) {
            let size = parseInt(p)
            this.AddFile(cmd, size)
        }

    }
    GetCurrentDirSize(): number {
        let sum = 0
        for (let i = 0; i < this.current.children.length; i++) {
            sum += this.current.children[i].fileSize
        }
        this.current.fileSize = sum
        return sum
    }
    AddFile(name: string, size: number) {
        this.current.children.push(new FileElement(name, size));
        this.GetCurrentDirSize()
    }
    AddDir(name: string) {
        let item = new FileElement(name, 0, true);
        item.parent = this.current
        this.current.children.push(item);
        return item;
    }
    List() {
        return this.current.children.map(f => f.fileName);
    }
    GetCurrentDir(): string {
        return this.current.fileName;
    }
    ChangeDir(name: string){
        if (name == '/') {
            while(this.current != this.root) {
                this.ChangeDir('..')
            }
            return
        }
        if (name == '..') {
            this.current = this.current.parent as FileElement
            this.GetCurrentDirSize()
            return
        }
        let elmnt = this.current.children.find(f => f.fileName === name)
        if (elmnt === undefined) {
            this.current = this.AddDir(name);
            return
        }
        this.current = elmnt as FileElement;
    }
    current: FileElement;
    root: FileElement;
    listmode: boolean;
    constructor() {
        this.current = new FileElement('/', 0, true);
        this.current.parent = this.current;
        this.root = this.current
        this.listmode = false;
    }
}

import * as fs from 'fs';
import * as path from 'path';

export class FileInput {

    data: string[];

    constructor(fname: string) {
        let file = path.join(__dirname,fname);
        this.data = fs.readFileSync(file, 'utf8').trim().split('\n')
    }
}