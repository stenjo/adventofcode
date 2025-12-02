import Foundation
import AdventCore

struct Day02 {
    static func parseRanges(_ input: String) -> [(String, String)] {
        let lines = input.nonEmptyLines
        var ranges: [(String, String)] = []
        for line in lines {
            let parts = line.split(separator: ",")
            for part in parts {
                let bounds: [String.SubSequence] = part.split(separator: "-")
                if bounds.count == 2,
                if let start = String(bounds[0]) {
                    let end = String(bounds[1])
                    ranges.append((start, end))
                }
        }
        return ranges
    }

    static func valid(_ idString: String) -> Bool {
        let length = idString.count
        guard length >= 0 else {
            return false
        }
        
        var repeated = false
        var previousChar: Character?
        if (idString.first == "0") {
            return false
        }
        for char in idString {
            if let prev = previousChar {
                if char == prev {
                    repeated = true
                }
            }
            previousChar = char
        }
        
        return !repeated
    }

    static func countInvalids(in range: (String, String)) -> Int {
        let (start, end) = range
        var invalidCount = 0
        for id in Int(start)!...Int(end)! {
            if !valid(String(id)) {
                invalidCount += 1
            }
        }
        return invalidCount
    }
    static func part1(_ input: String) -> Int {
        // TODO: Implement part 1 solution
        let lines = input.nonEmptyLines
        let ranges = parseRanges(lines.first ?? "")
        var totalInvalids = 0
        for range in ranges {
            totalInvalids += countInvalids(in: range)
        }   
        return totalInvalids
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
            let input = try FileReader.readInput(day: 2)
            
            let result1 = Benchmark.measure("Part 1") {
                Day02.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day02.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
