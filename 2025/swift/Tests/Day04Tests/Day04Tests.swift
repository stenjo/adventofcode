import Testing
import Foundation
@testable import Day04
import AdventCore

@Suite("Day04 Tests")
struct Day04Tests {
    
    let sampleInput = """
    ..@@.@@@@.
    @@@.@.@.@@
    @@@@@.@.@@
    @.@@@@..@.
    @@.@@@@.@@
    .@@@@@@@.@
    .@.@.@.@@@
    @.@@@.@@@@
    .@@@@@@@@.
    @.@.@@@.@.
    """

    @Test("Countng neighbors")
    func testCountingNeighbors() async throws {
        let grid = Day04.Grid(from: sampleInput)
        #expect(grid.countNeighbors(at: Day04.Point(x: 1, y: 1), ofType: .occupied) == 6)
        #expect(grid.countNeighbors(at: Day04.Point(x: 0, y: 0), ofType: .occupied) == 2)
        #expect(grid.countNeighbors(at: Day04.Point(x: 9, y: 0), ofType: .occupied) == 3)
        #expect(grid.countNeighbors(at: Day04.Point(x: 9, y: 9), ofType: .occupied) == 2)
        #expect(grid.countNeighbors(at: Day04.Point(x: 0, y: 9), ofType: .occupied) == 1)
    }           
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day04.part1(sampleInput)
        #expect(result == 13)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 4) else {
            return
        }
        
        let result = Day04.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day04.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 4) else {
            return
        }
        
        let result = Day04.part2(input)
        print("Part 2 result: \(result)")
    }
}
