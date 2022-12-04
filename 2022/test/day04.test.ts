import { Assignments} from '../src/day04'

describe('Assignments should', () => {
    it('have test running', () => {
        let a = new Assignments();

        expect(a).not.toBeNull();
    })

    it('get range from 2-4', () => {
        let a = new Assignments();

        expect(a.GetRange('2-4')).toStrictEqual([2,3,4]);
    })

    it('have no intersection', () => {
        let a = new Assignments();

        expect(a.OneContainsOther('2-4', '6-8')).toBe(false);
    })

    it('have one range contains other', () => {
        let a = new Assignments();

        expect(a.OneContainsOther('6-6', '4-8')).toBe(true);
    })

    it('have 2 pairs where one contains other', () => {
        let a = new Assignments();

        const data: string[] = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8'
        ]

        expect(a.GetContainingPairs(data)).toBe(2);
    })

    it('should get correct number of paris containing other', () => {
        let a = new Assignments();

        let data: string[] = a.GetLines('../input/day04.txt')

        expect(a.GetContainingPairs(data)).toBe(471);
    })

    it('have 4 pairs that overlap', () => {
        let a = new Assignments();

        const data: string[] = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8'
        ]

        expect(a.GetOverlappingPairs(data)).toBe(4);
    })

    it('should get correct number of paris overlapping other', () => {
        let a = new Assignments();

        let data: string[] = a.GetLines('../input/day04.txt')

        expect(a.GetOverlappingPairs(data)).toBe(888);
    })


})