# Day 23 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/23
#
using Test
using Match
using BenchmarkTools
using DataStructures

input = readlines("input.txt")[1]

mutable struct CupsGame
    cups :: Array{Int}
    current :: Int
    CupsGame(initial::String) = new(parse.(Int,[string(c) for c in initial]), 1)
    CupsGame(initial::Array{Int}) = new(initial, 1)
end

function Move(g::CupsGame)
    stack = []
    len = length(g.cups)
    selected = g.cups[g.current]
    for i in 1:3
        g.current+1 <= length(g.cups) ? push!(stack, popat!(g.cups, g.current+1)) : begin push!(stack, popfirst!(g.cups)); g.current -=1 end
    end

    dest = selected == 1 ? len : selected - 1
    while dest in stack
        dest = dest == 1 ? len : dest - 1
    end

    insertAt = findfirst(x->x == dest, g.cups)
    if insertAt == length(g.cups)
        g.cups = cat(g.cups,stack; dims=1)
    else
        g.cups = cat(g.cups[1:insertAt], stack, g.cups[insertAt+1:end]; dims=1)
    end
    g.current = findfirst(x->x == selected, g.cups) % length(g.cups) + 1
end

function RunGame(moves :: Int, game :: CupsGame)
    for i in 1:moves
        Move(game)
    end
    cuplist = copy(game.cups)
    cup = popfirst!(cuplist)
    while cup != 1
        push!(cuplist,cup)
        cup = popfirst!(cuplist)
    end
    parse(Int,join(cuplist))
end

@testset "CupsGame" begin
    game = CupsGame("389125467") 
    @test game.cups[5] == 2
    @test RunGame(1, game) == 54673289
    @test RunGame(9, game) == 92658374
    @test RunGame(100, CupsGame("389125467")) == 67384529

end

function Move(g::Dict, current::Int)

    stack = []
    max = maximum(collect(keys(g)))
    wrap(n) = n == 1 ? max : n - 1
    
    for _ in 1:3
        push!(stack,g[current])
        g[current] = g[g[current]]
    end

    dest = wrap(current)
    while dest in stack
        dest = wrap(dest)
    end
    next = g[dest]
    n = 0
    for _ in 1:3
        n = pop!(stack)
        push!(g, n=>next)
        next = n
    end
    g[dest] = n
    current = g[current]
end

function GetList(l::Dict)
    seq = []
    cup = l[1]
    while cup != 1 && !(cup  in seq)
        push!(seq,cup)
        cup = l[cup]
    end
    parse(Int,join(seq))

end

function GetList2(l::Dict)
    seq = [l[1],l[l[1]]]
    parse(Int,join(seq))
end

# Try making a list of dict label->next
function RunGame(moves :: Int, game :: Dict, current)
    for _ in 1:moves
        current = Move(game, current)
    end

    parse(Int,join(GetList(game)))
end

function SetUpGame(list::Vector{Int})
    game = Dict{Int,Int}()

    # Initialise dict bakwards to get next pointers
    # list = parse.(Int,[string(c) for c in init])
    current = list[1]   # Point to start of list
    for n in reverse(list)
        push!(game, n=>current)
        current = n
    end
    (current, game)  
end


@testset "CupsGameDict" begin
    # game = CupsGame("389125467") 
    list = parse.(Int,[string(c) for c in "389125467"])
    (current, game) = SetUpGame(list)
    # @test game.cups[5] == 2
    @test RunGame(1, game, current) == 54673289
    (current, game) = SetUpGame(list)
    @test RunGame(10, game, current) == 92658374
    (current, game) = SetUpGame(list)
    @test RunGame(100, game, current) == 67384529

end


# Part 1
# partOne(labling = input) = RunGame(100, CupsGame(labling))
function partOne(labling = input)
    list = parse.(Int,[string(c) for c in labling])
    (current, game) = SetUpGame(list)
    RunGame(100, game, current)
end


@test partOne("389125467") == 67384529
@test partOne() == 45798623

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(initial = input)
    # cups = cat(game.cups,Array{Int}(maximum(game.cups)+1:1000000-length(game.cups)); dims=1)
    list = parse.(Int,[string(c) for c in initial])
    cups = cat(list,Array{Int}(maximum(list)+1:1000000-length(list)); dims=1)
    (current, game) = SetUpGame(cups)

    for _ in 1:10^6
        current = Move(game, current)
    end

    game[1] * game[game[1]]

end

# @test partTwo("test.txt") == 291
# @test partTwo() == 33369

# @time println(string("Part two: ", partTwo())) # Answer too low
# @time partTwo()
