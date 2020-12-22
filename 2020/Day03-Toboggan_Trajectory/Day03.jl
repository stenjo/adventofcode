# Day 3 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/3
# 

using DelimitedFiles
using Test
using BenchmarkTools

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

inputdata = readlines("input.txt")


pos(x,y,l) = x*(y-1)%l+1

function Slope(inputList::Array, right::Int64, down::Int64 = 1)
    trees = 0
    for (i,input) in enumerate(inputList[1:down:end])
        trees += input[pos(right, i, length(input))] == '#' ? 1 : 0
    end
    trees
end

# Part 1
partOne(list=inputdata) = Slope(list,3,1)
@test partOne(testinput) == 7
@test partOne() == 232
println(string("Part one: ", partOne(inputdata)))
@time partOne()

# Part 2
partTwo(list=inputdata) = prod(s -> Slope(list, s...), [1,3,5,7,[1,2]])

@test partTwo(testinput) == 336
@test partTwo() == 3952291680
println(string("Part two: ", partTwo(inputdata)))
@time partTwo()