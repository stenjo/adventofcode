import {Blizzard, LoadLines, Valley} from '../src/day24'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day24.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Blizzard should', () =>{
    it('load', () =>{
        let b = new Blizzard(0,0,'>')

        expect(b).not.toBeNull()
    })
    it('move one step right', () =>{
        let b = new Blizzard(0,0,'>')

        b.Move()

        expect(b.x).toBe(1)
    })
    it('move two steps right', () =>{
        let b = new Blizzard(0,0,'>')

        b.Move()
        b.Move()

        expect(b.x).toBe(2)
    })
    it('move three steps right and wrap around at max width of 3', () =>{
        let b = new Blizzard(0,0,'>')

        b.Move(3)
        b.Move(3)
        b.Move(3)

        expect(b.x).toBe(0)
    })
    it('move one step left and wrap around at max width of 3', () =>{
        let b = new Blizzard(0,0,'<')

        b.Move(3)

        expect(b.x).toBe(2)
    })
    it('move one step up and wrap around at max height of 3', () =>{
        let b = new Blizzard(0,0,'^')

        b.Move(3,3)

        expect(b.x).toBe(0)
        expect(b.y).toBe(2)
    })
    it('move two steps down and wrap around at max height of 2', () =>{
        let b = new Blizzard(0,0,'v')

        b.Move(3,2)
        b.Move(3,2)

        expect(b.x).toBe(0)
        expect(b.y).toBe(0)
    })
    it('get same pos', () =>{
        let b = new Blizzard(1,1,'')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(1)
        expect(p.y).toBe(1)
    })
    it('get next pos at left', () =>{
        let b = new Blizzard(1,0,'<')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(0)
        expect(p.y).toBe(0)
    })
    it('get next pos wrapping at left', () =>{
        let b = new Blizzard(0,0,'<')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(2)
        expect(p.y).toBe(0)
    })

    it('get next pos at right', () =>{
        let b = new Blizzard(1,0,'>')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(2)
        expect(p.y).toBe(0)
    })
    it('get next pos wrapping at right', () =>{
        let b = new Blizzard(2,0,'>')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(0)
        expect(p.y).toBe(0)
    })
    it('get next pos up', () =>{
        let b = new Blizzard(2,1,'^')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(2)
        expect(p.y).toBe(0)
    })

    it('get next pos wrapping at top', () =>{
        let b = new Blizzard(2,0,'^')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(2)
        expect(p.y).toBe(1)
    })

    it('get next pos wrapping at bottom', () =>{
        let b = new Blizzard(2,1,'v')

        let p = b.NextPos(3,2)

        expect(p.x).toBe(2)
        expect(p.y).toBe(0)
    })

})

describe('Valley should', () => {
    it('load', ()=>{
        let v = new Valley(['']);

        expect(v).not.toBeNull()
    })

    it('load simple map', ()=>{
        const valley = [
            '#.#####',
            '#.....#',
            '#>....#',
            '#.....#',
            '#...v.#',
            '#.....#',
            '#####.#'
        ]
        let v = new Valley(valley);

        expect(v.width).toBe(5)
        expect(v.height).toBe(5)
        expect(v.blizzards.length).toBe(2)
        expect(v.blizzards[0].dir).toBe('>')
        expect(v.blizzards[0].x).toBe(0)
        expect(v.blizzards[0].y).toBe(1)
        expect(v.blizzards[1].dir).toBe('v')
        expect(v.blizzards[1].x).toBe(3)
        expect(v.blizzards[1].y).toBe(3)
    })
})


