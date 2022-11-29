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
    it('detect invalid ABA in "xyx[xyx]xyx"', ()=>{
        let i = new Ip( 'xyx[xyx]xyx' );

        expect(i.supportsSSL()).toBe(false)
    })
    it('detect ABA in "aaa[kek]eke"', ()=>{
        let i = new Ip( 'aaa[kek]eke' );

        expect(i.supportsSSL()).toBe(true)
    })

    it('detect ABA in "zazbz[bzb]cdb"', ()=>{
        let i = new Ip( 'zazbz[bzb]cdb' );

        expect(i.supportsSSL()).toBe(true)
    })

    it('detect ABA in "zazaza"', ()=>{
        let i = new Ip( 'zazaz' );

        expect(i.supportsSSL()).toBe(false)
    })
    it('detect ABA in "zaz[aba]aza"', ()=>{
        let i = new Ip( 'zaz[aba]aza' );

        expect(i.supportsSSL()).toBe(false)
    })

})

describe('Snooping should', () => {
    it('should return answer', () => {

        let i = new Snooping()
        expect(i.Part1()).toBe(115)
    })
    it('should return answer', () => {

        let i = new Snooping()
        expect(i.Part2()).toBe(231)
    })
})
