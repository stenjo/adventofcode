import Testing
import Foundation
@testable import Day11
import AdventCore

@Suite("Day11 Tests")
struct Day11Tests {
    
    let sampleInput = 
"""
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

    let complexSampleInput =
"""
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
    

    @Test("Counting paths in sample input")
    func testCountingPathsSample() async throws {
        var rack = Day11.ServerRack(sampleInput, topName: "you")
        #expect(rack.paths.count == 5)

        rack.paths.removeAll()
        _ = rack.buildPartTree(top: "you", target: "out", exclude: [])
        #expect(rack.paths.count == 5)
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day11.part1(sampleInput)
        #expect(result == 5)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 11) else {
            return
        }
        
        let result = Day11.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day11.part2(complexSampleInput)
        #expect(result == 2)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 11) else {
            return
        }
        
        let result = Day11.part2(input)
        print("Part 2 result: \(result)")
    }
}
