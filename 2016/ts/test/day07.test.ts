import {Ip, Snooping} from '../src/day07'

describe('IP should', () => {
    it('detect ABBA in "abba"', ()=>{
        let i = new Ip( 'abba' );

        expect(i.supportsTLS()).toBe(true)
    })
    it('detect invalid ABBA in "abcd[bddb]xyyx"', ()=>{
        let i = new Ip( 'abcd[bddb]xyyx' );

        expect(i.supportsTLS()).toBe(false)
    })
    it('detect invalid ABBA in "aaaa[qwer]tyui"', ()=>{
        let i = new Ip( 'aaaa[qwer]tyui' );

        expect(i.supportsTLS()).toBe(false)
    })
    it('detect ABBA in "ioxxoj[asdfgh]zxcvbn"', ()=>{
        let i = new Ip( 'ioxxoj[asdfgh]zxcvbn' );

        expect(i.supportsTLS()).toBe(true)
    })
    it('detect ABA in "aba[bab]xyz"', ()=>{
        let i = new Ip( 'aba[bab]xyz' );

        expect(i.supportsSSL()).toBe(true)
    })
})

describe('Snooping should', () => {
    it('should return answer', () => {

        let i = new Snooping()
        expect(i.Part1()).toBe(115)
    })
})
