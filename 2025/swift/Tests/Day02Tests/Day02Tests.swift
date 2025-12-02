import Testing
import Foundation
@testable import Day02
import AdventCore

@Suite("Day02 Tests")
struct Day02Tests {
    
    let sampleInput = """
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
    1698522-1698528,446443-446449,38593856-38593862,565653-565659,
    824824821-824824827,2121212118-2121212124
    """
    
    @Test("Parse Ranges")
    func testParseRanges() async throws {
        let ranges = Day02.parseRanges(sampleInput)
        #expect(ranges.count == 11)
        #expect(ranges[0] == (11,22))
        #expect(ranges[3] == (1188511880,1188511890))
        #expect(ranges[10] == (2121212118,2121212124))
    }

    @Test("Validate id")
    func testValidateID() async throws {

        #expect(Day02.valid("12345678") == true)
        #expect(Day02.valid("11234567") == false)
        #expect(Day02.valid("01") == false)
    }
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day02.part1(sampleInput)
        // #expect(result == expectedValue)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 2) else {
            return
        }
        
        let result = Day02.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day02.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 2) else {
            return
        }
        
        let result = Day02.part2(input)
        print("Part 2 result: \(result)")
    }
}
