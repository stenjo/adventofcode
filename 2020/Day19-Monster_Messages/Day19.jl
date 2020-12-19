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

function CompileRules(rules)
    cRules = Dict()
    for rule in rules  ## Find strings
        println(rule[2].patterns)
        # findall(v->( 4 in collect(Iterators.flatten(vcat.(v.ref)))), rules)
    end
end


function IsMatch(str, rules)

end

@testset "IsMatch" begin

end

# Part 1
# partOne(file="input.txt") = sum(map(v->Evaluate(v), readlines(file)))

# @test partOne("test.txt") == 26335
# @test partOne() == 18213007238947

# println(string("Part one: ", partOne()))
# @time partOne()

# # Part 2
# partTwo(file="input.txt") = sum(map(v->SolveReversePolish(v), readlines(file)))

# @test partTwo("test.txt") == 693891
# @test partTwo() == 388966573054664

# println(string("Part two: ", partTwo())) # Answer too high
# @time partTwo()
