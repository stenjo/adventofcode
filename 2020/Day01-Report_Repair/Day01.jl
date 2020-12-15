module Day01
export part1, part2
# Day 1 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/1
# 
# Out of the list : [1721,979,366,299,675,1456] find the two entries that sum to 2020
# and multiply these. Should result in 514579
using DelimitedFiles
include("utils.jl")

test = [1721,979,366,299,675,1456]
inputdata = readdlm("input.txt", '\t', Int, '\n')

function partOne(list)
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

function partTwo(list)
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

part1(inputdata)  = partOne(inputdata)
part2(inputdata) = partTwo(inputdata)

# println(partOne(inputdata))
# println(partTwo(inputdata))

end # module