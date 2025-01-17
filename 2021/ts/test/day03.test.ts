import { getMostCommonBit, getBitSlice, getMostCommonBits, getLeastCommonBit, getBinaryValue, getPowerConsumption, getLeastCommonBits, getOxygenRating, filterList, getCo2ScrubberRating} from '../src/day03';
import * as fs from 'fs';
import * as path from 'path';

describe('Determining the most common bit', () => {

    it('Should be 1 for 011110011100', () => {
        let bit = getMostCommonBit('011110011100');

        expect(bit).toBe(1);
    })

    it('Should be 0 for 010001010101', () => {
        let bit = getMostCommonBit('010001010101');

        expect(bit).toBe(0);
    })

    it('Should be 1 when equal numbers of 0 and 1', () => {
        let bit = getMostCommonBit('0101');

        expect(bit).toBe(1);
    })

    it('Most common bit in 111111110000 should be 1', () => {
        let bit = getMostCommonBit('111111110000');

        expect(bit).toBe(1);
    })

    it('Most common bit in 011101100011 should be 1', () => {
        let bit = getMostCommonBit('011101100011');

        expect(bit).toBe(1);
    })

    it('Least common bit in 011101100011 should be 1', () => {
        let bit = getLeastCommonBit('011101100011');

        expect(bit).toBe(0);
    })

    it('Most common bit in 000111100100 should be 1', () => {
        let bit = getMostCommonBit('000111100100');

        expect(bit).toBe(0);
    })

    it('Bit slice at position 3 in 000111100100 and 111111110000 should be 11', () => {
        let slice = getBitSlice(["000111100100","111111110000"], 3);

        expect(slice).toBe("11");
    })

    it('Bit slice at position 0 in 000111100100 and 111111110000 should be 01', () => {
        let slice = getBitSlice(["000111100100","111111110000"], 0);

        expect(slice).toBe("01");
    })

    test('Bit slice at position 10 in 000111100100 and 111111110000 should be 00', () => {
        let slice = getBitSlice(["000111100100","111111110000"], 10);

        expect(slice).toBe("00");
    })

    test('Bit slice at position 0 from data should be 011110011100', () => {
        let slice = getBitSlice(getLines(), 0);

        expect(slice).toBe("011110011100");
    })
    test('Bit slice at position 1 from data should be 010001010101', () => {
        let slice = getBitSlice(getLines(), 1);

        expect(slice).toBe("010001010101");
    })

    test('Bit slice at position 2 from data should be 111111110000', () => {
        let slice = getBitSlice(getLines(), 2);

        expect(slice).toBe("111111110000");
    })

    test('Most common bits in  10 in 000111100100 and 111111110000 should be 00', () => {
        let slice = getMostCommonBits(["000","111","111"]);

        expect(slice).toBe("111");
    })

    test('Most common bits in  should be 100', () => {
        let slice = getMostCommonBits(["000","101","110"]);

        expect(slice).toBe("100");
    })

    test('Binary value for 100  should be 4', () => {
        let rate = getBinaryValue("100");

        expect(rate).toBe(4);
    })

    test('Binary value for 111  should be 7', () => {
        let rate = getBinaryValue("111");

        expect(rate).toBe(7);
    })

    test('Most common bits in test data should be 10110', () => {
        let lines = getLines();
        let slice = getMostCommonBits(lines);

        expect(slice).toBe("10110");
    })


    test('Gamma rate should be 22', () => {
        let rate = getBinaryValue(getMostCommonBits(getLines()));

        expect(rate).toBe(22);
    })

    test('Epsilon rate should be 9', () => {
        let rate = getBinaryValue(getLeastCommonBits(getLines()));

        expect(rate).toBe(9);
    })

    test('Oxygen rate should be 23', () => {
        let rate = getOxygenRating(getLines());

        expect(rate).toBe(23);
    })
    
    test('Co2 Scrubber rate should be 10', () => {
        let rate = getCo2ScrubberRating(getLines());

        expect(rate).toBe(10);
    })
    
    test('filterlist should return filtered list', () => {
        let result = filterList(["000","100","011","100","111","010","000"], "01");

        expect(result.length).toBe(2);
        expect(result[0]).toBe("011");
        expect(result[1]).toBe("010");
    })

    test('Power consumption should be 198', () => {

        let result = getPowerConsumption(getLines());
        expect(result).toBe(198);
    })

})


function getLines(): string[] {
    let file = path.join(__dirname,'input/day03.txt');
    let lines = fs.readFileSync(file, 'utf8').trim().split('\n');

    return lines;
}
