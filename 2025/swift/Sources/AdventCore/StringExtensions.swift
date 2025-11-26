import Foundation

public extension String {
    /// Split string into lines
    var lines: [String] {
        self.split(separator: "\n", omittingEmptySubsequences: false)
            .map(String.init)
    }
    
    /// Split string into non-empty lines
    var nonEmptyLines: [String] {
        self.split(separator: "\n", omittingEmptySubsequences: true)
            .map(String.init)
    }
    
    /// Get all integers from the string
    var integers: [Int] {
        let pattern = "-?\\d+"
        guard let regex = try? NSRegularExpression(pattern: pattern) else {
            return []
        }
        
        let matches = regex.matches(
            in: self,
            range: NSRange(self.startIndex..., in: self)
        )
        
        return matches.compactMap { match in
            guard let range = Range(match.range, in: self) else { return nil }
            return Int(self[range])
        }
    }
}

public extension Array where Element == String {
    /// Join array of strings with newline
    var joinedByNewline: String {
        self.joined(separator: "\n")
    }
}
