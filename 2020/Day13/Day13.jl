# Day 12 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/12
#
# using DelimitedFiles
using Test
using Primes

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

# @test BusTimes("test.txt").depTime == 939


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

# @testset "WaitTime" begin
#     bt = BusTimes("test.txt")
#     @test WaitTime(59,bt) == 5
# end

function FactorizeBus(v::Vector)
    factors = Set{Int}()
    for (i,c) in v
        union!(factors, factor(Set, bus))
    end
    factors
end

function Valid(t, schedule)
    for (i,n) in schedule
        if (i-1+t) % n != 0
            return false
        end
    end
    true
end

# @test Valid(0,[(1,2),(2,3)]) == false
# @test Valid(2,[(1,2),(2,3)]) == true
# @test Valid(3,[(1,2),(2,3)]) == false
# @test Valid(4,[(1,2),(2,3)]) == false
# @test Valid(2,[(1,2),(2,3),(3,4)]) == true

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
# @testset "ParseSchedule" begin
#     @test ParseSchedule(["17","x","13","19"]) == [(1,17),(3,13),(4,19)]
#     @test ParseSchedule(BusTimes("test.txt").schedule) == [(1, 7), (2, 13), (5, 59), (7, 31), (8, 19)]
#     @test ParseSchedule(["1789","37","47","1889"]) == [(1, 1789), (2, 37), (3,47), (4,1889)]
# end

function GetEarliest(s::Vector)
    firstBus = s[1][2]
    t=firstBus
    while !Valid(t,s)
        t += firstBus
    end
    t
end

# @testset "GetEarliest" begin
#     @test GetEarliest([(1,2),(2,3)]) == 2
#     @test GetEarliest(ParseSchedule(["17","x","13","19"])) == 3417
#     @test GetEarliest(ParseSchedule(copy(split("67,7,59,61", ",")))) == 754018
#     @test GetEarliest(ParseSchedule(split("67,x,7,59,61", ","))) == 779210
#     @test GetEarliest(ParseSchedule(split("67,7,x,59,61", ","))) == 1261476
#     @test GetEarliest(ParseSchedule(split("1789,37,47,1889", ","))) == 1202161486
# end


function CommonInterval(a,b)
    ptr = a[2]
    offset = b[1] - a[1]
    while (ptr + offset) % b[2] != 0
        ptr += a[2]
    end
    ptr
end

function solve2((offs, ids))
    res = ids[1]-offs[1] # we can save the first iteration by just directly calculating it
    step = 1

    for (num, off) in zip(ids, offs)
        while !iszero((res + off) % num)
            res += step
        end
        step *= num
    end

    res
end

function GetEarliest2(s::Vector)
    t = s[1][2] - s[1][1]
    step = 1
    for (i,n) in s
        while !iszero((t + i) % n)
            t += step
        end
        step += i
    end
    t
end
@testset "GetEarliest2" begin
    @test GetEarliest2([(1,2),(2,3)]) == 2
    @test GetEarliest2([(1,2),(2,3),(3,4)]) == 2
    @test GetEarliest2([(1,2),(2,3),(3,4),(4,5)]) == 2
    @test GetEarliest2([(1,3),(2,5)]) == 9
    @test GetEarliest2([(1,2),(2,5)]) == 4
    @test GetEarliest2([(1,3),(2,4),(4,5)]) == 27
    @test GetEarliest2(ParseSchedule(["17","x","13","19"])) == 3417
    @test GetEarliest2(ParseSchedule(copy(split("67,7,59,61", ",")))) == 754018
    # @test GetEarliest2(ParseSchedule(split("67,x,7,59,61", ","))) == 779210
    # @test GetEarliest2(ParseSchedule(split("67,7,x,59,61", ","))) == 1261476
    # @test GetEarliest2(ParseSchedule(split("1789,37,47,1889", ","))) == 1202161486
end

# Part 1
function partOne(file="input.txt")
    bt = BusTimes(file)
    GetWaitTimes(bt)
end

# @test partOne("test.txt") == 295
# @test partOne() == 207
# println(string("Part one: ", partOne()))

# println(GetWaitTimes(BusTimes()))

# Part 2
function partTwo(file="input.txt")
    bt = BusTimes(file)
    GetEarliest2(ParseSchedule(bt.schedule))
end

# @test partTwo("test.txt") == 286
# @test partTwo() == 42495
# println()
# println(string("Part two: ", partTwo()))
