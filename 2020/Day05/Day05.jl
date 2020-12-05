# Day 5 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/5
# 

using DelimitedFiles
using Test

# Test information from the puzzle
testinput = [
    "BFFFBBFRRR", # row 70, column 7, seat ID 567
    "FFFBBBFRRR", # row 14, column 7, seat ID 119.
    "BBFFBBFRLL"] # row 102, column 4, seat ID 820

# Actual personallized data
inputdata = readdlm("input.txt", '\t', String, '\n', skipblanks=false)

function GetRow(spec)
    row = 127
    mask = 64
    for c in spec
        if c == 'F'
            row = row & ~mask
        end
        mask = mask >>> 1
    end
    row
end
@test GetRow("BFFFBBFRRR") == 70
@test GetRow("FFFBBBFRRR") == 14
@test GetRow("BBFFBBFRLL") == 102

function GetColumn(spec)
    column = 7
    mask = 4
    for c in spec[end-2:end]
        if c == 'L'
            column = column & ~mask
        end
        mask = mask >>> 1
    end
    column
end
@test GetColumn("BFFFBBFRRR") == 7
@test GetColumn("FFFBBBFRRR") == 7
@test GetColumn("BBFFBBFRLL") == 4

mutable struct BoardingPass
    row :: Int
    column :: Int
    seat :: Int

    function BoardingPass(spec)
        new(
            GetRow(spec),
            GetColumn(spec),
            GetRow(spec) * 8 + GetColumn(spec)
            )
    end
end

@testset "BoardingPass initialize" begin

    # row 70, column 7, seat ID 567
    bp = BoardingPass(testinput[1])
    @test bp.row == 70
    @test bp.column == 7
    @test bp.seat == 567
    
    # row 14, column 7, seat ID 119.
    bp = BoardingPass(testinput[2])
    @test bp.row == 14
    @test bp.column == 7
    @test bp.seat == 119
    
    # row 102, column 4, seat ID 820
    bp = BoardingPass(testinput[3])
    @test bp.row == 102
    @test bp.column == 4
    @test bp.seat == 820
end

function MaxSeatID(list)
    seatIds = []
    for bp in list
        push!(seatIds, BoardingPass(bp).seat)
    end
    maximum(seatIds)
end
@test MaxSeatID(testinput) == 820


# Part 1
function partOne(rawList)
    maximum(v->BoardingPass(v).seat, rawList)
end

@test partOne(testinput) == 820
@test partOne(inputdata) == 864
println(string("Part one: ", partOne(inputdata)))

# Part 2
function partTwo(rawList)
    seats = BoardingPass.(rawList)
    for r in 1:126
        if count(s->(s.row == r), seats) == 7
            for c in 0:7
                if length(filter(s->s.row == r && s.column == c, seats)) == 0
                    return r*8+c
                end
            end
        end
    end
end

@test partTwo(inputdata) == 739
println(string("Part two: ", partTwo(inputdata)))
