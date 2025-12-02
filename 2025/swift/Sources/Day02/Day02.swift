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
                if bounds.count == 2 {
                    let start = String(bounds[0])
                    let end = String(bounds[1])
                    ranges.append((start, end))
                }
            }
        }
        return ranges
    }

    static func substring(_ str: String, from: Int, to: Int) -> String {
        let startIndex = str.index(str.startIndex, offsetBy: from)
        let endIndex = str.index(str.startIndex, offsetBy: to)
        return String(str[startIndex..<endIndex])
    }

    static func valid(_ idString: String) -> Int {
        let length = idString.count

        guard length > 0 else {
            return 0
        }
        if idString.first == "0" {
            return 0
        }   
        
        let pos = length/2 
        let firstSubstring = substring(idString, from: 0, to: pos)
        let secondSubstring = substring(idString, from: pos, to: length)
        if firstSubstring == secondSubstring {
            return Int(idString) ?? 0
        }
        return 0
   
    }

    static func countInvalids(in range: (String, String)) -> [Int] {
        let (start, end) = range
        if start.first == "0" {
            return []
        }
        var invalidIds: [Int] = []
        for id in Int(start)!...Int(end)! {
            let validValue = valid(String(id))
            if validValue != 0 {
                invalidIds.append(validValue)
            }
        }
        return invalidIds
    }

    static func countInvalids2(in range: (String, String)) -> [Int] {
        let (start, end) = range
        if start.first == "0" {
            return []
        }
        var invalidIds: [Int] = []
        for id in Int(start)!...Int(end)! {
            let validValue = validate2(idString: String(id))
            if validValue != 0 {
                invalidIds.append(validValue)
            }
        }
        return invalidIds
    }

    static func validate2(idString: String) -> Int   {

        let length = idString.count
        guard length > 0 else {
            return 0
        }
        if idString.first == "0" {
            return 0
        }
        for pos in 1..<(length/2 + 1) {
            let substring = substring(idString, from: 0, to: pos)
            for _ in 1...((length / pos) - 1) {
                let fullString = String(repeating: substring, count: (length / pos))
                if idString == fullString {
                    return Int(idString) ?? 0
                }
            }
        }

        return 0
    }   

    static func part1(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        let ranges = parseRanges(lines.first ?? "")
        var invalidIds: [Int] = []
        for range in ranges {
            invalidIds.append(contentsOf: countInvalids(in: range))
        }   
        return invalidIds.reduce(0, +)
    }
    
    static func part2(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        let ranges = parseRanges(lines.first ?? "")
        var invalidIds: [Int] = []
        for range in ranges {
            invalidIds.append(contentsOf: countInvalids2(in: range))
        }   
        return invalidIds.reduce(0, +)
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
