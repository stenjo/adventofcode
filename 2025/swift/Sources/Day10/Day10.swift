import Foundation
import AdventCore

struct Day10 {


    struct Machine {
        var indicator: [Bool]
        let buttons: [[Int]]
        let joltage: [Int]
        let lightButtons: [[Int]]

        init(_ line: String) {
            // Parse the line to initialize the machine
            // Example line format: "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
            let parts = line.split(separator: " ")

            self.indicator = parts[0].map { ".#".contains($0) ? $0 == "#" : nil }.compactMap { $0 }
            
            // Parse buttons
            var tempButtons: [[Int]] = []
            for part in parts[1..<(parts.count - 1)] {
                let buttonString = part.trimmingCharacters(in: CharacterSet(charactersIn: "()"))
                let button = buttonString.split(separator: ",").compactMap { Int($0) }
                tempButtons.append(button)
            }
            self.buttons = tempButtons
            
            // Parse joltage
            let joltageString = parts.last!.trimmingCharacters(in: CharacterSet(charactersIn: "{}"))
            self.joltage = joltageString.split(separator: ",").compactMap { Int($0) }

            // Parse light buttons
            var tempLightButtons: [[Int]] = Array(repeating: [], count: indicator.count)
            for (index, button) in buttons.enumerated() {
                for light in button {
                    tempLightButtons[light].append(index)
                }
            }
            self.lightButtons = tempLightButtons
        }


        mutating func pressButton(_ index: Int) {
            // Logic to handle button press
            let lights = buttons[index]
            for light in lights {
                indicator[light] = !indicator[light]
            }
        }

        

        func keyPresses() -> Int {
            var bitIndicator = 0
            for (i, light) in self.indicator.enumerated() {
                if light {
                    bitIndicator |= (1 << i)
                }
            }

            var bitButtons: [Int] = []
            var resultSet: Set<Int> = []
            for button in buttons {
                var bitButton = 0
                for light in button {
                    bitButton |= (1 << light)
                }
                bitButtons.append(bitButton)
            }
                resultSet.insert(bitIndicator)
            var count = 0
            while !resultSet.contains(0) {
                var newResults: Set<Int> = []
                let resultSetCopy = resultSet
                for res in resultSetCopy {
                    for bitButton in bitButtons {
                        let newRes = res ^ bitButton
                        newResults.insert(newRes)
                    }
                }
                resultSet = newResults
                count += 1
            }

            return count
        }
    }    
    static func part1(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        var machines: [Machine] = []
        for line in lines {
            machines.append(Machine(line))
        }
        var totalPresses = 0
        for m in machines {
            totalPresses += m.keyPresses()
        }

        return totalPresses
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
            let input = try FileReader.readInput(day: 10)
            
            let result1 = Benchmark.measure("Part 1") {
                Day10.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day10.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
