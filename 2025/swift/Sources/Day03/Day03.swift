import Foundation
import AdventCore

struct Day03 {

    static func getJoltage(_ idString: String, _ digits:Int = 2) -> Int {
        var length = idString.count
        
        guard length >= digits else {
            return Int(idString) ?? 0
        }
        var numberList = idString.map { Int(String($0)) ?? 0 }
        var joltage = 0
        var power = digits
        while power > 0 {
            length = numberList.count
            let msd = numberList[0...(length-power)].sorted().last!
            joltage += msd * Int(pow(10.0, Double(power - 1)))
            power -= 1
            let msdPos = numberList.firstIndex(of: msd) ?? 0
            numberList.removeFirst(Int(msdPos + 1))
        }
        return joltage
    }
    static func joltSum(_ input: String, _ digits:Int = 2) -> Int {
        let lines = input.nonEmptyLines
        var total = 0
        for line in lines {
            total += getJoltage(line, digits)
        }
        return total
    }
    static func part1(_ input: String) -> Int {
        // TODO: Implement part 1 solution
        return joltSum(input)
    }
    
    static func part2(_ input: String) -> Int {
        // TODO: Implement part 2 solution
        return joltSum(input, 12)
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
