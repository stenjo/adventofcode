import Foundation
import AdventCore

struct Dial {
    var code = 50
    mutating func turn(instruction: String) -> Dial {
        let direction = instruction.first!
        let codeString = instruction.dropFirst()
        guard let dial = Int(codeString) else {
            fatalError("Invalid instruction: \(instruction)")
        }
        
        var nextCode: Int

        switch direction {
        case "L":
            nextCode = (code - dial)
        case "R":
            nextCode  = (code + dial)
        default:
            fatalError("Invalid direction: \(direction)")
        }

        var zeroPassed = 0
        while (nextCode < 0) {
            nextCode += 100
            zeroPassed += 1
        }
        zeroPassed += nextCode / 100
        code = nextCode % 100
        zero += zeroPassed

        return self
    }
    var zero: Int  = 0
}

struct Day01 {
    static func part1(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        var zeroCount = 0
        var dial = Dial()
        for line in lines {
            dial = dial.turn(instruction: line)
            if dial.code == 0 {
                zeroCount += 1
            }
        }   
        return zeroCount
    }
    
    static func part2(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        var dial = Dial()
        for line in lines {
            dial = dial.turn(instruction: line)
        }   
        return dial.zero
    }
}

@main
struct Main {
    static func main() {
        do {
            let input = try FileReader.readInput(day: 1)
            
            let result1 = Benchmark.measure("Part 1") {
                Day01.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day01.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
