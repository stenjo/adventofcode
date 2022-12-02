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
    it('count valid Part 2 passphrases', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.countValidPart2Phrases()).toBe(119);
    })

    it('detect anagram', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.isAnagram('iooo', 'oioo')).toBe(true);
        expect(p.isAnagram('abcde', 'ecdab')).toBe(true);
    })
    it('not detect anagram', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.isAnagram('iiii','oiii')).toBe(false);
    })

    it('detect anagram in passphrase', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.hasAnagram('abcde xyz ecdab')).toBe(true);
        expect(p.hasAnagram('oiii ioii iioi iiio')).toBe(true);
    })
    it('detect no anagram in passphrase', () => {
        let p = new Passphrase('../../data/input4.txt')

        expect(p.hasAnagram('abcde fghij')).toBe(false);
        expect(p.hasAnagram('a ab abc abd abf abj')).toBe(false);
        expect(p.hasAnagram('iiii oiii ooii oooi oooo')).toBe(false);
    })
})