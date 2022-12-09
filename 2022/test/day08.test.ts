import {LoadLines, TreeGrid} from '../src/day08'

describe('TreeGrid should', () => {
    it('load trees', () => {
        let t = new TreeGrid(['123', '456', '789'])

        expect(t.TreeAt(2,3)).toBe(8)
    })

    it('load trees from file', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeAt(4,1)).toBe(7)
        expect(t.TreeAt(5,5)).toBe(0)
    })

    it('have tree 2,2 visible from left', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleLeft(2,2)).toBe(true)
    })
    it('have tree 2,2 visible from top', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleTop(2,2)).toBe(true)
    })
    it('have tree 2,2 not visible from bottom', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleBottom(2,2)).toBe(false)
    })
    it('have tree 2,2 not visible from right', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleRight(2,2)).toBe(false)
    })
    it('have tree 3,2 visible from top and right only', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleTop(3,2)).toBe(true)
        expect(t.VisibleRight(3,2)).toBe(true)
        expect(t.VisibleBottom(3,2)).toBe(false)
        expect(t.VisibleLeft(3,2)).toBe(false)
    })
    it('have tree 4,2 not visible from any direction', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleTop(4,2)).toBe(false)
        expect(t.VisibleRight(4,2)).toBe(false)
        expect(t.VisibleBottom(4,2)).toBe(false)
        expect(t.VisibleLeft(4,2)).toBe(false)
    })
    it('have left-middle (2,3) 5 is visible, but only from the right', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.VisibleTop(2,3)).toBe(false)
        expect(t.VisibleRight(2,3)).toBe(true)
        expect(t.VisibleBottom(2,3)).toBe(false)
        expect(t.VisibleLeft(2,3)).toBe(false)
    })
    it('count visible from any direction', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.CountVisibleTops()).toBe(21)
    })
    it('count visible from any direction with real data', () => {
        let d = new LoadLines('../input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.CountVisibleTops()).toBe(1669)
    })
    it('see 1 tree looking up from left-middle (3,2) 5 (of height 3)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountUp(3,2)).toBe(1)
    })
    it('see 2 trees looking up from middle-bottom (3,4) 5 (of height 3 and 5)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountUp(3,4)).toBe(2)
    })
    it('see 1 tree looking left from left-middle (3,2) 5 (of height 5)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountLeft(3,2)).toBe(1)
    })
    it('see 1 tree looking left from right-bottom (5,5) 0 (of height 9)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountLeft(5,5)).toBe(1)
    })
    it('see 1 tree looking up from right-bottom (5,5) 0 (of height 9)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountUp(5,5)).toBe(1)
    })
    it('see 2 trees looking left from middle-bottom (3,4) 5 (of height 3 and 3)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountUp(3,4)).toBe(2)
    })
    it('see 1 tree looking up from right-bottom (5,5) 0 (of height 9)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountUp(5,5)).toBe(1)
    })
    it('see 1 tree looking right from left-middle (3,2) 5 (of height 5)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountRight(3,2)).toBe(2)
    })
    it('see 2 trees looking right from middle-bottom (3,4) 5 (of height 3 and 3)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountRight(3,4)).toBe(2)
    })
    it('see 1 tree looking right from left-middle (1,3) 6 (of height 5)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountRight(1,3)).toBe(4)
    })
    it('see 2 trees looking down from left-middle (3,2) 5 (of height 3)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountDown(3,2)).toBe(2)
    })
    it('see 1 tree looking down from middle-bottom (3,4) 5 (of height 3 and 5)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountDown(3,4)).toBe(1)
    })
    it('see 2 trees looking down from left-middle (1,3) 6 (of height 3 and 3)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountDown(1,3)).toBe(2)
    })
    it('see 3 trees looking down from right-top (5,1) 3 (of height 2, 2 and 9)', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeCountDown(5,1)).toBe(3)
    })

    it('count visible in array ', () => {
        let t = new TreeGrid([''])
        expect(t.countVisible([ 0, 9, 2, 2, 3 ])).toBe(1)
        expect(t.countVisible([ 6, 3, 3, 2 ])).toBe(3)
        expect(t.countVisible([ 6 ])).toBe(0)
        expect(t.countVisible([ 3, 4, 9 ])).toBe(1)
        expect(t.countVisible([ 3, 1, 7 ])).toBe(2)
        expect(t.countVisible([ 3, 3, 5, 6 ])).toBe(1)
        expect(t.countVisible([ 3, 2 ])).toBe(1)
    })

    it('get scenic score from left-middle (3,2) to be 4', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeScenicScore(3,2)).toBe(4)
    })
    it('get scenic score from middle-bottom (3,4) to be 8', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.TreeScenicScore(3,4)).toBe(8)
    })

    it('get best view to be 8', () => {
        let d = new LoadLines('../test/input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.MaxScenicScore()).toBe(8)
    })
    it('get best view from real data', () => {
        let d = new LoadLines('../input/day08.txt')
        let t = new TreeGrid(d.lines)

        expect(t.MaxScenicScore()).toBe(331344)
    })

})