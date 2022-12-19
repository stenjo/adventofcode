import { Blueprint, BlueprintHandler, LoadLines } from '../src/day19'

describe('LoadLines should', () => {
    it('load all lines', () => {
        let l = new LoadLines('../test/input/day19.txt');

        expect(l.lines.length).toBeGreaterThan(0)
    })
})

describe('Blueprint should', () => {
    it('read definition', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        expect(b.ore.cost).toBe(4)
        expect(b.clay.cost).toBe(2)
        expect(b.obsidian.cost).toBe(3)
        expect(b.geode.cost).toBe(2)
    })
    it('run blueprint 1 minute to get one ore', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(1)

        expect(b.ore.count).toBe(1)
    })
    it('run blueprint 2 minutes to get two ore', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(2)

        expect(b.ore.count).toBe(2)
    })
    it('run blueprint 3 minute to get one ore and one clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(3)

        expect(b.ore.count).toBe(1)
        expect(b.clay.robots).toBe(1)
        expect(b.clay.count).toBe(0)
    })
    it('run blueprint 4 minute to get two ore and one clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(4)

        expect(b.ore.count).toBe(2)
        expect(b.clay.robots).toBe(1)
        expect(b.clay.count).toBe(1)
    })
    it('run blueprint 5 minute to get one ore and two clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(5)

        expect(b.ore.count).toBe(1)
        expect(b.clay.robots).toBe(2)
        expect(b.clay.count).toBe(2)
    })
    it('run blueprint 6 minute to get two ore and four clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(6)

        expect(b.ore.count).toBe(2)
        expect(b.clay.robots).toBe(2)
        expect(b.clay.count).toBe(4)
    })
})

describe('BlueprintHandler should', () => {
    it('load all blueprints', () => {
        let lines = new LoadLines('../test/input/day19.txt').lines
        let bh = new BlueprintHandler(lines)

        expect(bh.blueprints.length).toBe(2)
    })
    it('load all blueprints from real data', () => {
        let lines = new LoadLines('../input/day19.txt').lines
        let bh = new BlueprintHandler(lines)

        expect(bh.blueprints.length).toBe(30)
    })
})