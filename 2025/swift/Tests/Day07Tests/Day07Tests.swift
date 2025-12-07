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

    @Test("Test timeline calculation")
    func testTimelineCalculation_0() async throws {
        var manifold = Day07.Manifold(from: 
        """
        ..S..
        ..^..
        .....
        """)
        #expect(manifold.timelines() == 2)
    }
    @Test("Test timeline calculation with splits")
    func testTimelineCalculation_1() async throws {
        var manifold = Day07.Manifold(from: 
        """
        ...S...
        ...^...
        ..^.^..
        .......
        """)
        // manifold.printGrid()
        #expect(manifold.timelines() == 4)
    }
    @Test("Test timeline calculation with splits 2")
    func testTimelineCalculation_2() async throws {
        var manifold = Day07.Manifold(from: 
        """
        ...S...
        ...^...
        ..^....
        .^.....
        """)
        // manifold.printGrid()
        #expect(manifold.timelines() == 4)
    }
    @Test("Test timeline calculation with splits 3")
    func testTimelineCalculation_3() async throws {
        var manifold = Day07.Manifold(from: 
        """
        ...S...
        ...^...
        ..^.^..
        .^...^.
        """)
        // manifold.printGrid()
        #expect(manifold.timelines() == 6)
    }
    @Test("Test timeline calculation with splits 4")
    func testTimelineCalculation_4() async throws {
        var manifold = Day07.Manifold(from: 
        """
        ...S...
        ...^...
        ..^.^..
        .......
        .^.^.^.
        """)
        let _ = manifold.tachyonPaths()
        let timelines = manifold.timelines()
        // manifold.printGrid()
        #expect(timelines == 8)

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
        #expect(result == 40)
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
