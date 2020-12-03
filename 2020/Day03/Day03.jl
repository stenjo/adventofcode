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


pos(x,y,l) = x*(y-1)%l+1

function Slope(right::Int64, down::Int64, inputList::Array)
    trees = 0
    for (i,input) in enumerate(inputList[1:down:end])
        trees += input[pos(right, i, length(input))] == '#' ? 1 : 0
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
