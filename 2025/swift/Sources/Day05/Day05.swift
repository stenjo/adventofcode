import Foundation
import AdventCore

struct Day05 {

    struct Inventory {

        var ranges: [ClosedRange<Int>] = []
        var ingeredients: [Int] = []

        init (from input: String) {
            let sections = input.components(separatedBy: "\n\n")
            let rangeLines = sections[0].nonEmptyLines
            let ingredientLines = sections[1].nonEmptyLines
            
            for line in rangeLines {
                let strParts = line.trimmingCharacters(in: .whitespacesAndNewlines).split(separator: "-")
                let parts = strParts.compactMap { Int($0) }
                if parts.count == 2 {
                    let range = parts[0]...parts[1]
                    ranges.append(range)
                }
            }
            
            for line in ingredientLines {
                if let number = Int(line.trimmingCharacters(in: .whitespacesAndNewlines)) {
                    ingeredients.append(number)
                }
            }
        }

         func isIngredientFresh(_ ingredient: Int) -> Bool {
            for range in ranges {
                if range.contains(ingredient) {
                    return true
                }
            }
            return false
        }

         func freshCount() -> Int {
            var freshCount = 0
            for ingredient in ingeredients {
                if isIngredientFresh(ingredient) {
                    freshCount += 1
                }
            }
            return freshCount
        }

        func getOverlappingRanges() -> [ClosedRange<Int>] {
            var overlappingRanges: [ClosedRange<Int>] = []
            for i in 0..<ranges.count {
                for j in (i + 1)..<ranges.count {
                    if ranges[i].overlaps(ranges[j]) {
                        let lowerBound = max(ranges[i].lowerBound, ranges[j].lowerBound)
                        let upperBound = min(ranges[i].upperBound, ranges[j].upperBound)
                        overlappingRanges.append(lowerBound...upperBound)
                    }
                }
            }
            return overlappingRanges
        }

        func mergeOverlappingRanges() -> [ClosedRange<Int>] {
            let sortedRanges = ranges.sorted { $0.lowerBound < $1.lowerBound }
            var mergedRanges: [ClosedRange<Int>] = []
            
            for range in sortedRanges {
                if let last = mergedRanges.last, last.overlaps(range) || last.upperBound + 1 == range.lowerBound {
                    let newRange = last.lowerBound...max(last.upperBound, range.upperBound)
                    mergedRanges[mergedRanges.count - 1] = newRange
                } else {
                    mergedRanges.append(range)
                }
            }
            return mergedRanges
        }   

        func rangeCount(mergedRanges: [ClosedRange<Int>]) -> Int {
            var count = 0
            for range in mergedRanges {
                count += (range.upperBound - range.lowerBound + 1)
            }
            return count
        }
    }

    static func part1(_ input: String) -> Int {
        let inventory = Inventory(from: input)
        return inventory.freshCount()
    }
    
    static func part2(_ input: String) -> Int {
        let inventory = Inventory(from: input)
        let mergedRanges = inventory.mergeOverlappingRanges()
        return inventory.rangeCount(mergedRanges: mergedRanges)
    }
}

@main
struct Main {
    static func main() {
        do {
            let input = try FileReader.readInput(day: 5)
            
            let result1 = Benchmark.measure("Part 1") {
                Day05.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day05.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
