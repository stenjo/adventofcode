import { Chamber, LoadLines, Rock } from '../src/day17'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day17.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Rock should', () => {
    it('be created', () => {
        let r = new Rock();

        expect(r).not.toBeNull()
    })
    
    it('have shape added', () => {
        const shape = [
            ' # ',
            '###',
            ' # '
        ]
        let r = new Rock(shape);

        expect(r.shape[2]).toBe(' # ')
    })
    
})

describe('Chamber should', () => {
    it('be created', () => {
        let c = new Chamber();

        expect(c).not.toBeNull()
    })
    it('have first rock', () => {
        let c = new Chamber()

        c.NewRock();

        expect(c.Rock()).toBe('####')
    })
    it('have first rock at floor', () => {
        let c = new Chamber()

        c.NewRock();

        expect(c.Line()).toBe('  #### ')
    })
    it('have first rock pushed righ', () => {
        let c = new Chamber()

        c.NewRock();
        c.PushRight();

        expect(c.Line()).toBe('   ####')
    })
    it('have first rock pushed righ again hitting wall', () => {
        let c = new Chamber()

        c.NewRock();
        c.PushRight();
        c.PushRight();

        expect(c.Line()).toBe('   ####')
    })
    it('have first rock pushed left', () => {
        let c = new Chamber()

        c.NewRock();
        c.PushLeft();

        expect(c.Line()).toBe(' ####  ')
    })
    it('have first rock pushed left until hitting wall', () => {
        let c = new Chamber()

        c.NewRock();
        c.PushLeft();
        c.PushLeft();
        c.PushLeft();

        expect(c.Line()).toBe('####   ')
    })
    it.skip('have first rock fall one unit with right jet', () => {
        let c = new Chamber()

        c.NewRock();
        c.DownWithJet('>')

        expect(c.Line()).toBe('   ####')
        expect(c.LineHeight()).toBe(2)
    })
    it.skip('have first rock fall one unit with left jet', () => {
        let c = new Chamber()

        c.NewRock();
        c.DownWithJet('<')

        expect(c.Line()).toBe(' ####  ')
        expect(c.LineHeight()).toBe(2)
    })
    it.skip('have first rock fall with left jet until floor', () => {
        let c = new Chamber()

        c.NewRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('<')
        }

        expect(c.Line()).toBe('####   ')
        expect(c.Floor()).toBe('####   ')
        expect(c.LineHeight()).toBe(0)
    })
    it.skip('have second rock fall with right jet until floor', () => {
        let c = new Chamber()

        c.NewRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('<')
        }
        c.NewRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('>')
        }

        expect(c.Line()).toBe('   ####')
        expect(c.Floor()).toBe('####   ')
        expect(c.LineHeight()).toBe(0)
    })
    it('have second rock moved right', () => {
        let c = new Chamber()
        c.NewRock(1)

        c.DownWithJet('>')

        expect(c.Line()).toBe('    #  ')
    })
    it('have second rock moved two right hitting wall', () => {
        let c = new Chamber()
        c.NewRock(1)

        c.DownWithJet('>')
        c.DownWithJet('>')

        expect(c.Line()).toBe('     # ')
    })
    it('have second rock moved three right hitting wall', () => {
        let c = new Chamber()
        c.NewRock(1)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        expect(c.Line()).toBe('     # ')
    })
    it('have second rock moved three left hitting wall', () => {
        let c = new Chamber()
        c.NewRock(1)

        c.DownWithJet('<')
        c.DownWithJet('<')
        c.DownWithJet('<')

        expect(c.Line()).toBe(' #     ')
    })
    it.skip('have height of 1 when first rock moved 3 down', () => {
        let c = new Chamber()
        c.NewRock(0)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        expect(c.Height()).toBe(1)
        expect(c.Floor()).toBe('   ####')
    })
    it.skip('have height of 3 when second rock moved 3 down on top of first', () => {
        let c = new Chamber()
        c.NewRock(0)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        c.NewRock(1)

        c.DownWithJet('<')
        c.DownWithJet('<')
        c.DownWithJet('<')

        expect(c.Height()).toBe(3)
        expect(c.Floor()).toBe(' # ####')
    })
    it.skip('have height of 2 when first rock moved 3 down on top of first', () => {
        let c = new Chamber()
        c.NewRock(0)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        c.NewRock(0)

        c.DownWithJet('<')
        c.DownWithJet('<')
        c.DownWithJet('<')

        expect(c.Height()).toBe(2)
        expect(c.Floor()).toBe('   ####')
    })
    it.skip('have height of 6 when first rock moved 3 down on top of first', () => {
        let c = new Chamber()
        c.NewRock(0)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        c.NewRock(1)

        c.DownWithJet('<')
        c.DownWithJet('<')
        c.DownWithJet('<')

        c.NewRock(2)

        c.DownWithJet('>')
        c.DownWithJet('>')
        c.DownWithJet('>')

        expect(c.Height()).toBe(4)
        expect(c.Floor()).toBe('   ####')
    })
    
    it.skip('have third rock moved down until resting', () => {
        let c = new Chamber()
        c.NewRock(1)

        c.DownWithJet('>>>>>>>>')

        expect(c.Height()).toBe(3)
        expect(c.RockResting()).toBe(true)
    })
})