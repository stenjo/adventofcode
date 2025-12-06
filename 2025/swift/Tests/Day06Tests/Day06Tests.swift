import Testing
import Foundation
@testable import Day06
import AdventCore

@Suite("Day06 Tests")
struct Day06Tests {
    
let sampleInput = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""
    
    @Test("Load sample inout to grid")
    func testLoadSampleInput() async throws {
        let grid = Day06.Grid(from: sampleInput)
        #expect(grid.cells.count == 4)
        #expect(grid.cells[0].count == 4)
        #expect(grid.cells[0] == ["123","328"," 51","64 "])
        #expect(grid.cells[1] == [" 45","64 ","387","23 "])
        #expect(grid.cells[2] == ["  6","98 ","215","314"])
        #expect(grid.cells[3] == ["*  ","+  ","*  ","+  "])
    }   

    @Test("Calculate problem list")
    func testCalculateList() async throws {
        let grid = Day06.Grid(from: sampleInput)
        #expect(grid.calculateList(from: ["123"," 45","  6","*"]) == 33210)
        // 328 + 64 + 98 = 490
        #expect(grid.calculateList(from: ["328","64","98","+"]) == 490)
    }
    
    @Test("Cephalopod calculation")
    func testCephalopodCalculation() async throws {
        let grid = Day06.Grid(from: sampleInput)
        // ,
        //                                      and: ["328","64","98","+"],
        // 175 * 581 * 32 = 3253600
        #expect(grid.rightmostCephalopod(from: [" 51","387","215","*  "]) == ["175","581"," 32","*  "])
        // 4 + 431 + 623 = 1058
        #expect(grid.rightmostCephalopod(from: ["64 ","23 ","314","+  "]) == ["  4","431","623","+  "])
    }
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day06.part1(sampleInput)
        #expect(result == 4277556)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 6) else {
            return
        }
        
        let result = Day06.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day06.part2(sampleInput)
        #expect(result == 3263827)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 6) else {
            return
        }
        
        let result = Day06.part2(input)
        print("Part 2 result: \(result)")
    }
}
