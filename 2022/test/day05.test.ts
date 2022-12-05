import {CrateStack, CrateMover, FileInput} from '../src/day05'

describe('CrateStack should', () => {
    it('have test runnings', () => {
        let cs = new CrateStack([])
        expect(cs).not.toBeNull();
    })
    it('add crate to stack', () => {
        let cs = new CrateStack([])
        cs.AddCrate('D')

        expect(cs.Top()).toBe('D');
    })
    it('remove crate from stack', () => {
        let cs = new CrateStack([])
        cs.AddCrate('D')
        cs.AddCrate('B')

        let c = cs.RemoveCrate()

        expect(cs.Top()).toBe('D');
        expect(c).toBe('B');
    })
})

describe('CrateMover should', () => {
    it('have test runnings', () => {
        let cm = new CrateMover([]);

        expect(cm).not.toBeNull();
    })
    it('get crates from string [Z] [M] [P]', () => {
        let cm = new CrateMover([]);

        let c = cm.GetCrates('[Z] [M] [P]')

        expect(c).toStrictEqual(['Z','M','P']);
    })
    it('get crates from string     [D]    ', () => {
        let cm = new CrateMover([]);

        let c = cm.GetCrates('    [D]    ')

        expect(c).toStrictEqual([' ','D',' ']);
    })
    it('create initial stacks', () => {
        const crateList = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 '
        ]
        let cm = new CrateMover(crateList);

        expect(cm.StackCount()).toBe(3);
        expect(cm.Top(2)).toBe('D')
        expect(cm.Top(3)).toBe('P')
    })
    it('move 1 from 2 to 1', () => {
        const crateList = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 '
        ]
        let cm = new CrateMover(crateList);
        cm.DoMove('move 1 from 2 to 1')

        expect(cm.Top(1)).toBe('D')
    })
    it('move 3 from 1 to 3', () => {
        const crateList = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 '
        ]
        let cm = new CrateMover(crateList);
        cm.DoMove('move 1 from 2 to 1')
        cm.DoMove('move 3 from 1 to 3')

        expect(cm.Top(3)).toBe('Z')
    })
    it('give top string CMZ', () => {
        const crateList = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 '
        ]
        let cm = new CrateMover(crateList);
        cm.DoMove('move 1 from 2 to 1')
        cm.DoMove('move 3 from 1 to 3')
        cm.DoMove('move 2 from 2 to 1')
        cm.DoMove('move 1 from 1 to 2')

        expect(cm.TopString()).toBe('CMZ')
    })

    it('create initial stacks from input', () => {
        let inputData = new FileInput('../test/input/day05.txt')
        let cm = new CrateMover(inputData.Stacks());

        expect(cm.StackCount()).toBe(3);
        expect(cm.Top(2)).toBe('D')
        expect(cm.Top(3)).toBe('P')
    })

    it('parse test input file', () => {
        let inputData = new FileInput('../test/input/day05.txt')
        let cm = new CrateMover(inputData.Stacks());
        cm.RunCrane(inputData.Commands())

        expect(cm.TopString()).toBe('CMZ')
    })
    it('parse real input file', () => {
        let inputData = new FileInput('../input/day05.txt')
        let cm = new CrateMover(inputData.Stacks());
        cm.RunCrane(inputData.Commands())

        expect(cm.TopString()).toBe('FWNSHLDNZ')
    })

    it('move multiple 3 from 1 to 3', () => {
        const crateList = [
            '    [D]    ',
            '[N] [C]    ',
            '[Z] [M] [P]',
            ' 1   2   3 '
        ]
        let cm = new CrateMover(crateList);
        cm.DoMoveMultiple('move 1 from 2 to 1')
        cm.DoMoveMultiple('move 3 from 1 to 3')

        expect(cm.Top(3)).toBe('D')
    })

    it('parse real input file', () => {
        let inputData = new FileInput('../input/day05.txt')
        let cm = new CrateMover(inputData.Stacks());
        cm.RunCraneMultiple(inputData.Commands())

        expect(cm.TopString()).toBe('RNRGDNFQG')
    })

    it('parse Martins input file', () => {
        let inputData = new FileInput('../test/input/day05-martin.txt')
        let cm = new CrateMover(inputData.Stacks());
        cm.RunCrane(inputData.Commands())

        expect(cm.TopString()).toBe('TDCHVHJTG')
    })
})

describe('FileInput should', () => {
    it('give stacks part', () => {
        let inputData = new FileInput('../test/input/day05.txt')
        
        expect(inputData.Stacks().length).toBe(4)
    })
    it('give commands part', () => {
        let inputData = new FileInput('../test/input/day05.txt')
        
        expect(inputData.Commands().length).toBe(4)
    })
})