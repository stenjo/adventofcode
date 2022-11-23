
export class Taxicab {
    Blocks(instruction: string): number {
        let directionsList = instruction.split(',')
        let distance = 0;

        directionsList.forEach(direction => {
            distance += parseInt(direction.trim()[1]);
        })
        return distance;
    }
}