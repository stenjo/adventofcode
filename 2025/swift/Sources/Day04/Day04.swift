import Foundation
import AdventCore

struct Day04 {

    struct Point: Hashable {
        let x: Int
        let y: Int
    }

    struct Grid {
        enum CellType: Character {
            case empty = "."
            case occupied = "@"
        }

        var cells: [[CellType]]
        
        init(from input: String) {
            let lines = input.nonEmptyLines
            self.cells = lines.map { line in
                line.map { char in
                    CellType(rawValue: char) ?? .empty
                }
            }
        }
        
        func countNeighbors(at point: Point, ofType type: CellType) -> Int {
            let directions = [
                (-1, -1), (0, -1), (1, -1),
                (-1, 0),          (1, 0),
                (-1, 1),  (0, 1),  (1, 1)
            ]
            
            var count = 0
            for (dx, dy) in directions {
                let newX = point.x + dx
                let newY = point.y + dy
                
                if newY >= 0 && newY < self.cells.count &&
                   newX >= 0 && newX < self.cells[newY].count &&
                   self.cells[newY][newX] == type {
                    count += 1
                }
            }
            return count
        }
    }

    var grid : Grid

    static func part1(_ input: String) -> Int {
        let grid = Grid(from: input)
        var availableCount = 0
        for y in 0..<grid.cells.count {
            for x in 0..<grid.cells[y].count {
                let point = Point(x: x, y: y)
                let occupiedNeighbors = grid.countNeighbors(at: point, ofType: .occupied)
                if occupiedNeighbors < 4 && grid.cells[y][x] != .empty {
                    availableCount += 1
                }
                // print("Point (\(x), \(y)) has \(occupiedNeighbors) occupied neighbors.")
            }
        }

        return availableCount
    }
    
    fileprivate static func getAvailable(_ x: Int, _ y: Int, _ grid: Day04.Grid)-> Bool {
        let point = Point(x: x, y: y)
        let occupiedNeighbors = grid.countNeighbors(at: point, ofType: .occupied)
        if occupiedNeighbors < 4 && grid.cells[y][x] != .empty {
            return true
        }
        return false
}

static func part2(_ input: String) -> Int {
        var grid = Grid(from: input)
        var totalRemoved = 0
        while true {
            var removed = 0
            for y in 0..<grid.cells.count {
                for x in 0..<grid.cells[y].count {
                    if getAvailable(x, y, grid) {
                        removed += 1
                        grid.cells[y][x] = .empty
                    }
                }
            }
            if removed == 0 {
                break
            }
            totalRemoved += removed
        }

        return totalRemoved
    }
}

@main
struct Main {
    static func main() {
        do {
            let input = try FileReader.readInput(day: 4)
            
            let result1 = Benchmark.measure("Part 1") {
                Day04.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day04.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
