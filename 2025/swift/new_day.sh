#!/bin/bash

# Script to create a new day's project structure
# Usage: ./new_day.sh <day_number>

if [ -z "$1" ]; then
    echo "Usage: ./new_day.sh <day_number>"
    echo "Example: ./new_day.sh 2"
    exit 1
fi

DAY=$1
DAY_PADDED=$(printf "%02d" $DAY)
DAY_NAME="Day${DAY_PADDED}"

echo "Creating structure for ${DAY_NAME}..."

# Create directories
mkdir -p "Sources/${DAY_NAME}"
mkdir -p "Tests/${DAY_NAME}Tests"

# Create main source file
cat > "Sources/${DAY_NAME}/${DAY_NAME}.swift" << EOF
import Foundation
import AdventCore

struct ${DAY_NAME} {
    static func part1(_ input: String) -> Int {
        // TODO: Implement part 1 solution
        let lines = input.nonEmptyLines
        return 0
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
            let input = try FileReader.readInput(day: ${DAY})
            
            let result1 = Benchmark.measure("Part 1") {
                ${DAY_NAME}.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                ${DAY_NAME}.part2(input)
            }
            print("Part 2: \(result2)")
            
        } catch {
            print("Error: \(error)")
        }
    }
}
EOF

# Create test file
cat > "Tests/${DAY_NAME}Tests/${DAY_NAME}Tests.swift" << EOF
import Testing
import Foundation
@testable import ${DAY_NAME}
import AdventCore

@Suite("${DAY_NAME} Tests")
struct ${DAY_NAME}Tests {
    
    let sampleInput = """
    // TODO: Add sample input from problem description
    """
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = ${DAY_NAME}.part1(sampleInput)
        // #expect(result == expectedValue)
        print("Part 1 sample result: \(result)")
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: ${DAY}) else {
            return
        }
        
        let result = ${DAY_NAME}.part1(input)
        print("Part 1 result: \(result)")
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = ${DAY_NAME}.part2(sampleInput)
        // #expect(result == expectedValue)
        print("Part 2 sample result: \(result)")
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: ${DAY}) else {
            return
        }
        
        let result = ${DAY_NAME}.part2(input)
        print("Part 2 result: \(result)")
    }
}
EOF

echo "✅ Created files:"
echo "   - Sources/${DAY_NAME}/${DAY_NAME}.swift"
echo "   - Tests/${DAY_NAME}Tests/${DAY_NAME}Tests.swift"
echo ""
echo "📝 Next steps:"
echo "   1. Add these lines to Package.swift in the products array:"
echo "      .executable(name: \"${DAY_NAME}\", targets: [\"${DAY_NAME}\"]),"
echo ""
echo "   2. Add these lines to Package.swift in the targets array:"
echo "      .executableTarget("
echo "          name: \"${DAY_NAME}\","
echo "          dependencies: [\"AdventCore\"],"
echo "          path: \"Sources/${DAY_NAME}\""
echo "      ),"
echo "      .testTarget("
echo "          name: \"${DAY_NAME}Tests\","
echo "          dependencies: [\"${DAY_NAME}\", \"AdventCore\"],"
echo "          path: \"Tests/${DAY_NAME}Tests\""
echo "      ),"
echo ""
echo "   3. Run: swift build"
echo "   4. Run: swift test --filter ${DAY_NAME}Tests"
echo "   5. Run specific day: swift run ${DAY_NAME}"

chmod +x "$0"
