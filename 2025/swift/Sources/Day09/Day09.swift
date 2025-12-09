import Foundation
import AdventCore

struct Day09 {
    struct Tile
    {
        let x: Int
        let y: Int
        let color: Color 

        enum Color {
            case red
            case blue
        }

        func area(_ tile: Tile) -> Int {
            return abs(self.x - tile.x+1) * abs(self.y - tile.y+1)
        }
    }
    struct Floor
    {
        let tiles: [Tile]

        init(from input: String) {
            var tempTiles: [Tile] = []
            let lines = input.nonEmptyLines
            for line in lines {
                let position = line.split(separator: ",").compactMap { Int($0) }

                if position.count == 2 {
                    let tile = Tile(x: position[0], y: position[1], color: .red)
                    tempTiles.append(tile)
                }
            }
            self.tiles = tempTiles

        }


        func largestRectangle() -> Int {
            var largestArea = 0
            for i in 0..<tiles.count-1 {
                let tile = tiles[i]
                if tile.color != .red {
                    continue
                }
                var area = 0
                for j in i+1..<tiles.count {
                    if i == j {
                        continue
                    }
                    let otherTile = tiles[j]
                    area = tile.area(otherTile)
                    if area > largestArea {
                        largestArea = area
                    }
                }
            }
            return largestArea
        }

    }
    static func part1(_ input: String) -> Int {
        let floor = Floor(from: input)
        return floor.largestRectangle()
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
            let input = try FileReader.readInput(day: 9)
            
            let result1 = Benchmark.measure("Part 1") {
                Day09.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day09.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
