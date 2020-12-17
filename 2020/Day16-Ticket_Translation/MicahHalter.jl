# https://adventofcode.com/2020/day/16
using AdventOfCode

input = readlines("input.txt")

parse_range(r) = UnitRange(parse.(Int, split(r, "-"))...)

in_range(r, v) = any(i->v ∈ i, r)

function find_fields(fields, tickets)
    validated_fields = Set()
    possible_fields = []
    num_fields = length(tickets[1])
    for idx ∈ 1:num_fields
        push!(possible_fields, Set(filter(i->all(t->in_range(fields[i], t[idx]), tickets), keys(fields))))
    end
    while length(validated_fields) != num_fields
        for idx ∈ 1:length(possible_fields)
            if length(possible_fields[idx]) == 1
                push!(validated_fields, first(possible_fields[idx]))
            else
                setdiff!(possible_fields[idx], validated_fields)
            end
        end
    end
    Dict(first(v)=>i for (i, v) ∈ enumerate(possible_fields))
end

function parse_tickets(input)
    block = 1
    fields = Dict()
    tickets = []
    myticket = nothing
    fail_rate = 0
    for line ∈ input
        if line == ""
            block += 1
        elseif block == 1
            l, r = split(line, ": ")
            ranges = eachmatch(r"(\d+-\d+)", r)
            push!(fields, l=>map(r->parse_range(r.match), ranges))
        elseif line != "your ticket:" && line != "nearby tickets:"
            ticket = parse.(Int, split(line, ","))
            if block == 2
                myticket = ticket
            elseif block == 3
                invalid = filter(i->all(j->!in_range(j, i), values(fields)), ticket)
                if isempty(invalid)
                    push!(tickets, ticket)
                else
                    fail_rate += sum(invalid)
                end
            end
        end
    end
    fields, myticket, tickets, fail_rate
end

fields, myticket, tickets, fail_rate = parse_tickets(input)

@info fail_rate

part_2 = prod([startswith(k, "departure") ? myticket[v] : 1 for (k,v) ∈ find_fields(fields, tickets)])
@info part_2