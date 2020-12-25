# Day 25 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/25
#
using Test
using Match
using BenchmarkTools
using Primes

function GetLoopSize(pub::Int)
    loopSize = 1
    num = 1
    while true
        num = (num*7) % 20201227
        if num == pub
            return loopSize
        end
        loopSize += 1
    end
    0
end

function Transform(sn::Int, ls::Int)
    num = 1
    for n in 1:ls
        num = (num*sn) % 20201227
    end
    num
end

@testset "Encryption" begin
@test GetLoopSize(5764801) == 8
@test GetLoopSize(17807724) == 11
@test Transform(17807724, 8) == 14897079
@test Transform(5764801, 11) == 14897079
end

# Part 1
# partOne(labling = input) = RunGame(100, CupsGame(labling))
function partOne(input="input.txt")
    door,card = parse.(Int, readlines(input))
    Transform(card, GetLoopSize(door))
end


@test partOne("test.txt") == 14897079
@test partOne() == 11328376

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
# No part two! Needed only 49 coins it seems.
