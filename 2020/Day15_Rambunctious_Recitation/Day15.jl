# Day 15 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/15
#
# using DelimitedFiles
using Test
using BenchmarkTools
# using Primes

test = [0,3,6]
input = [1,20,8,12,0,14]


function NthNumSpoken(num::Int, list::Vector{Int})
    numList = zeros(Int, num)
    for (i,n) in enumerate(list[1:end-1])
        numList[n+1]=i
    end
    turn = length(list)
    number = list[end]
    while turn < num
        next = numList[number+1] == 0 ? 0 : turn - numList[number+1]
        numList[number+1] = turn
        number = next
        turn += 1
    end
    number
end

@testset "NthNumSpoken" begin
    @test NthNumSpoken(10, [0,3,6]) == 0
    @test NthNumSpoken(2020, [0,3,6]) == 436
    @test NthNumSpoken(2020, [1,3,2]) == 1
    @test NthNumSpoken(2020, [2,1,3]) == 10
    @test NthNumSpoken(2020, [1,2,3]) == 27
    @test NthNumSpoken(2020, [2,3,1]) == 78
    @test NthNumSpoken(2020, [3,2,1]) == 438
    @test NthNumSpoken(2020, [3,1,2]) == 1836
end

# Part 1
partOne(num = 2020, list = input) = NthNumSpoken(num, list)

@test partOne(2020, test) == 436
@test partOne() == 492

@time println(string("Part one: ", partOne()))
# @time partOne()

# Part 2
partTwo(num = 30000000, list = input) = NthNumSpoken(num, list)

@test partTwo(30000000, [0,3,6]) == 175594
@test partTwo() == 63644

@time println(string("Part two: ", partTwo()))
# @time partTwo()
