import Foundation

public struct FileReader {
    /// Read input file for a specific day
    public static func readInput(day: Int) throws -> String {
        let currentFile = URL(fileURLWithPath: #filePath)
        let projectRoot = currentFile
            .deletingLastPathComponent()  // AdventCore
            .deletingLastPathComponent()  // Sources
            .deletingLastPathComponent()  // swift
        
        let inputPath = projectRoot
            .appendingPathComponent("../data")
            .appendingPathComponent(String(format: "day%02d.txt", day))
            .standardized
        
        return try String(contentsOf: inputPath, encoding: .utf8)
            .trimmingCharacters(in: .whitespacesAndNewlines)
    }
    
    /// Read a custom file path
    public static func readFile(path: String) throws -> String {
        return try String(contentsOfFile: path, encoding: .utf8)
            .trimmingCharacters(in: .whitespacesAndNewlines)
    }
}
