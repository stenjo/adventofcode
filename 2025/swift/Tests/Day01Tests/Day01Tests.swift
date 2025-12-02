import AdventCore
import Foundation
import Testing

@testable import Day01

@Suite("Day 01 Tests")
struct Day01Tests {

    let sampleInput = """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
        """
    @Test("Turn dial")
    func testTurnDial() async throws {
        var dial = Dial()  // Initialize the dial variable
        dial = dial.turn(instruction: "L68")
        #expect(dial.code == (82))
        dial = dial.turn(instruction: "R48")
        #expect(dial.code == (30))
        dial = dial.turn(instruction: "L5")
        #expect(dial.code == (25))
        dial = dial.turn(instruction: "R60")
        #expect(dial.code == (85))
    }

    @Test("passing zero increments count")
    func testPassingZero() async throws {
        var dial = Dial()
        dial = dial.turn(instruction: "L600")  // 50
        #expect(dial.zero == 6)
        #expect(dial.code == 50)
        dial = dial.turn(instruction: "L250")  // 0
        #expect(dial.zero == 9)
        #expect(dial.code == 0)
        dial = dial.turn(instruction: "R1500")  // 0
        #expect(dial.zero == 24)
        #expect(dial.code == 0)
        dial = dial.turn(instruction: "R75")  // 75
        #expect(dial.zero == 24)
        #expect(dial.code == 75)
        dial = dial.turn(instruction: "R25")  // 0
        #expect(dial.zero == 25)
        #expect(dial.code == 0)
    }

    @Test func passingZero() async throws {
        var dial = Dial()
        dial = dial.turn(instruction: "L55")  // 95
        #expect(dial.zero == 1)
        dial = dial.turn(instruction: "L1")  // 94
        #expect(dial.zero == 1)
        dial = dial.turn(instruction: "L99")  // 95
        #expect(dial.zero == 2)
        dial = dial.turn(instruction: "R14")  // 09
        #expect(dial.zero == 3)
        dial = dial.turn(instruction: "R82")  // 91
        #expect(dial.zero == 3)
        dial = dial.turn(instruction: "R155")  // 46
        #expect(dial.zero == 5)
        dial = dial.turn(instruction: "L200")  // 46
        #expect(dial.zero == 7)
        dial = dial.turn(instruction: "R250")  // 96
        #expect(dial.zero == 9)
        dial = dial.turn(instruction: "L96")  // 96
        #expect(dial.zero == 10)
    }

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
        #expect(result == 6)
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
