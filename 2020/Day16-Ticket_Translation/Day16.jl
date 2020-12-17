# Day 16 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/16
#
# using DelimitedFiles
using Test
using BenchmarkTools
# using Primes

function Load(file)
    lines=readlines(file)
    notes=Dict("fields"=>[])
    while length(lines) > 0
        l = popfirst!(lines)
        if length(l) < 2
            continue
        end
        parts = split(l, ':')
        if length(parts) > 1
            numbers = []
            if length(parts[2]) > 0
                for r in split(strip(parts[2]), " or ")
                    range = split(r,'-')
                    numbers = vcat(numbers, Vector{Int}(parse(Int,range[1]):parse(Int,range[2])))
                end
                push!(notes["fields"], parts[1])
            else
                l = popfirst!(lines)
                while length(l) > 0
                    push!(numbers, parse.(Int, split(l, ',')))
                    if length(lines) < 1
                        l = ""
                    else
                        l = popfirst!(lines)
                    end
                end
            end
            notes[parts[1]] = numbers 
        end
    end
    notes
end

function DiscardInvalidNearbys(notes)
    valids = vcat(convert.(Array, values(filter(v->!(v[1] in ["fields", "your ticket", "nearby tickets"]), notes)))...)
    filter!(a->length(intersect(a,valids)) == length(a), notes["nearby tickets"])
    notes
end

# @testset "DiscardInvalidNearbys" begin
#     @test length(DiscardInvalidNearbys(Load("test.txt"))["nearby tickets"]) == 1
#     @test pop!(DiscardInvalidNearbys(Load("test.txt"))["nearby tickets"]) == [7,3,47]
#     @test length(DiscardInvalidNearbys(Load("test2.txt"))["nearby tickets"]) == 3
#     @test pop!(DiscardInvalidNearbys(Load("test2.txt"))["nearby tickets"]) == [5,14,9]
# end

function MapFields(notes)
    nbt = hcat(notes["nearby tickets"]...)
    fields = copy(filter(s->startswith(s, r"departure"), notes["fields"]))
    sequence = Dict()
    while length(fields) > 0
        for i in 1:length(view(nbt, :, 1))      # For each position in nearby tickets
            options = []
            for f in fields
                if all(v->v in notes[f], view(nbt, i, :))
                    push!(options, f)
                end
            end
            if length(options) == 1
                option = options[1]
                sequence[i] = option
                fields = filter(x->!(x == option), fields)
            end
            # println(i, " ", length(options), " ", options)
        end
        # println(sequence)
    end
    ticket = Dict()
    for n in 1:length(notes["your ticket"][1])
        f = get(sequence, n, "")
        if f != ""
            ticket[f] = notes["your ticket"][1][n]
        end
    end
    ticket

end

# DiscardInvalidNearbys(ticketFields)
# MapFields(Load("input2.txt"))


# Part 1
function partOne(file="input.txt")
    ticketFields = Load(file)
    valids = vcat(convert.(Array, values(filter(v->!(v[1] in ["fields", "your ticket", "nearby tickets"]), ticketFields)))...)
    nearby = vcat(ticketFields["nearby tickets"]...)
    sum(filter(v->!(v in valids), nearby))
end

@test partOne("test.txt") == 71
@test partOne() == 23954

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(file="input.txt")
    ticketFields = Load(file)
    DiscardInvalidNearbys(ticketFields)
    # MapFields(ticketFields)
    # ticketFields
    prod(values(MapFields(ticketFields)))
end

@test partTwo("test2.txt") == 208
@test partTwo() == 453459307723

println(string("Part two: ", partTwo())) # Answer too high
@time partTwo()
