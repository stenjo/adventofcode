# module Day03
# export part1, part2
# Day 2 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/2
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

@test partOne(testinput) == 7
@test partTwo(testinput) == 336


# Actual personallized data

inputdata = readdlm("input.txt", '\t', String, '\n')

function Slope(right::Int64, down::Int64, inputList::Array)
    trees = 0
    pos = 1
    line = 1
    while line <= length(inputList)
        input = inputList[line]
        if input[pos] == '#'
            trees += 1
        end
        pos += right
        pos = (pos-1) % length(input) + 1
        line += down
    end
    return trees
end

partOne(list) = Slope(3,1,list)
partTwo(list) = prod([Slope(1,1,list),Slope(3,1,list),Slope(5,1,list),Slope(7,1,list),Slope(1,2,list)])

println(string("Part one: ", partOne(inputdata)))
println(string("Part two: ", partTwo(inputdata)))

# end # module