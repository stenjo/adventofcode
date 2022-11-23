
export class Bathroom {
    location : number = 5;

    Move(direction: string) {
        this.location = 2;
    }

    IsAt(): number {
        return this.location;    
    }

}