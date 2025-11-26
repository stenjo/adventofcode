import Foundation

public struct Benchmark {
    /// Measure execution time of a closure
    public static func measure<T>(_ label: String = "", _ closure: () throws -> T) rethrows -> T {
        let start = Date()
        let result = try closure()
        let elapsed = Date().timeIntervalSince(start)
        
        let labelText = label.isEmpty ? "" : " (\(label))"
        print("⏱️  Execution time\(labelText): \(String(format: "%.3f", elapsed * 1000))ms")
        
        return result
    }
}
