import { LoadLines } from '../src/day14'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day14.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})