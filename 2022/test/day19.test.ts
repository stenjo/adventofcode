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

        expect(b.ore.oreCost).toBe(4)
        expect(b.clay.oreCost).toBe(2)
        expect(b.obsidian.oreCost).toBe(3)
        expect(b.obsidian.clayCost).toBe(14)
        expect(b.geode.oreCost).toBe(2)
        expect(b.geode.obsidianCost).toBe(7)
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
    it('run blueprint 7 minute to get 1 ore and 6 clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(7)

        expect(b.ore.count).toBe(1)
        expect(b.clay.robots).toBe(3)
        expect(b.clay.count).toBe(6)
    })
    it('run blueprint 8 minute to get two ore and 9 clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(8)

        expect(b.ore.count).toBe(2)
        expect(b.clay.robots).toBe(3)
        expect(b.clay.count).toBe(9)
    })
    it('run blueprint 9 minute to get 3 ore and 12 clay', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(9)

        expect(b.ore.count).toBe(3)
        expect(b.clay.robots).toBe(3)
        expect(b.clay.count).toBe(12)
    })
    it('run blueprint 11 minute to get 2 ore, 4 clay and 1 obsidian', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(11)

        expect(b.ore.count).toBe(2)
        expect(b.clay.robots).toBe(3)
        expect(b.clay.count).toBe(4)
        expect(b.obsidian.robots).toBe(1)
    })
    it('run blueprint 18 minute to get 2 ore, 17 clay, 3 obsidian and 1 geode', () => {
        const def = 'Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.'

        let b = new Blueprint(def);

        b.Run(18)

        expect(b.ore.count).toBe(2)
        expect(b.clay.robots).toBe(4)
        expect(b.clay.count).toBe(17)
        expect(b.obsidian.robots).toBe(2)
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