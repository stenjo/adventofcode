import { Comparator, LoadLines, Packet } from "../src/day13";

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day13.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Packet should', ()=> {
    it('initialise empty packet', ()=> {
        let p = new Packet('')
        
        expect(p).not.toBeNull()
        expect(p.packet.length).toBe(0)
    })
    it('initialise empty single squared packet', ()=> {
        let p = new Packet('[]')
        
        expect(p).not.toBeNull()
        expect(p.packet.length).toBe(0)
    })
    it('initialise single squared packet with one number', ()=> {
        let p = new Packet('[6]')
        
        expect(p.packet.length).toBe(1)
        expect(p.packet[0]).toBe(6)
    })
    it('initialise single squared packet with two numbers', ()=> {
        let p = new Packet('[6,9]')
        
        expect(p.packet.length).toBe(2)
        expect(p.packet[0]).toBe(6)
        expect(p.packet[1]).toBe(9)
    })
    it('initialise single squared packet with 5 numbers', ()=> {
        let p = new Packet('[1,1,5,1,1]')
        
        expect(p.packet.length).toBe(5)
        expect(p.packet[4]).toBe(1)
        expect(p.packet[2]).toBe(5)
    })
    it('initialise a single squared packet containing an empty packet', () => {
        let p = new Packet('[[]]')
        
        expect(p).not.toBeNull()
        expect(p.packet.length).toBe(1)
        expect((p.packet[0] as Packet).packet.length).toBe(0)
    })
})

describe('Comparator should', () => {
    it('be created', () => {
        let c = new Comparator('','')

        expect(c).not.toBeNull()
    })
})