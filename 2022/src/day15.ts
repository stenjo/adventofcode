
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

export class Sensor {
    x: number;
    y: number;
    range: number;

    constructor(x: number, y: number, r: number) {
        this.x = x;
        this.y = y;
        this.range = r;
    }
}   

export class Beacon {
    x: number;
    y: number;
    range!: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
}   

export class Cave {
    CoverageAtLine(line: number):number {
        return this.coverage.filter(c => c.y == line).length;
    }
    SensorAt(arg0: number, arg1: number) {
        let sensor = this.sensors.filter(s => s.x === arg0 && s.y === arg1)
        if (sensor.length == 1) {
            return sensor[0]
        }
        else if (sensor.length == 0) {
            return undefined
        }
        else {
            throw new Error("Multiple sensors on list")
        }
    }

    sensors: Sensor[] = [];
    beacons: Beacon[] = [];;
    coverage: {x: number, y: number}[] = [];
    Deploy(deployStr: string) {
        let [_s,_a,pXS,pYS,_c,_b,_i,_at,bXS,bYS] = deployStr.split(' ');
        let sx = Number(pXS.slice(2, pXS.length-1))
        let sy = Number(pYS.slice(2, pYS.length-1))
        let bx = Number(bXS.slice(2, bXS.length-1))
        let by = Number(bYS.slice(2))

        let mh = this.manhattan(sx, sy, bx, by)

        this.sensors.push(new Sensor(sx, sy, mh))
        if (this.BeaconAt(bx,by) == false) {
            this.beacons.push(new Beacon(bx,by))
        }

        for (let y = sy - mh; y <= sy + mh; y++) {
            for (let x = sx - mh; x <= sx + mh; x++) {
                if (this.manhattan(sx,sy,x,y) <= mh 
                && this.BeaconAt(x,y) == false 
                && this.CoverageAt(x,y) == false) {
                    this.coverage.push({ x, y })
                }
            }
        }
    }
    BeaconAt(x: number, y: number): any {
        return this.beacons.filter(b => b.x === x && b.y === y).length > 0;
    }
    CoverageAt(x: number, y: number) {
        return this.coverage.filter(b => b.x === x && b.y === y).length > 0;
    }
    private manhattan(sx: number, sy: number, bx: number, by: number) {
        return Math.abs(by-sy) + Math.abs(bx - sx)
    }

    constructor() {}
}