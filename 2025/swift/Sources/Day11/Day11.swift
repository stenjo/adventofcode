import Foundation
import AdventCore

struct Day11 {
    struct Node {
        let name: String
        var connections: [Node] = []
        var path: [String] = []
        var visitedPaths: [[String]] = []
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
        let compulsoryDevices: [String]
        var nodes = [String: Node]()
        init(_ input: String, topName: String, compulsoryDevices: [String] = []) {
            let lines = input.nonEmptyLines
            for line in lines {
                let parts = line.split(separator: ":")
                if parts.count == 2 {
                    let device = parts[0].trimmingCharacters(in: .whitespaces)
                    let connections = parts[1].split(separator: " ").map { $0.trimmingCharacters(in: .whitespaces) }
                    devices[device] = connections
                }
            }
            self.compulsoryDevices = compulsoryDevices
            var top = Node(name: topName )
            top.connections = buildConnectionTree(top: topName)

        }

        mutating func buildConnectionTree(top: String, path: [String] = []) -> [Node] {
            var newPath = path
            newPath.append(top)
            if top == "out" {
                if compulsoryDevices.allSatisfy({ newPath.contains($0) }) {
                    paths.append(newPath.joined(separator: "->"))
                }
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

        mutating func dfs(current: String, target: String, visited: inout Set<String>, path: inout [String]) {
            visited.insert(current)
            path.append(current)

            if current == target {
                if compulsoryDevices.allSatisfy({ path.contains($0) }) {
                    paths.append(path.joined(separator: "->"))
                }
            } else {
                for neighbor in devices[current] ?? [] {
                    if !visited.contains(neighbor) {
                        dfs(current: neighbor, target: target, visited: &visited, path: &path)
                    }
                }
            }

            path.removeLast()
            visited.remove(current)
        }

        mutating func buildPartTree(top: String, path: [String] = [], target: String, exclude: Set<String> = [], visited: Set<String> = []) -> ([Node], Set<String>) {
            var newPath = path
            var newVisited = visited

            newPath.append(top)
            newVisited.insert(top)
            if exclude.contains(top) {
                return ([], newVisited)
            }
            if visited.contains(top) {
                return ([], newVisited)
            }
            if top == target {

                nodes[target]?.visitedPaths.append(newPath)
                print("At target: \(target), visited paths: \(nodes[target]?.visitedPaths ?? [])")
                return ([], newVisited)
            }
            var connections: [Node] = []
            for conn in devices[top] ?? [] {
                if !newPath.contains(conn) {
                    nodes[conn] = Node(name: conn, paths: newPath + [conn])
                    let (childConnections, _) = buildPartTree(top: conn, path: newPath, target: target, exclude: exclude, visited: newVisited)
                    nodes[conn]?.connections = childConnections
                    connections.append(nodes[conn]!)
                }
            }
            return (connections, newVisited)
        }

        mutating func getPaths(from top: String, to target: String, exclude: Set<String> = []) -> [Set<String>] {

            nodes.removeAll()
            nodes[top] = Node(name: top)
            let (connections, _) = buildPartTree(top: top, target: target, exclude: exclude)
            print("Target node: \(String(describing: nodes[target]))")
            nodes[top]?.connections = connections
            return nodes[target]?.visitedPaths.map { Set($0) } ?? []
        }
    }

    static func part1(_ input: String) -> Int {
        let rack = ServerRack(input,topName: "you")
        return rack.paths.count
    }
    
    static func part2(_ input: String) -> Int {
        var rack = ServerRack(input, topName: "you")
        rack.nodes.removeAll()
        var pathsCount = [Int]()

        rack.paths.removeAll()
        var visited = Set<String>()
        var path = [String]()
        rack.dfs(current: "svr", target: "out", visited: &visited, path: &path)
        
        // let paths = rack.getPaths(from: "svr", to: "out", exclude: Set([]))
        print(rack.paths)
        // print("Paths from svr to out: \(rack.nodes["out"]?.visitedPaths ?? [])")
        pathsCount.append(rack.paths.count)

        // let (_, paths2) = rack.buildPartTree(top: "fft", target: "dac", exclude: Set(["fft", "out"]).union(paths).subtracting("fft","svr"))
        // pathsCount.append(paths2.count)

        // let (_, paths3) = rack.buildPartTree(top: "dac", target: "out", exclude: Set(["fft", "srv"]).union(paths2).union(paths))
        // pathsCount.append(paths3.count)

        print("Paths counts: \(pathsCount)")

        return pathsCount.reduce(1, *)
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
