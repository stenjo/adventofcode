# Swift Testing Framework - Quick Reference

## Structure Overview

Each day is an **independent executable** with its own:
- Source file in `Sources/DayXX/`
- Test file in `Tests/DayXXTests/`
- Entry in `Package.swift`

## Creating a New Day

### Option 1: Using the Script (Recommended)

```bash
./new_day.sh 5
```

Then follow the instructions to update `Package.swift`.

### Option 2: Manual Setup

1. Create directories:
```bash
mkdir -p Sources/Day05 Tests/Day05Tests
```

2. Create `Sources/Day05/Day05.swift` (see template below)
3. Create `Tests/Day05Tests/Day05Tests.swift` (see template below)
4. Update `Package.swift` with new product and targets

## File Templates

### Solution Template (`Sources/DayXX/DayXX.swift`)

```swift
import Foundation
import AdventCore

struct Day05 {
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
            let input = try FileReader.readInput(day: 5)
            
            let result1 = Benchmark.measure("Part 1") {
                Day05.part1(input)
            }
            print("Part 1: \(result1)")
            
            let result2 = Benchmark.measure("Part 2") {
                Day05.part2(input)
            }
            print("Part 2: \(result2)")
        } catch {
            print("Error: \(error)")
        }
    }
}
```

### Test Template (`Tests/DayXXTests/DayXXTests.swift`)

```swift
import Testing
import Foundation
@testable import Day05
import AdventCore

@Suite("Day 05 Tests")
struct Day05Tests {
    
    let sampleInput = """
    paste sample input from problem here
    """
    
    @Test("Part 1 - Sample Input")
    func testPart1Sample() async throws {
        let result = Day05.part1(sampleInput)
        #expect(result == 42)  // Update with expected value
    }
    
    @Test("Part 1 - Actual Input")
    func testPart1Actual() async throws {
        guard let input = try? FileReader.readInput(day: 5) else {
            return  // Skip if file doesn't exist
        }
        
        let result = Day05.part1(input)
        print("Part 1 result: \(result)")
        // Once you know the answer:
        // #expect(result == correctAnswer)
    }
    
    @Test("Part 2 - Sample Input")
    func testPart2Sample() async throws {
        let result = Day05.part2(sampleInput)
        #expect(result == 0)  // Update with expected value
    }
    
    @Test("Part 2 - Actual Input")
    func testPart2Actual() async throws {
        guard let input = try? FileReader.readInput(day: 5) else {
            return
        }
        
        let result = Day05.part2(input)
        print("Part 2 result: \(result)")
    }
}
```

## Package.swift Entries

Add these to `Package.swift`:

```swift
// In products array:
.executable(name: "Day05", targets: ["Day05"]),

// In targets array:
.executableTarget(
    name: "Day05",
    dependencies: ["AdventCore"],
    path: "Sources/Day05"
),
.testTarget(
    name: "Day05Tests",
    dependencies: ["Day05", "AdventCore"],
    path: "Tests/Day05Tests"
),
```

## Common Commands

```bash
# Build everything
swift build

# Run specific day
swift run Day05

# Test specific day
swift test --filter Day05Tests

# Test with verbose output
swift test --filter Day05Tests --verbose

# Run all tests
swift test

# Clean build
swift package clean
```

## AdventCore Utilities

### File Reading
```swift
// Reads ../data/day05.txt
let input = try FileReader.readInput(day: 5)
```

### String Processing
```swift
let input = "a\nb\nc"
input.lines           // ["a", "b", "c"]
input.nonEmptyLines   // Skips empty lines

"x=5 y=-10".integers  // [5, -10]
```

### Performance Measurement
```swift
let result = Benchmark.measure("Label") {
    expensiveOperation()
}
```

## Testing Best Practices

1. **Always test sample input first** - Verify logic with known answers
2. **Print actual results** - Helps debug when tests fail
3. **Add assertions after solving** - Lock in correct answers
4. **Use guards for file reading** - Tests won't fail if data missing
5. **Run tests frequently** - Catch regressions early

## VS Code Integration

- `Cmd+Shift+B` - Build all
- `F5` - Debug current file
- `Cmd+Shift+P` → "Tasks: Run Task" → Choose task

## Debugging Tips

1. Add breakpoints in VS Code
2. Use `print()` statements liberally
3. Test components separately:
```swift
@Test("Parse input")
func testParsing() async throws {
    let parsed = parseInput(sampleInput)
    #expect(parsed.count == 3)
}
```

## Project Independence

- Each day is completely independent
- No shared state between days
- Can delete/modify any day without affecting others
- All shared utilities go in `AdventCore`

## File Organization

```
Sources/
  AdventCore/        ← Shared utilities (don't touch much)
  Day01/             ← Each day is isolated
    Day01.swift
  Day02/
    Day02.swift

Tests/
  Day01Tests/        ← Each test suite is isolated
    Day01Tests.swift
  Day02Tests/
    Day02Tests.swift
```
