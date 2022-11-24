import * as fs from 'fs';
import * as path from 'path';

class Position {
    x: number;
    y: number;
    constructor(x: number, y: number) { this.x = x; this.y = y; }
}
export class Taxicab {
    Blocks(instruction: string): number {
        let directionsList = instruction.split(',')
        let turn = ' ';
        let heading = 'N'
        let p:Position = new Position(0,0)

        directionsList.forEach(direction => {
            turn = getTurn(direction.trim());
            heading = getHeading(heading, turn);
            let length = getLength(direction.trim());
            p = moveTo(heading, length, p);
        })

        return Math.abs(p.x)+ Math.abs(p.y);

        function moveTo(head: string, len: number, pos: Position): Position {
            if (head === 'N') {
                pos.y += len;
            }
            if (head === 'E') {
                pos.x += len;
            }
            if (head === 'S') {
                pos.y -= len;
            }
            if (head === 'W') {
                pos.x -= len;
            }
            return pos
        }

        function getHeading(heading: string, turn: string): string {
            const directions: string[] = ['N', 'E', 'S', 'W'];
            let now = directions.indexOf(heading)
            if (turn === 'R') {
                now = (now + 1) % directions.length;
            }
            if (turn === 'L') {
                now = (now - 1)
                if (now === -1) {
                    now += directions.length;
                }
            }
            return directions[now];
        }

        function getLength(direction: string) {
            let numString = direction.substring(1).trim()
            return parseInt(numString);
        }

        function getTurn(direction: string): string {
            return direction.charAt(0);
        }
    }

    LoadLines():string {
        let filename = path.join(__dirname,'../../day01.txt');
        let lines = fs.readFileSync(filename, 'utf8').trim();

        return lines;
    }
}