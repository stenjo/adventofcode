# Advent of Code 2025 - Swift

This folder contains Swift solutions for Advent of Code 2025, organized as independent projects for each day with a shared core library and comprehensive testing framework.

## Project Structure

```
2025/swift/
├── .vscode/              # VS Code configuration
│   ├── settings.json
│   ├── tasks.json       # Build, test, and run tasks
│   └── launch.json      # Debug configurations
├── Sources/
│   ├── AdventCore/      # Shared utilities
│   │   ├── FileReader.swift
│   │   ├── StringExtensions.swift
│   │   └── Benchmark.swift
│   ├── Day01/           # Day 1 solution
│   │   └── Day01.swift
│   ├── Day02/           # Day 2 solution (template)
│   └── ...              # More days
├── Tests/
│   ├── Day01Tests/      # Day 1 tests
│   │   └── Day01Tests.swift
│   ├── Day02Tests/      # Day 2 tests
│   └── ...              # More tests
├── Package.swift        # Swift Package Manager configuration
├── new_day.sh          # Script to create new day structure
└── README.md           # This file
```

## Prerequisites

- Swift 6.2.1 or later ✓
- VS Code with SourceKit-LSP extension ✓

## Quick Start

### Create a New Day

```bash
./new_day.sh 2
```

This creates:
- `Sources/Day02/Day02.swift` - Main solution file
- `Tests/Day02Tests/Day02Tests.swift` - Test file
- Instructions for updating `Package.swift`

### Build and Test

```bash
# Build everything
swift build

# Run all tests
swift test

# Run specific day's tests
swift test --filter Day01Tests

# Run a specific day's solution
swift run Day01
```

## VS Code Tasks

Use `Cmd+Shift+P` → "Tasks: Run Task":

- **Swift: Build All** - Build all targets (`Cmd+Shift+B`)
- **Swift: Test All** - Run all tests
- **Swift: Run Day** - Run a specific day (prompts for day)
- **Swift: Test Day** - Test a specific day (prompts for day)
- **Swift: Create New Day** - Create new day structure (prompts for number)
- **Swift: Clean** - Clean build artifacts

## Shared Utilities (AdventCore)

### FileReader

```swift
// Automatically reads from ../data/day01.txt
let input = try FileReader.readInput(day: 1)

// Read custom file
let data = try FileReader.readFile(path: "custom.txt")
```

### String Extensions

```swift
let input = "line1\nline2\nline3"

// Split into lines
let lines = input.lines  // ["line1", "line2", "line3"]

// Non-empty lines only
let nonEmpty = input.nonEmptyLines

// Extract all integers
"x=5, y=-10, z=20".integers  // [5, -10, 20]
```

### Benchmark

```swift
let result = Benchmark.measure("Part 1") {
    Day01.part1(input)
}
// ⏱️  Execution time (Part 1): 1.234ms
```

## Testing Framework

Each day has its own test suite using Swift Testing:

```swift
@Suite("Day 01 Tests")
struct Day01Tests {
    let sampleInput = "..."
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day01.part1(sampleInput)
        #expect(result == 42)
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        let input = try FileReader.readInput(day: 1)
        let result = Day01.part1(input)
        print("Part 1 result: \(result)")
    }
}
```

## Typical Workflow

1. **Create new day**: `./new_day.sh 2`
2. **Update Package.swift**: Add the new day to products and targets (script provides exact code)
3. **Add sample input** to test file
4. **Implement solution** in `Sources/Day0X/Day0X.swift`
5. **Run tests**: `swift test --filter Day02Tests`
6. **Debug if needed**: Press `F5` and select the day
7. **Run final solution**: `swift run Day02`

## Example Day Structure

```swift
// Sources/Day01/Day01.swift
import Foundation
import AdventCore

struct Day01 {
    static func part1(_ input: String) -> Int {
        let lines = input.nonEmptyLines
        // Your solution here
        return 0
    }
    
    static func part2(_ input: String) -> Int {
        // Your solution here
        return 0
    }
}

@main
struct Main {
    static func main() {
        do {
            let input = try FileReader.readInput(day: 1)
            
            let result1 = Benchmark.measure("Part 1") {
                Day01.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day01.part2(input)
            }
            print("Part 2: \(result2)")
        } catch {
            print("Error: \(error)")
        }
    }
}
```

## Tips

- Input files should be in `../data/day01.txt` format
- Each day is an independent executable - they don't interfere with each other
- Shared code goes in `AdventCore`
- Tests run in parallel by default
- Use `#expect()` for assertions in tests
- Benchmark automatically measures execution time
