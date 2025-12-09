import Testing
import Foundation
@testable import Day09
import AdventCore

@Suite("Day09 Tests")
struct Day09Tests {
    
let sampleInput = 
"""
7,1
11,1
11,7
9,7
9,5
2,5
2,3         
7,3
"""
    
    @Test("Inside Tiles")
    func testInsideTiles() async throws {
        let floor = Day09.Floor(from: sampleInput)
        floor.printFloor()
        #expect(floor.isInside(x: 5, y: 5) == true)
        #expect(floor.isInside(x: 10, y: 5) == true)
        #expect(floor.isInside(x: 1, y: 1) == false)
        #expect(floor.isInside(x: 12, y: 1) == false)
        #expect(floor.isInside(x: 7, y: 8) == false)
        #expect(floor.isInside(x: 7, y: 0) == false)
    }

    @Test("Tile area")
    func testTileArea() async throws {
        #expect(Day09.Tile(x: 2, y: 2).area(Day09.Tile(x: 1, y: 1)) == 4)
        #expect(Day09.Tile(x: 2, y: 1).area(Day09.Tile(x: 1, y: 2)) == 4)
        #expect(Day09.Tile(x: 2, y: 5).area(Day09.Tile(x: 11, y: 1)) == 50)
    }

    @Test("Get rectangle")
    func testGetRectangle() async throws {
        let floor = Day09.Floor(from: sampleInput)
        let rect1 = floor.largestRectangle()
        #expect(rect1 == 50)
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day09.part1(sampleInput)
        #expect(result == 50)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 9) else {
            return
        }
        
        let result = Day09.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day09.part2(sampleInput)
        #expect(result == 24)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 9) else {
            return
        }
        
        let result = Day09.part2(input)
        print("Part 2 result: \(result)")
    }
}
