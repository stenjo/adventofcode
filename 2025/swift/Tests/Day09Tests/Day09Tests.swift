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
        // #expect(result == expectedValue)
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
