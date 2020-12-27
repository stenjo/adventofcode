# Day 19 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/19
#
using Test
using Match
using BenchmarkTools



mutable struct Rule
    rNo :: Int
    raw :: String
    str :: String
    ref :: Array
    patterns :: Array
    function Rule(s::SubString{String}="")
        if s == ""
            new(-1, s, "", [])
        else
            components = pop!(split(strip(s, '\"')))
            if tryparse(Int, components) !== nothing
                # numbers
                refs = []
                for group in split(strip(s), '|')
                    subrefs = []
                    for r in split(strip(group))
                        push!(subrefs,tryparse(Int, r))
                    end
                    push!(refs,subrefs)
                end
                new(-1,s,"",refs, [])
            else
                # string
                new(-1,s,components,[],[[components]])

            end
        end
    end

end

function LoadRulesAndMessages(file="input.txt")
    lines = readlines(file)
    rules = Dict()
    msgs = []
    # Load rules
    while length(lines) > 0 
        line = popfirst!(lines)
        if line == ""   ## Found separator for messages
            break
        end
        rule = split(line, ':'; limit=2)
        rules[parse(Int, rule[1])] = Rule(strip(rule[2]))
    end

    #load messages
    while length(lines) > 0 
        line = pop!(lines)
        push!(msgs, strip(line))
    end
    rules,msgs
end

@testset "LoadRulesAndMessages" begin
    rules,messages = LoadRulesAndMessages("test.txt")
    @test length(rules) == 6
    @test length(messages) == 5
end

function GetPattern(ruleNo, rules)
    patterns = Vector{String}()
    rule = rules[ruleNo]
    if length(rule.str) > 0
        return [rule.str]
    elseif length(rule.ref) > 0
        for rSet in rule.ref
            pattern = Vector{String}()
            for r in rSet
                p = GetPattern(r,rules)
                list = []
                for (i,n) in enumerate(p)
                    if length(pattern) > 0
                        for (j,m) in enumerate(pattern)
                            push!(list,string(m, n))
                        end
                    else
                        push!(list,n)
                    end
                end
                pattern = list
            end
            for p in pattern
                push!(patterns,p)
            end
        end
    end
    return patterns
end


function BuildPatterns(rules)
    patterns = []
end


@testset "Patterns" begin
    rules,messages = LoadRulesAndMessages("test.txt")
    @test GetPattern(4,rules) == ["a"]
    @test GetPattern(5,rules) == ["b"]
    @test GetPattern(2,rules) == ["aa", "bb"]
    @test GetPattern(1,rules) == ["aaab", "bbab", "aaba", "bbba", "abaa", "baaa", "abbb", "babb"]
    @test GetPattern(0,rules) == ["aaaabb", "abbabb", "aaabab", "abbbab", "aabaab", "abaaab", "aabbbb", "ababbb"]
end

# Part 1
function partOne(file="input.txt")
    rules,messages = LoadRulesAndMessages(file)
    patterns = GetPattern(0, rules)
    count(m->(m in patterns), messages)
end

@test partOne("test.txt") == 2
@test partOne() == 118

println(string("Part one: ", partOne()))
@time partOne()

# # Part 2
# partTwo(file="input.txt") = sum(map(v->SolveReversePolish(v), readlines(file)))

# @test partTwo("test.txt") == 693891
# @test partTwo() == 388966573054664

# println(string("Part two: ", partTwo())) # Answer too high
# @time partTwo()
