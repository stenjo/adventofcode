import { Comparator, LoadLines, Packet } from "../src/day13";

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day13.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
    it('get pairs', () => {
        let l = new LoadLines('../test/input/day13.txt');

        expect(l.pairs.length).toBe(8)
        expect(l.pairs[7][0].length).toBeGreaterThan(2)
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
    it('initialise a single squared packet containing a packet containing a number', () => {
        let p = new Packet('[[3]]')
        
        expect(p.packet.length).toBe(1)
        expect((p.packet[0] as Packet).packet.length).toBe(1)
        expect((p.packet[0] as Packet).packet[0]).toBe(3)
    })
    it('initialise a single squared packet containing a packet containing 3 numbers', () => {
        let p = new Packet('[[8,7,6]]')
        
        expect(p.packet.length).toBe(1)
        expect((p.packet[0] as Packet).packet.length).toBe(3)
        expect((p.packet[0] as Packet).packet[2]).toBe(6)
    })
    it('initialise a single squared packet containing a packet and a number', () => {
        let p = new Packet('[[1],4]')
        
        expect(p.packet.length).toBe(2)
        expect((p.packet[0] as Packet).packet.length).toBe(1)
        expect(p.packet[1]).toBe(4)
    })
    it('initialise a single squared packet containing a number and a packet', () => {
        let p = new Packet('[4,[1]]')
        
        expect(p.packet.length).toBe(2)
        expect((p.packet[1] as Packet).packet.length).toBe(1)
        expect(p.packet[0]).toBe(4)
    })
    it('initialise a single squared packet containing two packets', () => {
        let p = new Packet('[[1],[2,3,4]]')
        
        expect(p.packet.length).toBe(2)
        expect((p.packet[0] as Packet).packet.length).toBe(1)
        expect((p.packet[1] as Packet).packet.length).toBe(3)
        expect((p.packet[1] as Packet).packet[2]).toBe(4)
    })
    it('initialise a complex nested packet', () => {
        let p = new Packet('[1,[2,[3,[4,[5,6,7]]]],8,9]')
        
        expect(p.packet.length).toBe(4)
        expect((p.packet[1] as Packet).packet.length).toBe(2)
        expect((((p.packet[1] as Packet).packet[1] as Packet).packet[1] as Packet).packet.length).toBe(2)
        expect(p.packet[2] as number).toBe(8)
        expect(p.packet[3] as number).toBe(9)
    })
})

describe('Comparator should', () => {
    it('be created', () => {
        let c = new Comparator()

        expect(c).not.toBeNull()
    })
    it('compare high integer with low integer => "wrong"', () => {
        let c = new Comparator()
        let result = c.compare(2,1)

        expect(result).toBe('wrong')
    })
    it('compare high integer with low integer => "right"', () => {
        let c = new Comparator()
        let result = c.compare(1,2)

        expect(result).toBe('right')
    })
    it('compare equal integers => "same"', () => {
        let c = new Comparator()
        let result = c.compare(2,2)

        expect(result).toBe('same')
    })
    it('compare equal arrays => "same"', () => {
        let c = new Comparator()
        let p1 = new Packet('[2]')
        let p2 = new Packet('[2]')
        let result = c.compare(p1,p2)

        expect(result).toBe('same')
    })
    it('compare low array with high array => "right"', () => {
        let c = new Comparator()
        let p1 = new Packet('[1]')
        let p2 = new Packet('[2]')
        let result = c.compare(p1,p2)

        expect(result).toBe('right')
    })
    it('compare arrays with several integers => "right"', () => {
        let c = new Comparator()
        let p1 = new Packet('[1,1]')
        let p2 = new Packet('[1,2]')
        let result = c.compare(p1,p2)

        expect(result).toBe('right')
    })
    it('compare long arrays with several integers => "right"', () => {
        let c = new Comparator()
        let p1 = new Packet('[1,1,3,1,1]')
        let p2 = new Packet('[1,1,5,1,1]')
        let result = c.compare(p1,p2)

        expect(result).toBe('right')
    })
    it('compare empty array with longer array => "right"', () => {
        let c = new Comparator()
        let p1 = new Packet('[]')
        let p2 = new Packet('[3]')
        let result = c.compare(p1,p2)

        expect(result).toBe('right')
    })
    it('compare complex arrays => "wrong"', () => {
        let c = new Comparator()
        let p1 = new Packet('[1,[2,[3,[4,[5,6,7]]]],8,9]')
        let p2 = new Packet('[1,[2,[3,[4,[5,6,0]]]],8,9]')
        let result = c.compare(p1,p2)

        expect(result).toBe('wrong')
    })
    it('compare package pair => "wrong"', () => {
        let c = new Comparator()
        let pair:string[] = ['[1,[2,[3,[4,[5,6,7]]]],8,9]', '[1,[2,[3,[4,[5,6,0]]]],8,9]']
        let result = c.ComparePair(pair)

        expect(result).toBe('wrong')
    })
    it('get IndiceSum => 13', () => {
        let c = new Comparator()
        let pairs = new LoadLines('../test/input/day13.txt').pairs
        let result = c.IndicesSum(pairs)

        expect(result).toBe(13)
    })
    it('get IndiceSum for real data', () => {
        let c = new Comparator()
        let pairs = new LoadLines('../input/day13.txt').pairs
        let result = c.IndicesSum(pairs)

        expect(result).toBe(5938)
    })
    it('get sorted packages => 16', () => {
        let c = new Comparator()
        let packages = new LoadLines('../test/input/day13.txt').lines
        let result = c.SortPackages(packages)

        expect(result.length).toBe(16)
    })
    it('get DecodeKey => "140"', () => {
        let c = new Comparator()
        let packages = new LoadLines('../test/input/day13.txt').lines
        let result = c.DecodeKey(packages)

        expect(result).toBe(140)
    })
    it('get DecodeKey for real data', () => {
        let c = new Comparator()
        let packages = new LoadLines('../input/day13.txt').lines
        let result = c.DecodeKey(packages)

        expect(result).toBe(29025)
    })
})