# Day 1 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/1
# 
# Out of the list : [1721,979,366,299,675,1456] find the two entries that sum to 2020
# and multiply these. Should result in 514579
using DelimitedFiles
using Test
using BenchmarkTools

include("utils.jl")

test = [1721,979,366,299,675,1456]
inputdata = readdlm("input.txt", '\t', Int, '\n')



# Part 1
function partOne(list=parse.(Int, readlines("input.txt")))
    numSum = 2020
    numbers = []
    for i in list 
        # println(i)
        if numSum - i in list
            push!(numbers,numSum - i)
        end
    end
    product = multiplyArray(numbers)
end

@test partOne(test) == 514579
@test partOne() == 1007331

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(list=parse.(Int, readlines("input.txt")))
    numSum = 2020
    numbers = []
    for i in list 
        for j in list
            number = numSum - i - j
            if number in list && ! (number in numbers)
                push!(numbers, number)
            end
        end
    end
    product = multiplyArray(numbers)
end

@test partTwo(test) == 241861950
@test partTwo() == 48914340

println(string("Part two: ", partTwo())) # Answer too low
@time partTwo()

