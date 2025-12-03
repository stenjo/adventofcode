import Foundation
import AdventCore

struct Day03 {

    static func getJoltage(_ idString: String) -> Int {
        let length = idString.count
        
        guard length >= 2 else {
            return Int(idString) ?? 0
        }
        let numberList = idString.map { Int(String($0)) ?? 0 }
        let msd = numberList[0...(length-2)].sorted().last!
        let msdPos = numberList.firstIndex(of: msd) ?? 0
        let lsd = numberList[msdPos + 1..<length].sorted().last!
        return msd * 10 + lsd
    }
    static func joltSum(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        var total = 0
        for line in lines {
            total += getJoltage(line)
        }
        return total
    }
    static func part1(_ input: String) -> Int {
        // TODO: Implement part 1 solution
        let lines = input.nonEmptyLines
        return joltSum(input)
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
            let input = try FileReader.readInput(day: 3)
            
            let result1 = Benchmark.measure("Part 1") {
                Day03.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day03.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
