import Testing
import Foundation
@testable import Day03
import AdventCore

@Suite("Day03 Tests")
struct Day03Tests {
    
    let sampleInput = """
    987654321111111
    811111111111119
    234234234234278
    818181911112111
    """
    
    @Test("Get joltage")
    func testGetJoltage() async throws {
        #expect(Day03.getJoltage("987654321111111") == 98)
        #expect(Day03.getJoltage("234234234234278") == 78)
        #expect(Day03.getJoltage("811111111111119") == 89)
        #expect(Day03.getJoltage("818181911112111") == 92)
    }
    
    @Test("Sum joltage")
    func testJoltSum() async throws {
        let result = Day03.joltSum(sampleInput)
        #expect(result == 357)
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day03.part1(sampleInput)
        #expect(result == 357)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 3) else {
            return
        }
        
        let result = Day03.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day03.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 3) else {
            return
        }
        
        let result = Day03.part2(input)
        print("Part 2 result: \(result)")
    }
}
