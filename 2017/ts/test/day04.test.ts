import {Passphrase} from '../src/day04'

describe('Passphrase should', () => {
    it('load lines', () => {
        let p = new Passphrase('../../data/input4.txt');

        expect(p.lines.length).toBeGreaterThan(0);
    })
    it('validate phrase', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.isValid('aa bb cc dd ee')).toBe(true);
        expect(p.isValid('aa bb cc dd aaa')).toBe(true);
    })

    it('validate phrase to false', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.isValid('aa bb cc dd aa')).toBe(false);
    })
    it('count valid passphrases', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.countValidPhrases()).toBe(325);
    })
})