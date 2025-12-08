import Foundation
import AdventCore

struct Day08 {
    struct Pos {
        let x: Int
        let y: Int
        let z: Int
    }
    class Box {
        let pos: Pos
        let index: Int
        var circuit: Int?
        init (x: Int, y: Int, z: Int, index: Int, circuit: Int? = nil) {
            self.pos =  Pos(x: x, y: y, z: z)
            self.index = index
            self.circuit = circuit
        }
        func distance(to other: Box) -> Double {
            let dx = other.pos.x - self.pos.x
            let dy = other.pos.y - self.pos.y
            let dz = other.pos.z - self.pos.z
            return sqrt(Double(abs(dx)*abs(dx)) + Double(abs(dy)*abs(dy)) + Double(abs(dz)*abs(dz)))
        }
        func printedPos() -> String {
            return "\(pos.x),\(pos.y),\(pos.z)"
        }
    }
    struct BoxGrid {
        let boxes: [Box]
        
        init(from input: String) {
            var tempBoxes: [Box] = []
            let lines = input.nonEmptyLines
            for line in lines {
                let position = line.split(separator: ",").compactMap { Int($0) }

                if position.count == 3 {
                    let box = Box(x: position[0], y: position[1], z: position[2], index: tempBoxes.count)
                    tempBoxes.append(box)
                }
            }
            self.boxes = tempBoxes
        }
        func getClosestBox(to box: Box) -> Box? {
            var closestBox: Box? = nil
            var closestDistance: Double = Double.greatestFiniteMagnitude
            for otherBox in boxes {
                if otherBox.index == box.index {
                    continue
                }
                let distance = box.distance(to: otherBox)
                if distance < closestDistance {
                    closestDistance = distance
                    closestBox = otherBox
                }
            }
            return closestBox
        }
        func createCircuits() -> Circuits {
            let circuits = Circuits(from: self)
            return circuits
        }
    }

    struct BoxPairs {
        var pairs: [BoxPair] = []

        mutating func addPair(box1: Box, box2: Box) {
            let distance = box1.distance(to: box2)
            let pair = BoxPair(box1: box1, box2: box2, distance: distance)
            pairs.append(pair)
        }
        mutating func sortByDistance() {
            pairs.sort { $0.distance < $1.distance }
        }
        func contains(box: Box) -> Bool {
            for pair in pairs {
                if pair.box1.index == box.index || pair.box2.index == box.index {
                    return true
                }
            }
            return false
        }
        func hasPair(_ box1: Box, _ box2: Box) -> Bool {
            for pair in pairs {
                if (pair.box1.index == box1.index && pair.box2.index == box2.index) ||
                   (pair.box1.index == box2.index && pair.box2.index == box1.index) {
                    return true
                }
            }
            return false
        }
    }

    struct BoxPair {
        let box1: Box
        let box2: Box
        let distance: Double
    }

    struct Circuits {
        var circuits: [[Int]] = []

        var circuitIndex: Int = 0
        var boxPairs = BoxPairs()
        init(from boxGrid: BoxGrid) {
            for box in boxGrid.boxes {
                let otherBox = boxGrid.getClosestBox(to: box)
                if !boxPairs.hasPair(box, otherBox!) {
                    boxPairs.addPair(box1: box, box2: otherBox!)
                }

                if boxPairs.pairs.count >= 10 {
                    break
                }

            }
            boxPairs.sortByDistance()
            print("Box pairs count: \(boxPairs.pairs.map({ ($0.box1.index, $0.box2.index) }))")
            print("Box pairs distances: \(boxPairs.pairs.map({ $0.distance }))")
            for pair in boxPairs.pairs.prefix(10) {
                if pair.box1.circuit == nil && pair.box2.circuit == nil {
                    addBoxToCircuit(box: pair.box1, circuitIndex: circuitIndex)
                    addBoxToCircuit(box: pair.box2, circuitIndex: circuitIndex)
                    circuitIndex += 1
                } else if let circuitIdx = pair.box1.circuit, pair.box2.circuit == nil {
                    addBoxToCircuit(box: pair.box2, circuitIndex: circuitIdx)
                } else if let circuitIdx = pair.box2.circuit, pair.box1.circuit == nil {
                    addBoxToCircuit(box: pair.box1, circuitIndex: circuitIdx)
                }
            }

            print("Circuit counts: \(circuits.map({ $0.count }))")
        }

        mutating func addBoxToCircuit(box: Box, circuitIndex: Int) {
            box.circuit = circuitIndex
            if circuits.count <= circuitIndex {
                circuits.append([])
            }
            circuits[circuitIndex].append(box.index)
        }

        func distanceBetween(_ box1: Box, _ box2: Box) -> Int {
            let dx = box1.pos.x - box2.pos.x
            let dy = box1.pos.y - box2.pos.y
            let dz = box1.pos.z - box2.pos.z
            return abs(dx) + abs(dy) + abs(dz)
        }

    }
    static func part1(_ input: String) -> Int {
        let boxGrid = BoxGrid(from: input)
        let circuits = boxGrid.createCircuits() 

        return circuits.circuits.reduce(1, { $0 * $1.count })
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
            let input = try FileReader.readInput(day: 8)
            
            let result1 = Benchmark.measure("Part 1") {
                Day08.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day08.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
