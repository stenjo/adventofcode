# Day 6 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/6
# 

using DelimitedFiles
using Test

# Test information from the puzzle
testinput = [
    "abcx",
    "abcy",
    "abcz"] 
testlines = readlines("testinput.txt")

# Actual personallized data
inputdata = readlines("input.txt")

function CleanUpInput(input)
    chunk = []
    output = []
    for item in input
        if item == ""
            push!(output, copy(chunk))
            empty!(chunk)
        else
            push!(chunk, item)
        end
    end
    push!(output, copy(chunk))
    output
end
@testset "  CleanUpInput" begin
    @test length(CleanUpInput(testinput)) == 1
    @test length(CleanUpInput(testlines)) == 5
    @test length(CleanUpInput(testlines)[3]) == 2 
end

function AnyOneAnswers(group)
    unique(join(group))
end
@testset "AnyOneAnswers" begin
    @test length(AnyOneAnswers(CleanUpInput(testlines)[1])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[2])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[3])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[4])) == 1 #a
    @test length(AnyOneAnswers(CleanUpInput(testlines)[5])) == 1 #b
    @test sum(length.(AnyOneAnswers.(CleanUpInput(testlines)))) == 11
end

function EveryOneAnswers(group)
    count(v->v==group[1], group)
    questions = []
    for q in join(group)
        if count(x->(q in x), group) == length(group)
            push!(questions, q)
        end
    end
    join(unique(questions))
end


@testset "EveryOneAnswers" begin
    @test length(EveryOneAnswers(CleanUpInput(testlines)[1])) == 3 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[2])) == 0 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[3])) == 1 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[4])) == 1 #a
    @test length(EveryOneAnswers(CleanUpInput(testlines)[5])) == 1 #b
    @test sum(length.(EveryOneAnswers.(CleanUpInput(testlines)))) == 6
end


# Part 1
function partOne(rawList)
    sum(length.(AnyOneAnswers.(CleanUpInput(rawList))))
end

@test partOne(testlines) == 11
@test partOne(inputdata) == 6590
println(string("Part one: ", partOne(inputdata)))

# Part 2
function partTwo(rawList)
    sum(length.(EveryOneAnswers.(CleanUpInput(rawList))))
end

# @test partTwo(inputdata) == 739
println(string("Part two: ", partTwo(inputdata)))
