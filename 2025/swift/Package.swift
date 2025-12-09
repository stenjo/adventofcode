// swift-tools-version: 6.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "AdventOfCode2025",
    platforms: [.macOS(.v13)],
    products: [
        .library(name: "AdventCore", targets: ["AdventCore"]),
        .executable(name: "Day01", targets: ["Day01"]),
        .executable(name: "Day02", targets: ["Day02"]),
        .executable(name: "Day03", targets: ["Day03"]),
        .executable(name: "Day04", targets: ["Day04"]),
        .executable(name: "Day05", targets: ["Day05"]),
        .executable(name: "Day06", targets: ["Day06"]),
        .executable(name: "Day07", targets: ["Day07"]),
        .executable(name: "Day08", targets: ["Day08"]),
        .executable(name: "Day09", targets: ["Day09"]),
        // Add more days here as you create them
        // .executable(name: "Day02", targets: ["Day02"]),
    ],
    targets: [
        // Shared utilities and helpers
        .target(
            name: "AdventCore",
            dependencies: [],
            path: "Sources/AdventCore"
        ),
        
        // Day 01
        .executableTarget(
            name: "Day01",
            dependencies: ["AdventCore"],
            path: "Sources/Day01"
        ),
        .testTarget(
            name: "Day01Tests",
            dependencies: ["Day01", "AdventCore"],
            path: "Tests/Day01Tests"
        ),
              .executableTarget(
          name: "Day02",
          dependencies: ["AdventCore"],
          path: "Sources/Day02"
      ),
      .testTarget(
          name: "Day02Tests",
          dependencies: ["Day02", "AdventCore"],
          path: "Tests/Day02Tests"
      ),
           .executableTarget(
          name: "Day03",
          dependencies: ["AdventCore"],
          path: "Sources/Day03"
      ),
      .testTarget(
          name: "Day03Tests",
          dependencies: ["Day03", "AdventCore"],
          path: "Tests/Day03Tests"
      ),
       .executableTarget(
          name: "Day04",
          dependencies: ["AdventCore"],
          path: "Sources/Day04"
      ),
      .testTarget(
          name: "Day04Tests",
          dependencies: ["Day04", "AdventCore"],
          path: "Tests/Day04Tests"
      ),
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
      .executableTarget(
          name: "Day06",
          dependencies: ["AdventCore"],
          path: "Sources/Day06"
      ),
      .testTarget(
          name: "Day06Tests",
          dependencies: ["Day06", "AdventCore"],
          path: "Tests/Day06Tests"
      ),
           .executableTarget(
          name: "Day07",
          dependencies: ["AdventCore"],
          path: "Sources/Day07"
      ),
      .testTarget(
          name: "Day07Tests",
          dependencies: ["Day07", "AdventCore"],
          path: "Tests/Day07Tests"
      ),
      .executableTarget(
          name: "Day08",
          dependencies: ["AdventCore"],
          path: "Sources/Day08"
      ),
      .testTarget(
          name: "Day08Tests",
          dependencies: ["Day08", "AdventCore"],
          path: "Tests/Day08Tests"
      ),
      .executableTarget(
          name: "Day09",
          dependencies: ["AdventCore"],
          path: "Sources/Day09"
      ),
      .testTarget(
          name: "Day09Tests",
          dependencies: ["Day09", "AdventCore"],
          path: "Tests/Day09Tests"
      ),
        // Add more days here following the same pattern
        // Day 02
        // .executableTarget(
        //     name: "Day02",
        //     dependencies: ["AdventCore"],
        //     path: "Sources/Day02"
        // ),
        // .testTarget(
        //     name: "Day02Tests",
        //     dependencies: ["Day02", "AdventCore"],
        //     path: "Tests/Day02Tests"
        // ),
    ]
)
