# Day 12 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/12
#
# using DelimitedFiles
using Test
using BenchmarkTools
# using Primes

mutable struct BusTimes
    depTime :: Int64
    schedule :: Vector{String}
    function BusTimes(file="input.txt")
        indata = readlines(file)
        d = parse(Int, indata[1])
        s = split(indata[2], ",")
        new(d, s)
    end
end

@test BusTimes("test.txt").depTime == 939


function WaitTime(bus::Int, b :: BusTimes)
    bus - mod(b.depTime, bus)
end

function GetWaitTimes(bt::BusTimes)
    waiting = []
    bus = 0
    shortest = 1000
    for c in bt.schedule
        if !('x' in c)
            w = WaitTime(parse(Int, c), bt)
            if w < shortest
                shortest = w
                bus = parse(Int, c)
            end
            push!(waiting, WaitTime(parse(Int, c), bt))
        end
    end
    bus * shortest
end

@testset "WaitTime" begin
    bt = BusTimes("test.txt")
    @test WaitTime(59,bt) == 5
end

function Valid(t, schedule)
    for (i,n) in schedule
        if (i-1+t) % n != 0
            return false
        end
    end
    true
end

@test Valid(0,[(1,2),(2,3)]) == false
@test Valid(2,[(1,2),(2,3)]) == true
@test Valid(3,[(1,2),(2,3)]) == false
@test Valid(4,[(1,2),(2,3)]) == false
@test Valid(2,[(1,2),(2,3),(3,4)]) == true

function ParseSchedule(s::Vector)
    v = Vector()
    for (i,n) in enumerate(s)
        if !('x' in n)
            bus = parse(Int, n)
            push!(v, (i,bus))
        end
    end
    v
end
@testset "ParseSchedule" begin
    @test ParseSchedule(["17","x","13","19"]) == [(1,17),(3,13),(4,19)]
    @test ParseSchedule(BusTimes("test.txt").schedule) == [(1, 7), (2, 13), (5, 59), (7, 31), (8, 19)]
    @test ParseSchedule(["1789","37","47","1889"]) == [(1, 1789), (2, 37), (3,47), (4,1889)]
end

function FindDeparture(s::Vector)
    firstBus = s[1][2]
    t=firstBus
    while !Valid(t,s)
        t += firstBus
    end
    t
end

@testset "FindDeparture" begin
    @test FindDeparture([(1,2),(2,3)]) == 2
    @test FindDeparture(ParseSchedule(["17","x","13","19"])) == 3417
    @test FindDeparture(ParseSchedule(copy(split("67,7,59,61", ",")))) == 754018
    @test FindDeparture(ParseSchedule(split("67,x,7,59,61", ","))) == 779210
    @test FindDeparture(ParseSchedule(split("67,7,x,59,61", ","))) == 1261476
    @test FindDeparture(ParseSchedule(split("1789,37,47,1889", ","))) == 1202161486
end

# Chinese remainder solves this apparently
# https://rosettacode.org/wiki/Chinese_remainder_theorem
# Part 2 (from https://julialang.zulipchat.com/#narrow/stream/265470-advent-of-code/topic/Solutions.20day.2013/near/219750527)
########################################
function FindPattern(s::Vector)
    # chineseremainder(buses, times)
    x = s[1][2]
    offset = x
    for i in 2:length(s)
        d, y = s[i]
        r = mod(1-d - offset, y)
        offset = mod(invmod(x, y)*r, y) * x + offset
        x = lcm(x, y)
    end
    offset
end

@testset "FindPattern" begin
    @test FindPattern([(1,2),(2,3)]) == 2
    @test FindPattern([(1,3),(2,5)]) == 9
    @test FindPattern([(1,2),(2,5)]) == 4
    @test FindPattern([(1,3),(2,4),(4,5)]) == 27
    @test FindPattern(ParseSchedule(["17","x","13","19"])) == 3417
    @test FindPattern(ParseSchedule(copy(split("67,7,59,61", ",")))) == 754018
    @test FindPattern(ParseSchedule(split("67,x,7,59,61", ","))) == 779210
    @test FindPattern(ParseSchedule(split("67,7,x,59,61", ","))) == 1261476
    @test FindPattern(ParseSchedule(split("1789,37,47,1889", ","))) == 1202161486
end

# Part 1
function partOne(file="input.txt")
    bt = BusTimes(file)
    GetWaitTimes(bt)
end

@test partOne("test.txt") == 295
@test partOne() == 207
println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(file="input.txt")
    bt = BusTimes(file)
    FindPattern(ParseSchedule(bt.schedule))
end

@test partTwo("test.txt") == 1068781
@test partTwo() == 530015546283687
println(string("Part two: ", partTwo()))
@time partTwo()
