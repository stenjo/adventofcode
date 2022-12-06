import {Communicator, FileInput} from '../src/day06'

describe('Communicator should', () => {
    it('have test running', () => {
        let a = new Communicator();

        expect(a).not.toBeNull();
    })

    it('find start of packet marker at 5 ', () => {
        let a = new Communicator();
        let start = a.FindMarker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)

        expect(start).toBe(5);
    })
    it('identify start of packet marker to be false ', () => {
        let a = new Communicator();
        let valid = a.isValidMarker('bvwb'.split(''), 4)

        expect(valid).toBe(false);
    })
    it('identify start of packet marker to be true ', () => {
        let a = new Communicator();
        let valid = a.isValidMarker('vwbj'.split(''), 4)

        expect(valid).toBe(true);
    })
    it('find start of packet marker at 7 ', () => {
        let a = new Communicator();
        let start = a.FindMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)

        expect(start).toBe(7);
    })
    it('find start of packet marker at 6 ', () => {
        let a = new Communicator();
        let start = a.FindMarker('nppdvjthqldpwncqszvftbrmjlhg', 4)

        expect(start).toBe(6);
    })
    it('find start of packet marker for real data ', () => {
        let a = new Communicator();
        let data = new FileInput('../input/day06.txt').data;
        
        let start = a.FindMarker(data, 4)

        expect(start).toBe(1909);
    })

    it('find start of message marker at 19 ', () => {
        let a = new Communicator();
        let start = a.FindMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)

        expect(start).toBe(19);
    })

    it('find start of message marker for real data ', () => {
        let a = new Communicator();
        let data = new FileInput('../input/day06.txt').data;
        
        let start = a.FindMarker(data, 14)

        expect(start).toBe(3380);
    })


})