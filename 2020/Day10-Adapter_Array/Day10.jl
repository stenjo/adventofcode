# Day 10 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/10
#
using Test

function LoadAdapters(file="input.txt")
    adapterList = parse.(Int, readlines(file))
    sort!(adapterList)
    pushfirst!(adapterList,0)
    push!(adapterList, maximum(adapterList)+3)
end

@testset "LoadAdapters" begin
    adapters = LoadAdapters("test.txt")
    @test length(adapters) == 13
    @test maximum(adapters) == 19+3
    @test minimum(adapters) == 0
    @test adapters[1] == minimum(adapters)
    @test adapters[end] == maximum(adapters)
end

# Array of diffs between one element and the next
FindGaps(list) = list[2:end] .- list[1:end-1]

@testset "FindGaps" begin
    adapters = LoadAdapters("test.txt")
    gaps = FindGaps(adapters)
    @test count(g->(g == 1), gaps) == 7
    @test count(g->(g == 3), gaps) == 5
    gaps = FindGaps(LoadAdapters("test2.txt"))
    @test count(g->(g == 1), gaps) == 22
    @test count(g->(g == 3), gaps) == 10
end

function ValidChain(list)
    maximum(FindGaps(list)) <= 3
end

function FindCombinations(list)
    diffs = FindGaps(list)
    configs = zeros(Int, list[end]+3)
    configs[end] = 1
    for a in reverse(list[2:end]) # Start from largest - Do not include starting adapter
        configs[a] = sum(configs[a+1:a+3])
    end
    sum(configs[1:3])
end

@testset "FindCombinations" begin
    a = LoadAdapters("test.txt")
    @test FindCombinations(a) == 8
    @test FindCombinations(LoadAdapters("test2.txt")) == 19208
end

# Part 1
function partOne(file="input.txt")
    gaps = FindGaps(LoadAdapters(file))
    count(g->(g == 1), gaps) * count(g->(g == 3), gaps)
end
@test partOne("test.txt") == 35
@test partOne("test2.txt") == 220
@test partOne() == 1917
println(string("Part one: ", partOne()))

# Part 2
partTwo(file="input.txt") = FindCombinations(LoadAdapters(file))

@test partTwo("test.txt") == 8
@test partTwo("test2.txt") == 19208
@test partTwo() == 113387824750592
println(string("Part two: ", partTwo()))
