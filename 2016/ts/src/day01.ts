import * as fs from 'fs';
import * as path from 'path';

// --- Day 1: No Time for a Taxicab ---
// You're airdropped near Easter Bunny Headquarters in a city somewhere.
// "Near", unfortunately, is as close as you can get - the instructions on the
// Easter Bunny Recruiting Document the Elves intercepted start here, and
// nobody had time to work them out further.

// The Document indicates that you should start at the given coordinates
// (where you just landed) and face North. Then, follow the provided sequence:
// either turn left (L) or right (R) 90 degrees, then walk forward the given
// number of blocks, ending at a new intersection.

// There's no time to follow such ridiculous instructions on foot, though, so
// you take a moment and work out the destination. Given that you can only
// walk on the street grid of the city, how far is the shortest path to the
// destination?

// For example:

// - Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5
//   blocks away.
// - R2, R2, R2 leaves you 2 blocks due South of your starting position,
//   which is 2 blocks away.
// - R5, L5, R5, R3 leaves you 12 blocks away.
// How many blocks away is Easter Bunny HQ?


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

        return this.Manhattan(p);

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

    private Manhattan(p: Position): number {
        return Math.abs(p.x) + Math.abs(p.y);
    }

    LoadLines():string {
        let filename = path.join(__dirname,'../../day01.txt');
        let lines = fs.readFileSync(filename, 'utf8').trim();

        return lines;
    }
}