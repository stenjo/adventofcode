import Testing
import Foundation
@testable import Day10
import AdventCore

@Suite("Day10 Tests")
struct Day10Tests {
    
    let sampleInput = 
"""
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


    @Test("Loading Machines")
    func testLoadingMachines() async throws {
        let lines = sampleInput.nonEmptyLines
        var machines: [Day10.Machine] = []
        for line in lines {
            machines.append(Day10.Machine(line))
        }
        #expect(machines.count == 3)
        #expect(machines[0].indicator == [false, true, true, false])
        #expect(machines[0].buttons.count == 6)
        #expect(machines[0].joltage == [3,5,4,7])
        #expect(machines[0].lightButtons[0] == [4,5])
        #expect(machines[1].indicator == [false, false, false, true, false])
        #expect(machines[1].buttons.count == 5)
        #expect(machines[1].joltage == [7,5,12,7,2])
        #expect(machines[2].indicator == [false, true, true, true, false, true])
        #expect(machines[2].buttons.count == 4)
        #expect(machines[2].joltage == [10,11,11,5,10,5])
    }   

    @Test("Button press count")
    func testButtonPressCount() async throws {
        let lines = sampleInput.nonEmptyLines
        var machines: [Day10.Machine] = []
        for line in lines {
            machines.append(Day10.Machine(line))
        }
        
        let presses1 = machines[0].keyPresses()
        #expect(presses1 == 2)
        
        let presses2 = machines[1].keyPresses()
        #expect(presses2 == 3)
        
        let presses3 = machines[2].keyPresses()
        #expect(presses3 == 2)
    }
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day10.part1(sampleInput)
        #expect(result == 7)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 10) else {
            return
        }
        
        let result = Day10.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day10.part2(sampleInput)
        #expect(result == 2)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 10) else {
            return
        }
        
        let result = Day10.part2(input)
        print("Part 2 result: \(result)")
    }
}
