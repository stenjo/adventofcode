# Day 22 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/22
#
using Test
using Match
using BenchmarkTools

function LoadDecks(file="input.txt")
    lines = readlines(file)
    decks = []
    player = 0
    for l in lines
        if startswith(l,"Player")
            player = parse(Int, split(split(l,":")[1])[2])
            push!(decks, [])
        elseif l == ""
            player == 0
        elseif player != 0
            push!(decks[player], parse(Int, l))
        end
    end
    decks
end

function PlayRound(decks)
    p1 = popfirst!(decks[1])
    p2 = popfirst!(decks[2])
    if p1 > p2
        push!(decks[1], p1)
        push!(decks[1], p2)
    elseif p2 > p1
        push!(decks[2], p2)
        push!(decks[2], p1)
    else
        println("E!!!")
    end
    decks
end

GetIncrSum(decks) = sum(p->length(p) > 0 ? sum(map(x -> x[2]*(length(p)-x[1]+1), enumerate(p))) : 0, [s for s in decks if !all(isempty.(s))])

function GetIncrSum1(decks)
    sum = 0
    for d in decks
        for (i,n) in enumerate(reverse(d))
            sum += i*n
        end
    end
    sum
end

GetHash(decks) = hash(Pair(sum(map(x -> x[2]*x[1], enumerate(decks[1]))),sum(diff(map(x -> x[2]*x[1], enumerate(reverse(decks[2])))))))

function PlayRound2(decks, checksums, game, round)
    round +=1
    # println("\n-- Round ", round, " (Game ", game, ") --")
    # println("Player 1's deck: ", decks[1])
    # println("Player 2's deck: ", decks[2])
    winner = 0
    if GetHash(decks) in checksums  # Been here before
        decks[1] = vcat(decks[1],decks[2])
        empty!(decks[2])
        winner = 1
        # println("Game ", game, " won by Player 1 on been here before")
    else
        push!(checksums, GetHash(decks))
        p1 = popfirst!(decks[1])
        p2 = popfirst!(decks[2])
        # println("Player 1 plays: ",p1, " (cards left: ", length(decks[1]), ")")
        # println("Player 2 plays: ",p2, " (cards left: ", length(decks[2]), ")")
        if length(decks[1]) >= p1 && length(decks[2]) >= p2 # both players got cards
            # the winner of the round is determined by playing a new game of Recursive Combat
            # println("Playing a sub-game to determine the winner...")
            (winner,_) = Game([copy(decks[1][1:p1]), copy(decks[2][1:p2])], game)
            if winner == 1
                push!(decks[1], p1)
                push!(decks[1], p2)
            else
                push!(decks[2], p2)
                push!(decks[2], p1)
            end
        else
            if p1 > p2
                push!(decks[1], p1)
                push!(decks[1], p2)
                winner = 1
            elseif p2 > p1
                push!(decks[2], p2)
                push!(decks[2], p1)
                winner = 2
            end
        end
    end
    # println("Player ", winner," wins round ",round," of game ",game,"!")
    decks, round
end

function Game(decks, game)
    game +=1
    # println("\n=== Game ", game," ===")
    checksums = []
    round = 0
    ds = copy(decks)
    while !(0 in map(x->length(x), ds))
        decks,round = PlayRound2(ds, checksums, game, round)
    end
    winner = length(decks[1]) > 0 ? 1 : 2
    # println("Winner of game ",game, " is player ", winner,"!\n")
    (winner, decks)
end


@testset "Cardgame" begin
    @test length(LoadDecks("test.txt")) == 2
    @test map(x->length(x), LoadDecks("test.txt")) == [5,5]
    @test GetIncrSum(LoadDecks("test.txt")) == 171

    decks = LoadDecks()
    checksums = []
    @test GetIncrSum(decks) == 16842
    (decks, _) = PlayRound2(decks,checksums,0,0)
    @test GetIncrSum(decks) == 17376
    @test GetIncrSum([[41, 8, 42, 20, 48, 22, 50, 24], [40, 17, 43, 4, 34, 21, 35, 23, 39, 1]]) == 2640
    @test GetIncrSum([[41, 40, 20, 4, 48, 34, 22, 21, 50, 35, 24, 23], [17, 8, 43, 42, 39, 7]]) == 2928
    @test GetIncrSum([[48, 39, 34, 7, 21, 20, 50, 42, 35, 4, 23, 22, 17, 5, 40, 24], [43, 41]]) == 4140
    @test GetIncrSum([[5, 48, 17, 50, 41, 4, 21, 42, 23, 25, 28, 3, 31, 16, 45, 12, 29, 19, 44, 37, 47, 15, 38, 10], [24, 1, 40, 7, 8, 43, 34, 20, 35, 22, 39, 13, 26, 2, 27, 14, 49, 33, 32, 18, 46, 36, 30, 6]]) == 15202
    @test GetIncrSum([[31, 16, 45, 12, 29, 19, 44, 37, 47, 15, 38, 10, 9, 11, 48, 1, 50, 7, 41, 8, 42, 20, 25, 22], [26, 2, 27, 14, 49, 33, 32, 18, 46, 36, 30, 6, 24, 5, 40, 17, 43, 4, 34, 21, 35, 23, 39, 28]]) == 15821
    @test GetIncrSum([[45, 12, 29, 19, 44, 37, 47, 15, 38, 10, 9, 11, 48, 1, 50, 7, 41, 8, 42, 20, 25, 22, 31, 26], [27, 14, 49, 33, 32, 18, 46, 36, 30, 6, 24, 5, 40, 17, 43, 4, 34, 21, 35, 23, 39, 28, 13, 3]]) == 16524
end



# Part 1
function partOne(file="input.txt")
    decks = LoadDecks(file)
    while !(0 in map(x->length(x), decks))
        PlayRound(decks)
    end
    GetIncrSum(decks)
end

@test partOne("test.txt") == 306
@test partOne() == 34255

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(file="input.txt")
    decks = LoadDecks(file)
    (winner, result) = Game(decks, 0)
    # println("Player 1's deck: ", decks[1])
    # println("Player 2's deck: ", decks[2])
    GetIncrSum(result)
end

@test partTwo("test.txt") == 291
# @test partTwo() == 33369

println(string("Part two: ", partTwo())) # Answer too low
# @time partTwo()
