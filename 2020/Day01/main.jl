# Day 1 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/1
# 
# Out of the list : [1721,979,366,299,675,1456] find the two entries that sum to 2020
# and multiply these. Should result in 514579
using DelimitedFiles

test = [1721,979,366,299,675,1456]
inputdata = readdlm("Day01/input.txt", '\t', Int, '\n')

function multiplyArray(list)
    product = 1
    for i in list
        product = product * i
    end
    return product
end

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
    return product
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
    return product
end


println(partOne(inputdata))
println(partTwo(inputdata))

