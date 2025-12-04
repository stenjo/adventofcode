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
