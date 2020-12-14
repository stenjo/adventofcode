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

# Chinese remainder solves this apparently
# https://rosettacode.org/wiki/Chinese_remainder_theorem

function chineseremainder(n::Array, a::Array)
    Π = prod(n)
    mod(sum(ai * invmod(Π ÷ ni, ni) * (Π ÷ ni) for (ni, ai) in zip(n, a)), Π)
end
 
@test chineseremainder([3, 5, 7], [2, 3, 2]) == 23
@test chineseremainder([1, 3], [0, 2]) == 2


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
    buses = [i[2] for i in s]
    times = [i[1]-1 for i in s]
    chineseremainder(buses, times)
end

@testset "GetEarliest2" begin
    # @test GetEarliest2([(1,2),(2,3)]) == 2
    # @test GetEarliest2([(1,2),(2,3),(3,4)]) == 2
    # @test GetEarliest2([(1,2),(2,3),(3,4),(4,5)]) == 2
    # @test GetEarliest2([(1,3),(2,5)]) == 9
    # @test GetEarliest2([(1,2),(2,5)]) == 4
    # @test GetEarliest2([(1,3),(2,4),(4,5)]) == 27
    # @test GetEarliest2(ParseSchedule(["17","x","13","19"])) == 3417
    # @test GetEarliest2(ParseSchedule(copy(split("67,7,59,61", ",")))) == 754018
    # @test GetEarliest2(ParseSchedule(split("67,x,7,59,61", ","))) == 779210
    # @test GetEarliest2(ParseSchedule(split("67,7,x,59,61", ","))) == 1261476
    # @test GetEarliest2(ParseSchedule(split("1789,37,47,1889", ","))) == 1202161486
end

# Part 1
function partOne(file="input.txt")
    bt = BusTimes(file)
    GetWaitTimes(bt)
end

@test partOne("test.txt") == 295
@test partOne() == 207
println(string("Part one: ", partOne()))
@btime partOne()

# println(GetWaitTimes(BusTimes()))

# Part 2
function partTwo(file="input.txt")
    bt = BusTimes(file)
    GetEarliest2(ParseSchedule(bt.schedule))
end

# @test partTwo("test.txt") == 286
# @test partTwo() == 530015546283687
# println()
# println(string("Part two: ", partTwo()))

########################################
# Part 2 (from https://julialang.zulipchat.com/#narrow/stream/265470-advent-of-code/topic/Solutions.20day.2013/near/219750527)
########################################
function solve(v)
    x = v[1][1]
    offset = x
    for i in 2:length(v)
        y, d = v[i]
        r = mod(-d - offset, y)
        offset = mod(invmod(x, y)*r, y) * x + offset
        x = lcm(x, y)
    end

    return offset
end

function solve(v::T) where {T <: AbstractString}
    res = []
    for (i, x) in enumerate(split(v, ","))
        x == "x" && continue
        push!(res, (parse(Int, x), i - 1))
    end

    return solve(identity.(res))
end

println("Part 2: ", solve(readlines("input.txt")[2]))