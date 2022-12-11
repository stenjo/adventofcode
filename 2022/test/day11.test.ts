import {Monkey, MonkeySim, LoadLines} from '../src/day11'

describe('Monkey should', ()=> {
    it('be created', ()=> {
        let m = new Monkey([]);

        expect(m).not.toBeNull();
    })
    it('get correct id', ()=> {
        let m = new Monkey(['Monkey 2:']);

        expect(m.id).toBe(2);
    })
    it('initialise items correctly', ()=> {
        const model = [
            'Monkey 2:',
            '  Starting items: 79, 60, 97'
        ]
        let m = new Monkey(model);

        expect(m.worries.length).toBe(3);
        expect(m.worries[0]).toBe(79)
    })
    it('initialise operations correctly', ()=> {
        const model = [
            'Monkey 2:',
            '  Starting items: 79, 60, 97',
            '  Operation: new = old * old'
        ]
        let m = new Monkey(model);

        expect(m.operation.length).toBeGreaterThan(3);
        expect(m.operation).toBe('old * old')
    })
    it('initialise divisible by correctly', ()=> {
        const model = [
            'Monkey 2:',
            '  Starting items: 79, 60, 97',
            '  Operation: new = old * old',
            '  Test: divisible by 13'
        ]
        let m = new Monkey(model);

        expect(m.divisibleBy).toBe(13)
    })
    it('initialise test outcomes correctly', ()=> {
        const model = [
            'Monkey 2:',
            '  Starting items: 79, 60, 97',
            '  Operation: new = old * old',
            '  Test: divisible by 13',
            '    If true: throw to monkey 1',
            '    If false: throw to monkey 3'
        ]
        let m = new Monkey(model);

        expect(m.throwIfTrue).toBe(1)
        expect(m.throwIfFalse).toBe(3)
    })
    
    it('inspects worry multiplies by 19, divides by 3', ()=> {
        const model = [
            'Monkey 0:',
            'Starting items: 79, 98',
            'Operation: new = old * 19',
            'Test: divisible by 23',
              'If true: throw to monkey 2',
              'If false: throw to monkey 3'
        ]
        let m = new Monkey(model);

        let result = m.RunOperation(79)

        expect(result).toBe(500)
    })
   
    it('inspects worry adds 6, divides by 3', ()=> {
        const model = [
            'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
            '  If true: throw to monkey 2',
            '  If false: throw to monkey 0'
        ]
        let m = new Monkey(model);

        let result = m.RunOperation(54)

        expect(result).toBe(20)
    })
   
    it('inspects worry multiplies by itself, divides by 3', ()=> {
        const model = [
            'Monkey 2:',
            '  Starting items: 79, 60, 97',
            '  Operation: new = old * old',
            '  Test: divisible by 13',
            '    If true: throw to monkey 1',
            '    If false: throw to monkey 3'
        ]
        let m = new Monkey(model);

        let result = m.RunOperation(79)

        expect(result).toBe(2080)
    })
   
    it('inspects worry increases by 3, divides by 3', ()=> {
        const model = [
            'Monkey 3:',
            'Starting items: 74',
            'Operation: new = old + 3',
            'Test: divisible by 17',
            '  If true: throw to monkey 0',
            '  If false: throw to monkey 1'
        ]
        let m = new Monkey(model);

        let result = m.RunOperation(74)

        expect(result).toBe(25)
    })
       
    it('tests is not divisible by 19 and throw to 0', ()=> {
        const model = [
            'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
            '  If true: throw to monkey 2',
            '  If false: throw to monkey 0'
        ]
        let m = new Monkey(model);

        let result = m.TestAndThrow(20)

        expect(result).toBe(0)
    })
   
    it('tests is divisible by 19 and throw to 2', ()=> {
        const model = [
            'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
            '  If true: throw to monkey 2',
            '  If false: throw to monkey 0'
        ]
        let m = new Monkey(model);

        let result = m.TestAndThrow(19)

        expect(result).toBe(2)
    })
   
    it('tests is not divisible by 19 and throw to 0', ()=> {
        const model = [
            'Monkey 1:',
            'Starting items: 54, 65, 75, 74',
            'Operation: new = old + 6',
            'Test: divisible by 19',
            '  If true: throw to monkey 2',
            '  If false: throw to monkey 0'
        ]
        let m = new Monkey(model);

        let result = m.TestAndThrow(0)

        expect(result).toBe(0)
    })
   
})

describe('MonkeySim should', ()=> {
    it('have simulator running', ()=> {
        let m = new MonkeySim();

        expect(m).not.toBeNull();
    })
    it('loads monkeys', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines

        m.LoadMonkeys(input)

        expect(m.monkeys.length).toBe(4)
        expect(m.monkeys[0].id).toBe(0)
        expect(m.monkeys[3].id).toBe(3)
    })

    it('inspects monkey 0 first time and throws 500 to 3', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        let result = m.Inspect(m.monkeys[0])


        expect(result).toStrictEqual({monkey:3,worry:500})
        expect(result.monkey).toBe(3)
        expect(result.worry).toBe(500)
    })
    it('inspects monkey 0 second time and throws 620 to 3', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.Inspect(m.monkeys[0])
        let result = m.Inspect(m.monkeys[0])


        expect(result).toStrictEqual({monkey:3,worry:620})
        expect(result.monkey).toBe(3)
        expect(result.worry).toBe(620)
    })
    it('inspects monkey 1 first time and throws 20 to 0', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        let result = m.Inspect(m.monkeys[1])


        expect(result).toStrictEqual({monkey:0,worry:20})
        expect(result.monkey).toBe(0)
        expect(result.worry).toBe(20)
    })
    it('inspects monkey 1 second time and throws 23 to 0', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.Inspect(m.monkeys[1])
        let result = m.Inspect(m.monkeys[1])


        expect(result).toStrictEqual({monkey:0,worry:23})
        expect(result.monkey).toBe(0)
        expect(result.worry).toBe(23)
    })
    
    it('inspects monkey 0 a full round throwing 2 worries to 3 and has inspected 2 items', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.InspectMonkey(m.monkeys[0])

        expect(m.monkeys[0].inspects).toBe(2)
        expect(m.monkeys[3].worries.length).toBe(3)
    })
    it('run first round leaving monkey 0 with 4 items', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.RunRound()

        expect(m.monkeys[0].worries.length).toBe(4)
    })

    it('run first round leaving monkey 1 with 6 items, last one 1046', ()=> {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.RunRound()

        expect(m.monkeys[1].worries.length).toBe(6)
        expect(m.monkeys[1].worries[m.monkeys[1].worries.length-1]).toBe(1046)
        expect(m.monkeys[1].inspects).toBe(4)
    })

    it('run 20 rounds leaving Monkey 0 with 101 inspects and Monkey 3 with 105', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.RunRound(20)

        expect(m.monkeys[0].inspects).toBe(101)
        expect(m.monkeys[3].inspects).toBe(105)
    })
    it('run 20 rounds and get monkeybusiness of 10605', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.RunRound(20)

        expect(m.GetMonkeyBusiness()).toBe(10605)
    })
    it('run 20 rounds and get monkeybusiness of real data', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../input/day11.txt').lines
        m.LoadMonkeys(input)

        m.RunRound(20)

        expect(m.GetMonkeyBusiness()).toBe(64032)
    })
    it('run 1 round with no releaf and get inspects for all Monkeys', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound()

        expect(m.monkeys[0].inspects).toBe(2)
        expect(m.monkeys[1].inspects).toBe(4)
        expect(m.monkeys[2].inspects).toBe(3)
        expect(m.monkeys[3].inspects).toBe(6)
    })
    it('run 20 rounds with no releaf and get inspects for all Monkeys', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(20)

        expect(m.monkeys[0].inspects).toBe(99)
        expect(m.monkeys[1].inspects).toBe(97)
        expect(m.monkeys[3].inspects).toBe(103)
        expect(m.monkeys[2].inspects).toBe(8)
    })
    it('run 1000 rounds with no releaf giving 5204 inspects for Monkey 0', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(1000)

        expect(m.monkeys[0].inspects).toBe(5204)
        expect(m.monkeys[3].inspects).toBe(5192)
    })

    it('run 2000 rounds with no releaf and get monkeybusiness of 2713310158', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(2000)

        expect(m.monkeys[0].inspects).toBe(10419)
        expect(m.monkeys[3].inspects).toBe(10391)
        expect(m.GetMonkeyBusiness()).toBe(108263829)
    })

    it('run 9000 rounds with no releaf and get monkeybusiness of 2713310158', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(9000)

        expect(m.monkeys[0].inspects).toBe(46945)
        expect(m.monkeys[3].inspects).toBe(46807)
        expect(m.GetMonkeyBusiness()).toBe(2197354615)
    })

    it('run 10000 rounds with no releaf and get monkeybusiness of 2713310158', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../test/input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(10000)

        expect(m.monkeys[0].inspects).toBe(52166)
        expect(m.monkeys[3].inspects).toBe(52013)
        expect(m.GetMonkeyBusiness()).toBe(2713310158)
    })
    it('run 10000 rounds with no releaf from real data', () => {
        let m = new MonkeySim();
        let input = new LoadLines('../input/day11.txt').lines
        m.LoadMonkeys(input)

        m.releaf = false;
        m.RunRound(10000)

        expect(m.GetMonkeyBusiness()).toBe(12729522272)
    })
})