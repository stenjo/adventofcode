
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
    TuningFreq(arg0: number) {
        throw new Error('Method not implemented.');
    }
    CoverageAtLine(line: number):number {
        this.coverage = []
        this.sensors.forEach(s => this.addCoverage(s, line));
        let sum = this.coverage.reduce((acc, s) => {
            return acc + (s.end - s.start);
        }, 0);
        return sum;
    }
    GetSensorAt(arg0: number, arg1: number) {
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
    coverage: {start: number, end: number}[] = [];
    cov: number[] = [];
    Deploy(deployStr: string) {
        if (deployStr.length == 0) return
        
        let [_s,_a,pXS,pYS,_c,_b,_i,_at,bXS,bYS] = deployStr.split(' ');
        let sx = Number(pXS.slice(2, pXS.length-1))
        let sy = Number(pYS.slice(2, pYS.length-1))
        let bx = Number(bXS.slice(2, bXS.length-1))
        let by = Number(bYS.slice(2))

        let mh = this.manhattan(sx, sy, bx, by)

        let s = new Sensor(sx, sy, mh)
        this.sensors.push(s)
        if (this.BeaconAt(bx,by) == false) {
            this.beacons.push(new Beacon(bx,by))
        }
    }

    private addCoverage(sensor:Sensor, y:number) {
        let range = (2 * sensor.range + 1) - 2 *Math.abs(sensor.y - y)
        let start = sensor.x - sensor.range + Math.abs(sensor.y - y)
        let end = start + range
        let checked: {start: number, end: number}[] = []

        if (range < 0) return

        while(this.coverage.length > 0 ) {
            let c = this.coverage.shift() as {start: number, end: number}
            if (start <= c.start && end >= c.end) {
                continue
            }
            if (start < c.start && end > c.start && end < c.end) {
                checked.push({start: end, end: c.end})
                continue
            }
            if (start > c.start && start < c.end && end >= c.end) {
                checked.push({start: c.start, end: start})
                continue
            }
            checked.push(c)
        }
        checked.push({start: start, end: start + range})
        checked.forEach(c => this.coverage.push(c))
    }

    SensorAt(x: number, y: number): boolean {
        return this.sensors.filter(b => b.x === x && b.y === y).length > 0;
    }
    BeaconAt(x: number, y: number): boolean {
        return this.beacons.filter(b => b.x === x && b.y === y).length > 0;
    }
    CoverageAt(x: number, y: number): boolean {
        return this.coverage.filter(b => b.start === x && b.end === y).length > 0;
    }
    private manhattan(sx: number, sy: number, bx: number, by: number): number {
        return Math.abs(by-sy) + Math.abs(bx - sx)
    }

    constructor() {}
}