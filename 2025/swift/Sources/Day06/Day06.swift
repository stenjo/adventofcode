import Foundation
import AdventCore

struct Day06 {

    struct Grid {
        var cells: [[String]]
        var colWidths: [Int] = []
        init(
            from input: String
        ) {
            let lines = input.nonEmptyLines
            self.cells = lines.map { $0.split(separator: " ").map { String($0) } }
            for column in 0..<cells[0].count {
                var maxWidth = 0
                for row in cells {
                    if row[column].count > maxWidth {
                        maxWidth = row[column].count
                    }
                }
                colWidths.append(maxWidth)
            }

            for column in 0..<cells[0].count {
                let from = column > 0 ? colWidths[0...column-1].reduce(0, +) + column : 0
                var to: Int = from + colWidths[column]
                for rowIndex in 0..<cells.count {

                    let line = lines[rowIndex]
                    if line.count < to {
                        to = line.count
                    }
                    let startIndex = line.index(lines[rowIndex].startIndex, offsetBy: from)
                    let endIndex = line.index(lines[rowIndex].startIndex, offsetBy: to)
                    let cell = String(line[startIndex..<endIndex])       
                    self.cells[rowIndex][column] = String(cell)
                }
            }
        }

        func calculateList(from list: [String]) -> Int {
            let op = list[list.count - 1].trimmingCharacters(in: CharacterSet.whitespaces)
            switch op {
            case  "*":
                return list.compactMap { Int($0.trimmingCharacters(in: .whitespaces)) }.reduce(1, *)
            case  "+":
                return list.compactMap { Int($0.trimmingCharacters(in: .whitespaces)) }.reduce(0, +)
            default:
                return 0
            }
        }

        func cephalopod(for col: Int) -> Int {
            var colList: [String] = []
            for row in cells {
                colList.append(row[col])
            }
            return calculateList(from: colList)
        }

        func rightmostCephalopod(from list:[String]) -> [String] {
            var maxLength = 0
            var mutableList = list
            let op = mutableList.popLast()!

            for item in list {
                if item.count > maxLength {
                    maxLength = item.count
                }
            }
            var result: [String] = []
            for i in 0...maxLength-1 {
                let pos = maxLength - 1 - i
                result.append("")
                let lastIndex = result.count - 1
                for item in mutableList {
                    if item.count > pos {
                        let index = item.index(item.startIndex, offsetBy: pos)
                        result[lastIndex] += String(item[index])
                    }
                }
            }
            result.append(op)
            return result
        }

        func cephalopodTotal(for rows: [[String]]) -> Int {
            var total = 0
            let columns = rows[0].count
            for col in 0..<columns {
                var colList: [String] = []
                for row in rows {
                    colList.append(row[col])
                }
                let rightmost = rightmostCephalopod(from: colList)
                total += calculateList(from: rightmost)
            }
            return total
        }

        func grandTotal(for rows: [[String]]) -> Int {
            var total = 0
            let columns = rows[0].count
            for col in 0..<columns {
                var colList: [String] = []
                for row in rows {
                    colList.append(row[col])
                }
                total += calculateList(from: colList)
            }
            return total
        }
    }


    
    static func part1(_ input: String) -> Int {
        let grid = Grid(from: input)
        let total = grid.grandTotal(for: grid.cells)
        return total
    }
    
    static func part2(_ input: String) -> Int {
        let grid = Grid(from: input)
        let total = grid.cephalopodTotal(for: grid.cells)
        return total
    }
}

@main
struct Main {
    static func main() {
        do {
            let input = try FileReader.readInput(day: 6)
            
            let result1 = Benchmark.measure("Part 1") {
                Day06.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day06.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
