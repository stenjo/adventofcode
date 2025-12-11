import Foundation
import AdventCore

struct Day11 {
    struct Node {
        let name: String
        var connections: [Node] = []
        var path: [String] = []
        init(name: String, connections: [Node] = [], paths: [String] = []) {
            self.name = name
            self.connections = connections
            self.path = paths
        }
    }
    struct ServerRack {
        var devices: [String: [String]]=[:]
        var paths: [String]=[]
        var tree = [String: Set<String>]()
        init(_ input: String) {
            let lines = input.nonEmptyLines
            for line in lines {
                let parts = line.split(separator: ":")
                if parts.count == 2 {
                    let device = parts[0].trimmingCharacters(in: .whitespaces)
                    let connections = parts[1].split(separator: " ").map { $0.trimmingCharacters(in: .whitespaces) }
                    devices[device] = connections
                }
            }
            var top = Node(name: "you" )
            top.connections = buildConnectionTree(top: "you")

        }

        mutating func buildConnectionTree(top: String, path: [String] = []) -> [Node] {
            var newPath = path
            newPath.append(top)
            if top == "out" {
                paths.append(newPath.joined(separator: "->"))
                return []  
            }
            var connections: [Node] = []
            for conn in devices[top] ?? [] {
                if !newPath.contains(conn) {
                    var newNode = Node(name: conn, paths: newPath + [conn])
                    newNode.connections = buildConnectionTree(top: conn, path: newPath)
                    connections.append(newNode)
                }
            }
            return connections
        }

        func reachableDevices(from start: String) -> Set<String> {
            var visited: Set<String> = []
            var toVisit: [String] = [start]
            
            while !toVisit.isEmpty {
                let current = toVisit.removeLast()
                if !visited.contains(current) {
                    visited.insert(current)
                    if let neighbors = devices[current] {
                        for neighbor in neighbors {
                            toVisit.append(neighbor)
                        }
                    }
                }
            }
            return visited
        }
    }
    static func part1(_ input: String) -> Int {
        let rack = ServerRack(input)
        return rack.paths.count
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
            let input = try FileReader.readInput(day: 11)
            
            let result1 = Benchmark.measure("Part 1") {
                Day11.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day11.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
