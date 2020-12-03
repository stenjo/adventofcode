# Day 3 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/3
# 

using DelimitedFiles
using Test

# Test information from the puzzle
testinput = [
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

# Actual personallized data

inputdata = readdlm("input.txt", '\t', String, '\n')



function Slope(right::Int64, down::Int64, inputList::Array)
    trees = 0
    pos = 1
    for input in inputList[1:down:end]
        trees += input[pos] == '#' ? 1 : 0
        pos = (pos + right - 1) % length(input) + 1
    end
    trees
end

# Part 1
partOne(list) = Slope(3,1,list)
@test partOne(testinput) == 7
@test partOne(inputdata) == 232
println(string("Part one: ", partOne(inputdata)))

# Part 2
partTwo(list) = prod([Slope(1,1,list),Slope(3,1,list),Slope(5,1,list),Slope(7,1,list),Slope(1,2,list)])
@test partTwo(testinput) == 336
@test partTwo(inputdata) == 3952291680
println(string("Part two: ", partTwo(inputdata)))
