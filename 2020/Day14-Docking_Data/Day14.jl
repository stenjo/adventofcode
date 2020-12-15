# Day 14 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/14
#
# using DelimitedFiles
using Test
using BenchmarkTools
# using Primes

mutable struct Computer
    onesMask :: UInt64
    zeroMask :: UInt64
    mask :: String
    pc :: Int
    code :: Vector{String}
    mem :: Dict{UInt64,UInt64}
    function Computer(file="input.txt")
        code = readlines(file)
        new(0, typemax(UInt64), "", 1, code, Dict())
    end
end

function AddMask(m, c::Computer)
    c.onesMask = 0
    c.zeroMask = typemax(UInt64)
    c.mask = m
    for (i,n) in enumerate(reverse(m))
        if n == '0'
            c.zeroMask &= ~(2^(i-1))
        elseif n == '1'
            c.onesMask |= 2^(i-1)
        end
    end
end

function GetAddresses(v::UInt64, c::Computer)
    addresses = [v]
    for (i,n) in enumerate(reverse(c.mask))
        if n == '1'
            for (j,a) in enumerate(addresses)
                addresses[j] = a | 2^(i-1)
            end
        elseif n == 'X'
            na = []
            for (j,a) in enumerate(addresses)
                addresses[j] = a | 2^(i-1)
                push!(na, a & ~(2^(i-1)))
            end
            addresses = vcat(addresses, na)
        end
    end
    addresses
end

Masked(v::UInt64, c::Computer) = v & c.zeroMask | c.onesMask

function Execute(c::Computer, part::Int)
    instr = split(c.code[c.pc])
    if instr[1] == "mask"
        AddMask(pop!(instr), c)
    elseif instr[1][1:3] == "mem"
        m = match(r"\[(?<pos>\d+)\]$", instr[1])
        pos = parse(Int64, m["pos"])
        value = parse(UInt64, pop!(instr))
        if part == 2
            map(a->c.mem[a] = value, GetAddresses(UInt64(pos), c))
        elseif part == 1
            c.mem[pos] = Masked(value, c)
        end
    end
    c.pc += 1
end

@testset "Tests" begin
    c = Computer("test.txt")
    @test length(c.code) == 4
    @test c.zeroMask == typemax(UInt64)
    AddMask("X01", c)
    @test Masked(UInt64(0), c) == 0b001
    @test Masked(typemax(UInt64),c) == ~ UInt64(0b010)
    AddMask("1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", c)
    @test Masked(UInt64(0), c) == 0b0100000000000000000000000000000000000
    AddMask("0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", c)
    @test Masked(typemax(UInt64),c) == ~ UInt64(0b0100000000000000000000000000000000000)

    Execute(c,1)
    @test c.zeroMask != typemax(UInt64)
    @test ~c.zeroMask == 2^1
    @test c.onesMask == 2^6
    @test c.onesMask == 0b01000000
    @test Masked(UInt64(11),c) == 0b1001001
    Execute(c,1)
    @test Int(c.mem[8]) == 73
    Execute(c,1)
    @test Int(c.mem[7]) == 101
    Execute(c,1)
    @test Int(c.mem[8]) == 64

    c = Computer("test2.txt")
    Execute(c,1)
    @test sort(Int.(GetAddresses(UInt64(42), c))) == [26,27,58,59]
    Execute(c,1)
    Execute(c,1)
    @test sort(Int.(GetAddresses(UInt64(26), c))) == [16,17,18,19, 24, 25, 26, 27]

end



# Part 1
function partOne(file="input.txt")
    c = Computer(file)
    while c.pc <= length(c.code)
        Execute(c, 1)
    end
    sum(values(c.mem))
end

@test partOne("test.txt") == 165
@test partOne() == 13865835758282

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(file="input.txt")
    c = Computer(file)
    while c.pc <= length(c.code)
        Execute(c,2)
    end
    sum(values(c.mem))
end

@test partTwo("test2.txt") == 208
@test partTwo() == 4195339838136

println(string("Part two: ", partTwo()))
@time partTwo()
