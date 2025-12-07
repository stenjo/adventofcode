import Testing
import Foundation
@testable import Day07
import AdventCore

@Suite("Day07 Tests")
struct Day07Tests {
    
let sampleInput = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
    
    @Test("Test tachyon path calculation")
    func testTachyonPathCalculation() async throws {
        var manifold = Day07.Manifold(from: sampleInput)
        let pathCount = manifold.tachyonPaths()
        // #expect(pathCount == expectedValue)
        print("Tachyon path count: \(pathCount)")
    }
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day07.part1(sampleInput)
        #expect(result == 21)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 7) else {
            return
        }
        
        let result = Day07.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day07.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 7) else {
            return
        }
        
        let result = Day07.part2(input)
        print("Part 2 result: \(result)")
    }
}
