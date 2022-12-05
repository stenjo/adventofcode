
describe('Testing array functions should', () => {
    it('add all numbers using reduce()', () => {
        let total = [0,1,2,3].reduce((a,b)=>{return a+b});
        expect(total).toBe(6)
    })
    it('subtract all numbers using reduceRight()', () => {
        let total = [0,1,2,6].reduceRight((a,b)=>{return a-b});
        expect(total).toBe(3)
    })
    it('add all numbers using reduce() with starting value', () => {
        let total = [0,1,2,3].reduce((a,b)=>{return a+b}, 10);
        expect(total).toBe(16)
    })

    it('find if contains element', () => {
        let found = [1,2,3,4,0].some(x => x == 3)
        expect(found).toBe(true)
    })
    it('find if not contains element', () => {
        let found = [1,2,3,4,0].some(x => x == 8)
        expect(found).toBe(false)
    })
    it('find if contains element', () => {
        let found = [1,2,3,4,2].some(x => x == 2)
        expect(found).toBe(true)
    })
    it('concatenate arrays', () => {
        let merged = [1,2,3,4,2].concat([2, 5, 8, 1, 4])
        expect(merged.length).toBe(10)
    })
    it('sort arrays ascending', () => {
        let merged = [1,2,3,4,2].concat([2, 5, 8, 1, 4]).sort()
        expect(merged.pop()).toBe(8)
    })

    it('sort arrays decending', () => {
        let merged = [1,2,3,4,2].concat([2, 5, 8, 1, 4]).sort( (a, b) => { return b - a})
        expect(merged.pop()).toBe(1)
    })
    it('filters arrays with includes', () => {
        let merged = [1,5,2,3,4,2].concat([2, 5, 8, 1, 4]).sort((a, b)=> { return b - a})
            .filter( (e, i, arr) => { return !arr.slice(0,i).includes(e)})

        expect(merged).toStrictEqual([1,2,3,4,5,8].reverse())
        expect(merged.length).toBe(6)
    })
    it('filters arrays with some', () => {
        let merged = [1,5,2,3,4,2].concat([2, 5, 8, 1, 4]).sort().reverse()
            .filter( (e, i, arr) => { return !arr.slice(0,i).some(x => x == e)})

        expect(merged).toStrictEqual([1,2,3,4,5,8].reverse())
        expect(merged.length).toBe(6)
    })
})