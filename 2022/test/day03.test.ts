

import {Rucksack} from '../src/day03'

describe('Rucksack should', () => {
    it('have test run', () => {
        let r = new Rucksack()

        expect(r).not.toBeNull()
    })

    it('find p as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('vJrwpWtwJgWrhcsFMMfFFhFp')

        expect(item).toBe('p');
    })
    it('find L as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')

        expect(item).toBe('L');
    })
    it('find P as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('PmmdzqPrVvPwwTWBwg')

        expect(item).toBe('P');
    })
    it('find v as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')

        expect(item).toBe('v');
    })
    it('find t as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('ttgJtRGJQctTZtZT')

        expect(item).toBe('t');
    })
    it('find s as common item', () => {
        let r = new Rucksack()
        let item = r.getCommonItem('CrZsJsPPZsGzwwsLwLmpwMDw')

        expect(item).toBe('s');
    })

    it('get 16 as priority from p', () => {
        let r = new Rucksack()

        expect(r.getPriority('p')).toBe(16);
    })
    it('get 38 as priority from L', () => {
        let r = new Rucksack()

        expect(r.getPriority('L')).toBe(38);
    })
    it('get 42 as priority from P', () => {
        let r = new Rucksack()

        expect(r.getPriority('P')).toBe(42);
    })
    it('get priority sum from data', () => {
        let r = new Rucksack()
        r.load('../test/input/day03.txt');

        expect(r.getPrioritySum()).toBe(157);
    })
    it('get priority sum from real data', () => {
        let r = new Rucksack()
        r.load('../input/day03.txt');

        expect(r.getPrioritySum()).toBe(7821);
    })

    it('get r as common of thre', () => {
        let r = new Rucksack()
        const items: string[] = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]
        expect(r.getCommonOfThree(items)).toBe('r');
    })
    it('get Z as common of thre', () => {
        let r = new Rucksack()
        const items: string[] = [
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw'
        ]
        expect(r.getCommonOfThree(items)).toBe('Z');
    })
    it('get group priority sum from data', () => {
        let r = new Rucksack()
        r.load('../test/input/day03.txt');

        expect(r.getGroupPrioritySum()).toBe(70);
    })
    it('get group priority sum from real data', () => {
        let r = new Rucksack()
        r.load('../input/day03.txt');

        expect(r.getGroupPrioritySum()).toBe(2752);
    })

})