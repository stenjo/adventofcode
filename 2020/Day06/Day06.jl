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
    foreach(i->(i != "" ? push!(chunk, i) : begin push!(output, copy(chunk)); empty!(chunk); end), input)
    push!(output, copy(chunk))
end

@testset "  CleanUpInput" begin
    @test length(CleanUpInput(testinput)) == 1
    @test length(CleanUpInput(testlines)) == 5
    @test length(CleanUpInput(testlines)[3]) == 2 
end

function GetInput(str=read("input.txt", String))
    map(split, split(str, "\r\n\r\n"))
end
@testset "GetInput" begin
    @test length(GetInput(read("testinput.txt", String))) == 5
    @test length(GetInput(read("testinput.txt", String))[3]) == 2 
end

function GetDefaultInput()
    # map(split, split(read("input.txt", String), "\r\n\r\n"))
    map(split, split(read("testinput.txt", String), "\r\n\r\n"))
end
@testset "GetDefaultInput" begin
    @test length(GetDefaultInput()) == 5
    @test length(GetDefaultInput()[3]) == 2 
end

AnyOneAnswers(group) = join(union(group...))

@testset "AnyOneAnswers" begin
    @test length(AnyOneAnswers(testinput)) == 6 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[1])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[2])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[3])) == 3 #abc
    @test length(AnyOneAnswers(CleanUpInput(testlines)[4])) == 1 #a
    @test length(AnyOneAnswers(CleanUpInput(testlines)[5])) == 1 #b
    @test sum(length.(AnyOneAnswers.(CleanUpInput(testlines)))) == 11
end

EveryOneAnswers(group) = join(intersect(group...))

@testset "EveryOneAnswers" begin
    @test length(EveryOneAnswers(testinput)) == 3 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[1])) == 3 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[2])) == 0 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[3])) == 1 #abc
    @test length(EveryOneAnswers(CleanUpInput(testlines)[4])) == 1 #a
    @test length(EveryOneAnswers(CleanUpInput(testlines)[5])) == 1 #b
    @test sum(length.(EveryOneAnswers.(CleanUpInput(testlines)))) == 6
end


# Part 1
partOne(rawList) = sum(length.(AnyOneAnswers.(CleanUpInput(rawList))))

@test partOne(testlines) == 11
@test partOne(inputdata) == 6590
println(string("Part one: ", partOne(inputdata)))

# Part 2
partTwo(rawList) = sum(length.(EveryOneAnswers.(CleanUpInput(rawList))))

@test partTwo(inputdata) == 3288
println(string("Part two: ", partTwo(inputdata)))
println(sum(length.(map(g->join(intersect(g...)), map(split, split(read("input.txt", String), "\r\n\r\n")) ))))
