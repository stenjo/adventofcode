import Testing
import Foundation
@testable import Day05
import AdventCore

@Suite("Day05 Tests")
struct Day05Tests {
    
    let sampleInput = """
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32
   """

   @Test("In range check")
    func testInRange() {
        let range = 3...7
        #expect(range.contains(3))
        #expect(range.contains(5))
        #expect(range.contains(7))
        #expect(!range.contains(2))
        #expect(!range.contains(8))
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day05.part1(sampleInput)
        #expect(result == 3)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 5) else {
            return
        }
        
        let result = Day05.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day05.part2(sampleInput)
        #expect(result == 14)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 5) else {
            return
        }
        
        let result = Day05.part2(input)
        print("Part 2 result: \(result)")
    }
}
