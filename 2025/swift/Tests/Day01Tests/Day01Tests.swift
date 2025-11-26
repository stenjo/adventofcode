import Testing
import Foundation
@testable import Day01
import AdventCore

@Suite("Day 01 Tests")
struct Day01Tests {
    
    let sampleInput = """
    example line 1
    example line 2
    example line 3
    """
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day01.part1(sampleInput)
        #expect(result == 3)
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        // Skip if input file doesn't exist
        guard let input = try? FileReader.readInput(day: 1) else {
            return
        }
        
        let result = Day01.part1(input)
        // Update with expected result once you know it
        // #expect(result == expectedValue)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day01.part2(sampleInput)
        #expect(result == 0)
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        // Skip if input file doesn't exist
        guard let input = try? FileReader.readInput(day: 1) else {
            return
        }
        
        let result = Day01.part2(input)
        // Update with expected result once you know it
        // #expect(result == expectedValue)
        print("Part 2 result: \(result)")
    }
}
