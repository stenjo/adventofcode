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
})

describe('Chamber should', () => {
    it('be created', () => {
        let c = new Chamber();

        expect(c).not.toBeNull()
    })
    it('have first rock', () => {
        let c = new Chamber()

        c.DropRock();

        expect(c.Rock()).toBe('####')
    })
    it('have first rock at floor', () => {
        let c = new Chamber()

        c.DropRock();

        expect(c.Line()).toBe('  #### ')
    })
    it('have first rock pushed righ', () => {
        let c = new Chamber()

        c.DropRock();
        c.PushRight();

        expect(c.Line()).toBe('   ####')
    })
    it('have first rock pushed righ again hitting wall', () => {
        let c = new Chamber()

        c.DropRock();
        c.PushRight();
        c.PushRight();

        expect(c.Line()).toBe('   ####')
    })
    it('have first rock pushed left', () => {
        let c = new Chamber()

        c.DropRock();
        c.PushLeft();

        expect(c.Line()).toBe(' ####  ')
    })
    it('have first rock pushed left until hitting wall', () => {
        let c = new Chamber()

        c.DropRock();
        c.PushLeft();
        c.PushLeft();
        c.PushLeft();

        expect(c.Line()).toBe('####   ')
    })
    it('have first rock fall one unit with right jet', () => {
        let c = new Chamber()

        c.DropRock();
        c.DownWithJet('>')

        expect(c.Line()).toBe('   ####')
        expect(c.LineHeight()).toBe(3)
    })
    it('have first rock fall one unit with left jet', () => {
        let c = new Chamber()

        c.DropRock();
        c.DownWithJet('<')

        expect(c.Line()).toBe(' ####  ')
        expect(c.LineHeight()).toBe(3)
    })
    it('have first rock fall with left jet until floor', () => {
        let c = new Chamber()

        c.DropRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('<')
        }

        expect(c.Line()).toBe('####   ')
        expect(c.Floor()).toBe('####   ')
        expect(c.LineHeight()).toBe(0)
    })
    it('have second rock fall with right jet until floor', () => {
        let c = new Chamber()

        c.DropRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('<')
        }
        c.DropRock();
        while(c.LineHeight() > 0) {
            c.DownWithJet('>')
        }

        expect(c.Line()).toBe('   ####')
        expect(c.Floor()).toBe('####   ')
        expect(c.LineHeight()).toBe(0)
    })
})