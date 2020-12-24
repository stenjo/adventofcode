# Day 24 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/24
#
using Test
using Match
using BenchmarkTools
using DataStructures

#        1       
# -2  -1   0   1   2   3
#

function Move(tile::Pair{Int,Int}, inst::String)
    @match inst begin
        "nw" => return Pair(tile[1]-1,tile[2]-1)
        "ne" => return Pair(tile[1]+1,tile[2]-1)
        "w"  => return Pair(tile[1]-2,tile[2])
        "e"  => return Pair(tile[1]+2,tile[2])
        "sw" => return Pair(tile[1]-1,tile[2]+1)
        "se" => return Pair(tile[1]+1,tile[2]+1)
    end
end

function SplitInstructions(s::String)
    inst = Vector{String}()
    skipOne = false
    for i in 1:length(s)
        if skipOne
            skipOne = false
        elseif s[i] in "ew"
            push!(inst, s[i:i])
        elseif s[i] in "ns"
            push!(inst, s[i:i+1])
            skipOne = true
        end
    end
    inst
end

function TilePos(inst::Vector{String}, tile = Pair{Int,Int}(0,0))
    for i in inst
        tile = Move(tile, i)
    end
    tile
end

function NearByTiles(tiles::Dict, tile::Pair{Int,Int})
    count = 0
    x,y = tile
    for i in x-2:x+2, j in y-1:y+1 
        if  (i == x-2 && j == y-1) || 
            (i == x-2 && j == y+1) || 
            (i == x+2 && j == y-1) || 
            (i == x+2 && j == y+1)
            continue
        end
        if Pair(i,j) in keys(tiles)
            if !(i == x && j == y) 
                count += 1
            end
        end
    end
    count
end

function RunDay(tiles)
    tiles2 = deepcopy(tiles)
    (minX,maxX) = extrema(map(k->k[1], collect(keys(tiles))))
    (minY,maxY) = extrema(map(k->k[2], collect(keys(tiles))))

    # for tile in tiles
    for x in minX-2:maxX+2, y in minY-1:maxY+1
        if  (x == minX-2 && y == minY-1) || 
            (x == maxX+2 && y == minY-1) ||
            (x == minX-2 && y == maxY+1) ||
            (x == maxX+2 && y == maxY+1)
            continue
        end
        check = Pair(x,y)
        nearby = NearByTiles(tiles, check)
        if check in tiles && (nearby > 2 || nearby == 0)
            delete!(tiles2, check)
        elseif !(check in tiles) && nearby == 2
            push!(tiles2, check=>"Black")
        end
    end
    tiles2
end

@testset "TileFlipping" begin
    @test SplitInstructions("esenee") == ["e", "se", "ne", "e"]
    @test SplitInstructions("nwwswee") == ["nw", "w", "sw", "e", "e"]
    @test Move(Pair(0,0), "ne") == Pair(1,-1)
    @test Move(Pair(0,0), "nw") == Pair(-1,-1)
    @test Move(Pair(0,0), "w") == Pair(-2,0)
    @test Move(Pair(0,0), "se") == Pair(1,1)
    @test TilePos(SplitInstructions("nwwswee")) == Pair(0,0)
    @test NearByTiles(Dict(Pair(1,-1)=>"Black", Pair(-2,0)=>"Black"), Pair(0,0)) == 2
    @test NearByTiles(Dict(Pair(1,-1)=>"Black", Pair(-2,0)=>"Black", Pair(-2,1)=>"Black"), Pair(0,0)) == 2
    # @test count(TilePos()
end

# Part 1
# partOne(labling = input) = RunGame(100, CupsGame(labling))
function partOne(input="input.txt")
    tiles = Dict()
    for tile in SplitInstructions.(readlines(input))
        t = TilePos(tile)
        t in keys(tiles) ? delete!(tiles, t) : push!(tiles, t=>"Black")
    end
    length(tiles)
end


@test partOne("test.txt") == 10
@test partOne() == 277

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(input="input.txt")
    tiles = Dict()
    for tile in SplitInstructions.(readlines(input))
        t = TilePos(tile)
        t in keys(tiles) ? delete!(tiles, t) : push!(tiles, t=>"Black")
    end
    for n in 1:1
        tiles = RunDay(tiles)
    end
    length(tiles)
end

# @test partTwo("test.txt") == 2208
# @test partTwo() == 33369

# @time println(string("Part two: ", partTwo())) # Answer too low
# @time partTwo()
