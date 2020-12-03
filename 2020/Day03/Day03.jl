# module Day03
# export part1, part2
# Day 2 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/2
# 

using DelimitedFiles
# include("utils.jl")

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

inputdata = readdlm("input.txt", '\t', String, '\n')

function Slope(right::Int64, down::Int64, inputList::Array)
    trees = 0
    pos = 1
    line = 1
    while line <= count(i->(true), inputList)
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


function partOne(list)
    return Slope(3,1,list)
end

function partTwo(list)
    return prod([Slope(1,1,list),Slope(3,1,list),Slope(5,1,list),Slope(7,1,list),Slope(1,2,list)])
end


println(partOne(inputdata))
println(partTwo(inputdata))

# end # module