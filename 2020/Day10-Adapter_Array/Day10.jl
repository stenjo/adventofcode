# Day 10 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/10
#
# using DelimitedFiles
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

function FindGaps(list)
    diffs = []
    for i in 1:length(list)-1
        diff = list[i+1]-list[i]
        push!(diffs, diff)
    end
    diffs
end
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
    count = 1
    vars = 1
    filterlist = []
    offset = 0
    for (i,n) in enumerate(list)
        if i == 1 || i == length(list) || offset > 0
            if offset > 0
                offset -= 1
            end
            continue
        end
        while ValidChain(filter(v->!(v in filterlist), list))
            push!(filterlist, list[i+offset])
            if ValidChain(filter(v->!(v in filterlist), list))
                count += 1
            end
            offset += 1
        end
        exp = length(filterlist)-1
        n = length(filterlist)
        if exp > 0
            vars *= 2^exp
            println([length(filterlist), 2^exp, vars, offset, n*(n-1)/2])
            empty!(filterlist)
            continue
        end
        while length(filterlist) > 0
            popfirst!(filterlist)
            if ValidChain(filter(v->!(v in filterlist), list)) && length(filterlist) > 0
                count += 1
            end
        end
    end
    vars
end

function Recurse(list)
    combinations = 0
    max = length(list) < 5 ? length(list) : 5
    for (i,n) in enumerate(list[2:max-1])
        filteredList = filter(v->v!=n, list[i:max])
        if ValidChain(filteredList)    #If chain still valid when removing this number
            combinations += 1 + Recurse(filteredList)
        end
    end
    combinations
end

function RecursiveFindCombination(list)
    combinations = 0
    for (i,n) in enumerate(list[2:end-1])
        filteredList = filter(v->v!=n, list[i:end])
        if ValidChain(filteredList)    #If chain still valid when removing this number
            combinations += 1 + RecursiveFindCombination(filteredList)
        end
    end
    combinations
end

function BrettsWay(list, range)
    solutions = []
    for (i,n) in enumerate(list)
        if n <= 1
            push!(solutions, 1)
        else
            solution = 0
            count_back = 1
            while i - count_back >= 1 && count_back <= range
                if n - range <= list[i-count_back]
                    solution += solutions[i-count_back]
                end
                count_back += 1
            end
            push!(solutions, solution)
        end
    end
    pop!(solutions)
end


@testset "FindCombinations" begin
    # 1 -> 1
    # 2 -> 2
    # 3 -> 4
    # 4 -> 
    a = LoadAdapters("test.txt")
    @test RecursiveFindCombination(a)+1 == 8
    @test RecursiveFindCombination(LoadAdapters("test2.txt"))+1 == 19208
    @test BrettsWay(a, 3) == 8
    @test BrettsWay(LoadAdapters("test2.txt"), 3) == 19208
    # @test FindCombinations(a) == 8
    # @test FindCombinations(LoadAdapters("test2.txt")) == 19208
end

# Part 1
partOne(file="input.txt") = count(g->(g == 1), FindGaps(LoadAdapters(file))) * count(g->(g == 3), FindGaps(LoadAdapters(file)))

@test partOne("test.txt") == 35
@test partOne("test2.txt") == 220
@test partOne() == 1917
println(string("Part one: ", partOne()))

# Part 2
partTwo(file="input.txt") = BrettsWay(LoadAdapters(file), 3)

@test partTwo("test.txt") == 8
@test partTwo("test2.txt") == 19208
@test partTwo() == 113387824750592
println(string("Part two: ", partTwo()))
