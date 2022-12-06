import {Communicator, FileInput} from '../src/day06'

describe('Communicator should', () => {
    it('have test running', () => {
        let a = new Communicator();

        expect(a).not.toBeNull();
    })

    it('find start of packet marker at 5 ', () => {
        let a = new Communicator();
        let start = a.FindPacketMarker('bvwbjplbgvbhsrlpgdmjqwftvncz')

        expect(start).toBe(5);
    })
    it('identify start of packet marker to be false ', () => {
        let a = new Communicator();
        let valid = a.startOfPacket('bvwb'.split(''))

        expect(valid).toBe(false);
    })
    it('identify start of packet marker to be true ', () => {
        let a = new Communicator();
        let valid = a.startOfPacket('vwbj'.split(''))

        expect(valid).toBe(true);
    })
    it('find start of packet marker at 7 ', () => {
        let a = new Communicator();
        let start = a.FindPacketMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb')

        expect(start).toBe(7);
    })
    it('find start of packet marker at 6 ', () => {
        let a = new Communicator();
        let start = a.FindPacketMarker('nppdvjthqldpwncqszvftbrmjlhg')

        expect(start).toBe(6);
    })
    it('find start of packet marker for real data ', () => {
        let a = new Communicator();
        let data = new FileInput('../input/day06.txt').lines;
        
        let start = a.FindPacketMarker(data)

        expect(start).toBe(1909);
    })

    it('find start of message marker at 19 ', () => {
        let a = new Communicator();
        let start = a.FindMessageMarker('mjqjpqmgbljsphdztnvjfqwrcgsmlb')

        expect(start).toBe(19);
    })

    it('find start of message marker for real data ', () => {
        let a = new Communicator();
        let data = new FileInput('../input/day06.txt').lines;
        
        let start = a.FindMessageMarker(data)

        expect(start).toBe(3380);
    })


})