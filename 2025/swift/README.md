# Advent of Code 2025 - Swift

This folder contains Swift solutions for Advent of Code 2025.

## Project Structure

```
2025/swift/
├── .vscode/          # VS Code configuration
├── Sources/          # Source code
│   └── AdventOfCode2025/
│       └── AdventOfCode2025.swift
├── Package.swift     # Swift Package Manager configuration
└── README.md        # This file
```

## Prerequisites

- Swift 6.2.1 or later (already installed ✓)
- VS Code with SourceKit-LSP extension (installed ✓)

## Building and Running

### Using VS Code Tasks

- **Build**: `Cmd+Shift+B` (or Terminal → Run Build Task)
- **Run**: `Cmd+Shift+P` → "Tasks: Run Test Task" → Swift: Run

### Using Terminal

```bash
# Build the project
swift build

# Run the program
swift run

# Clean build artifacts
swift package clean
```

## Debugging

Press `F5` to start debugging. The debugger is configured to:
1. Build the project automatically
2. Launch the executable
3. Stop at breakpoints

## Adding New Days

To add a new day's solution:

1. Create a new Swift file in `Sources/AdventOfCode2025/`
2. Add the solution code
3. Update the main file to call your solution

Example structure for a day:

```swift
import Foundation

struct Day01 {
    static func part1(_ input: String) -> Int {
        // Your solution here
        return 0
    }
    
    static func part2(_ input: String) -> Int {
        // Your solution here
        return 0
    }
}
```

## Tips

- Input files should be stored in `../data/` directory
- Use `String(contentsOfFile:)` to read input files
- The SourceKit-LSP extension provides code completion, navigation, and error checking
