# Day 8 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/8
#
# using DelimitedFiles
using BenchmarkTools
using Test

function IsValidNumber(list::Vector{Int}, preamble::Int, num::Int)

    numbers = copy(list)
    while length(numbers) > 0
        n = pop!(numbers)
        for m in numbers
            if m + n == num
                return true
            end
        end
    end
    false
end
@test IsValidNumber([1721,979,366,299,675,1456], 5, 665) == true
@test IsValidNumber([1721,979,366,299,675,1456], 5, 666) == false

function FindFirstNonValid(preamble=25, file="input.txt")

    numbers =  parse.(Int,readlines(file))
    for i in preamble+1:length(numbers)
        n = numbers[i]
        if IsValidNumber(numbers[i-preamble:i-1], preamble, n) == false
            return n
        end
    end
end

@test FindFirstNonValid(5, "test.txt") == 127

function FindRange(num::Int, list::Vector{Int})
    first = 1
    last = 1
    while first < length(list) && last < length(list)
        while sum(list[first:last]) < num && last <= length(list)
            last += 1
        end
        while sum(list[first:last]) > num && first <= length(list)
            first += 1
        end
        if sum(list[first:last]) == num
            return list[first:last]
        end
    end
end

@testset "FindRange" begin
    list = parse.(Int,readlines("test.txt"))
    range = FindRange(127, list)
    @test range  == [15, 25, 47, 40]
    @test maximum(range) == 47
    @test minimum(range) == 15
    @test minimum(range) + maximum(range) == 62
end

# Part 1
partOne(preamble = 25, file="input.txt") = FindFirstNonValid(preamble, file)

@test partOne(5, "test.txt") == 127
@test partOne() == 36845998
println(string("Part one: ", partOne()))

# stats = Dict()
# jbench = @benchmark partOne()
# stats["partOne"] = minimum(jbench.times)/1e3

# Part 2
function partTwo(num = 25, file="input.txt")
    range = FindRange(num, parse.(Int,readlines(file)))
    minimum(range) + maximum(range)
end
@test partTwo(36845998) == 4830226
println(string("Part two: ", partTwo(36845998)))

# jbench = @benchmark partTwo()
# stats["partTwo"] = minimum(jbench.times)/1e3


# for (key, value) in sort(collect(stats), by=last)
#     println(rpad(key, 10, " "), lpad(round(value; digits=1), 6, " "), " ms")
# end
