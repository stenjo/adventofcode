import Foundation
import AdventCore

struct Day07 {

    struct Manifold {
        var grid: [[Character]]
        let rows: Int
        let cols: Int
        
        init(from input: String) {
            let lines = input.nonEmptyLines
            self.grid = lines.map { Array($0) }
            self.rows = grid.count
            self.cols = grid.first?.count ?? 0
        }
        
        // Additional methods to analyze the manifold can be added here
        mutating func tachyonPaths() -> Int {
            var splits = 0
            for row in 1..<rows {
                for col in 0..<cols {
                    let cell = grid[row][col]
                    if cell == "^" {
                        if "S|".contains(grid[row - 1][col])
                        {
                            if col > 0 {
                                grid[row][col-1] = "|" // Mark as part of tachyon path]
                            }
                            if col < cols - 1 {
                                grid[row][col+1] = "|" // Mark as part of tachyon path]
                            }
                            splits += 1
                        }
                    } else if cell == "." {
                    if  "|S".contains(grid[row - 1][col])  {
                            grid[row][col] = "|" // Mark as part of tachyon path
                        }
                    }
                }
            }
            return splits
        } 
    }

    static func part1(_ input: String) -> Int {
        var manifold = Day07.Manifold(from: input)
        let pathCount = manifold.tachyonPaths()
        return pathCount
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
            let input = try FileReader.readInput(day: 7)
            
            let result1 = Benchmark.measure("Part 1") {
                Day07.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day07.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
