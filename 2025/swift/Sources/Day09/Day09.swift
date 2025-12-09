import Foundation
import AdventCore

struct Day09 {
    struct Tile
    {
        let x: Int
        let y: Int

        func area(_ tile: Tile) -> Int {
            return (abs(self.x - tile.x)+1) * (abs(self.y - tile.y)+1)
        }
        func toString() -> String {
            return "(\(x),\(y))"
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
                    let tile = Tile(x: position[0], y: position[1])
                    tempTiles.append(tile)
                }
            }
            self.tiles = tempTiles
        }

        func get(x:Int,y:Int)-> Tile? {
            return tiles.first(where: { $0.x == x && $0.y == y })
        }

        func isInside(x:Int,y:Int) -> Bool {
            if get(x: x, y: y) != nil {
                return true
            }

            // Check surrounding tiles to see
            let q1=tiles.filter({$0.x <= x && $0.y <= y})
            let q2=tiles.filter({$0.x >= x && $0.y <= y})
            let q3=tiles.filter({$0.x <= x && $0.y >= y})
            let q4=tiles.filter({$0.x >= x && $0.y >= y})
            if 
            q1.count > 0 && q4.count > 0 && q3.count > 0 && q2.count > 0
            {
                return true
            }
            return false
        }

        func largestRectangle() -> Int {
            var largestArea = 0
            var corners: (Tile, Tile)? = nil
            for i in 0..<tiles.count-1 {
                let tile = tiles[i]
                var area = 0
                for j in i+1..<tiles.count {
                    let otherTile = tiles[j]
                    area = tile.area(otherTile)
                    if area > largestArea {
                        largestArea = area
                        corners = (tile, otherTile)
                        print("New largest area: \(largestArea) with corners \(tile.toString()) and \(otherTile.toString())")
                    }
                }
            }
            return largestArea
        }

        

        func largestAllGreens() -> Int {
            var largestArea = 0
            for i in 0..<tiles.count-1 {
                let tile = tiles[i]
                var area = 0
                for j in i+1..<tiles.count {
                    if i == j {
                        continue
                    }
                    let otherTile = tiles[j]
                    area = tile.area(otherTile)
                    if area > largestArea && allGreens(tile1: tile, tile2: otherTile) {
                        largestArea = area
                    }
                }
            }
            return largestArea
        }

        func allGreens(tile1: Tile, tile2: Tile) -> Bool {
            let minX = min(tile1.x, tile2.x)
            let maxX = max(tile1.x, tile2.x)
            let minY = min(tile1.y, tile2.y)
            let maxY = max(tile1.y, tile2.y)

            let middleX = abs(maxX - minX) / 2 + minX
            let middleY = abs(maxY - minY) / 2 + minY

            return !isInside(x: middleX, y: middleY)
        }

        func printRectangle(tile1: Tile?, tile2: Tile?) {
            if tile1 == nil || tile2 == nil {
                print("No rectangle to print")
                return
            }
            let minX = min(tile1!.x, tile2!.x)
            let maxX = max(tile1!.x, tile2!.x)
            let minY = min(tile1!.y, tile2!.y)
            let maxY = max(tile1!.y, tile2!.y)

            for y in 0...maxY+2 {
                var line = ""
                for x in 0...maxX+2 {
                    if get(x: x, y: y) != nil {
                            line += "#"
                    } else if x >= minX && x <= maxX && y >= minY && y <= maxY {
                        line += "O"
                    } else {
                        line += "."
                    }
                }
                print(line)
            }
        }

        func printFloor() {
            let maxX = tiles.map { $0.x }.max() ?? 0
            let maxY = tiles.map { $0.y }.max() ?? 0

            for y in 0...maxY+2 {
                var line = ""
                for x in 0...maxX+2 {
                    if get(x: x, y: y) != nil {
                            line += "#"
                    } else if 
                        isInside(x: x, y: y) {
                        line += "X"
                    } else {
                        line += "."
                    }
                }
                print(line)
            }
        }

    }
    static func part1(_ input: String) -> Int {
        let floor = Floor(from: input)
        return floor.largestRectangle()
    }
    
    static func part2(_ input: String) -> Int {
        let floor = Floor(from: input)
        return floor.largestAllGreens()
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
