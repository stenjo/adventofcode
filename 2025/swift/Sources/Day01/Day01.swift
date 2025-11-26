import Foundation
import AdventCore

struct Day01 {
    static func part1(_ input: String) -> Int {
        // TODO: Implement part 1 solution
        let lines = input.nonEmptyLines
        return lines.count
    }
    
    static func part2(_ input: String) -> Int {
        // TODO: Implement part 2 solution
        return 0
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
