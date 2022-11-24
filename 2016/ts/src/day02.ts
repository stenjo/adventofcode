
export class Bathroom {
    GetKey(arg0: string): any {

        for (let i = 0; i < arg0.length; i++) {
            this.Move(arg0[i]);
        }
        return this.IsAt();
    }
    location : number = 5;

    Move(direction: any) {
        if (direction == 'U') {
            this.location -= 3;
        }
        if (direction === 'L') {
            if (this.location > 1 && this.location !== 4 && this.location !== 7) {
                this.location -= 1;
            }
        }
        if (direction === 'R') {
            if (this.location !== 3 && this.location !== 6 && this.location !== 9) {
                this.location += 1;
            }
        }
        if (direction === 'D') {
            if (this.location < 7) {
                this.location += 3;
            }
        }
    }

    IsAt(): number {
        return this.location;    
    }

}
