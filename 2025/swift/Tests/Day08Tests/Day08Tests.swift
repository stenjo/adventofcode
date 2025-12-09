import Testing
import Foundation
@testable import Day08
import AdventCore

@Suite("Day08 Tests")
struct Day08Tests {
    
    let sampleInput = 
"""
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

    @Test("Get closest box")
    func testGetClosestBox() async throws {
        let boxGrid = Day08.BoxGrid(from: sampleInput)
        if let firstBox = boxGrid.boxes.first {
            let closestBox = boxGrid.getClosestBox(to: firstBox)
            #expect(closestBox?.printedPos() == "425,690,689")
            print("Closest box to \(firstBox.pos) is \(String(describing: closestBox?.pos))")
        }
    
    }   

    @Test("BoxPairs creation")
    func testBoxPairsCreation() async throws {
        let boxGrid = Day08.BoxGrid(from: sampleInput)
        let boxPairs = Day08.BoxPairs(boxGrid: boxGrid)
        #expect(boxPairs.pairs.count == 10)
        let pair0 = boxPairs.pairs[0]
        #expect(pair0.box1.pos.toString() == "(162,817,812)")
        #expect(pair0.box2.pos.toString() == "(425,690,689)")
        let pair1 = boxPairs.pairs[1]
        #expect(pair1.box1.pos.toString() == "(162,817,812)")
        #expect(pair1.box2.pos.toString() == "(431,825,988)")
        let pair2 = boxPairs.pairs[2]
        #expect(pair2.box1.pos.toString() == "(906,360,560)")
        #expect(pair2.box2.pos.toString() == "(805,96,715)")
        let pair3 = boxPairs.pairs[3]
        #expect(pair3.box1.pos.toString() == "(431,825,988)")
        #expect(pair3.box2.pos.toString() == "(425,690,689)")
        print("Box pairs count: \(boxPairs.pairs.count)")
        print(" 1: ", boxPairs.pairs[0].box1.toString(), boxPairs.pairs[0].box2.toString(), Int(boxPairs.pairs[0].distance))
        print(" 2: ", boxPairs.pairs[1].box1.toString(), boxPairs.pairs[1].box2.toString(), Int(boxPairs.pairs[1].distance))
        print(" 3: ", boxPairs.pairs[2].box1.toString(), boxPairs.pairs[2].box2.toString(), Int(boxPairs.pairs[2].distance))
    }

    @Test("Create circuits 10 iterations")
    func testCreateCircuits10() async throws {
        let boxGrid = Day08.BoxGrid(from: sampleInput)
        let circuits = boxGrid.createCircuits()
        #expect(circuits.circuits.count == 11)
        print("Circuits: \(circuits.circuits)")
    }
    @Test("Create circuits 3 iterations")
    func testCreateCircuits3() async throws {
        let boxGrid = Day08.BoxGrid(from: sampleInput)
        var circuits = Day08.Circuits(from: boxGrid, iterations: 3)
        circuits.circuits.sort { $0.count > $1.count }
        #expect(circuits.circuits[0].count == 3)
        #expect(circuits.circuits[1].count == 2)
        #expect(circuits.circuits[3].count == 1)
        #expect(circuits.circuits.count == 17)
        print("Circuits (3 iterations): \(circuits.circuits)")
    }

    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day08.part1(sampleInput)
        #expect(result == 40)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 8) else {
            return
        }
        
        let result = Day08.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day08.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 8) else {
            return
        }
        
        let result = Day08.part2(input)
        print("Part 2 result: \(result)")
    }
}
