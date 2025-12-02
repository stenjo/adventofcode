import Testing
import Foundation
@testable import Day02
import AdventCore

@Suite("Day02 Tests")
struct Day02Tests {
    
    let sampleInput = """
    11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124,010-100
    """
    
    @Test("Parse Ranges")
    func testParseRanges() async throws {
        let ranges = Day02.parseRanges(sampleInput)
        #expect(ranges.count == 12)
        #expect(ranges[0] == ("11","22"))
        #expect(ranges[3] == ("1188511880","1188511890"))
        #expect(ranges[10] == ("2121212118","2121212124"))
    }

    @Test("Validate id")
    func testValidateID() async throws {

        #expect(Day02.valid("12345678") == 0)
        #expect(Day02.valid("11234567") == 0)
        #expect(Day02.valid("01") == 0)
        #expect(Day02.valid("123123") == 123123)
    }

    @Test("Invalid count")
    func testInvalidCount() async throws {
        #expect( Day02.countInvalids(in: ("11", "22")) == [11,22]) // 11 and 22 are invalid
        #expect( Day02.countInvalids(in: ("95", "115")) == [99]) // 99
        #expect( Day02.countInvalids(in: ("998", "1012")) == [1010]) // 1010
        #expect( Day02.countInvalids(in: ("1188511880", "1188511890")) == [1188511885]) // 1188511885
        #expect( Day02.countInvalids(in: ("222220", "222224")) == [222222]) // 222222
        #expect( Day02.countInvalids(in: ("1698522", "1698528")) == []) // None
        #expect( Day02.countInvalids(in: ("446443", "446449")) == [446446]) // 446446
        #expect( Day02.countInvalids(in: ("38593856", "38593862")) == [38593859]) // 38593860
        #expect( Day02.countInvalids(in: ("565653", "565659")) == [])
        #expect( Day02.countInvalids(in: ("824824821", "824824827")) == []) // 824824824
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day02.part1(sampleInput)
        #expect(result == 1227775554)
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
