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


