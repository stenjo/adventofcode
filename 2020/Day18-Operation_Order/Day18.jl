# Day 18 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/18
#
using Test
using Match
using BenchmarkTools

function GetSubStatement(str::SubString{String})
    openCnt = 0
    for (i,n) in enumerate(str)
        if n == '('
            openCnt += 1
        elseif n == ')' 
            if openCnt == 0
                return str[1:i-1]
            else
                openCnt -= 1
            end
        end
    end
    str
end


function DoOperation(oper::Char, value1::Int, value2::Int)
    result = 0
    @match oper begin
        '+' => (result = value1 + value2)
        '-' => (result = value1 - value2)
        '*' => (result = value1 * value2)
         _  => println("Unknown operation: ", oper)
    end
    result
end

function Evaluate(line)
    statements = strip(filter(c->c!=' ',line))
    result = 0
    while length(statements) > 0
        if statements[1] == '('
            sub = GetSubStatement(statements[2:end])
            result = Evaluate(sub)
            statements = statements[length(sub)+3:end]
        elseif statements[1] in join(string.(Array(0:9)))
            result = parse(Int, statements[1])
            statements = statements[2:end]
        elseif statements[1] in "+*-" && statements[2] == '('
            sub = GetSubStatement(statements[3:end])
            value = Evaluate(sub)
            result = DoOperation(statements[1], result, value)
            statements = statements[length(sub)+4:end]
        elseif statements[1] in "+*-" && parse(Int, statements[2]) in 1:9
            result = DoOperation(statements[1], result, parse(Int, statements[2]))
            statements = statements[3:end]
        end
    end
    result
end

@testset "Evaluate" begin
    @test DoOperation('+', 3, 9) == 12
    @test DoOperation('-', 3, 9) == -6
    @test DoOperation('*', 3, 9) == 27
    @test Evaluate("1 + 2 * 3 + 4 * 5 + 6") == 71
    @test Evaluate("1 + (2 * 3) + (4 * (5 + 6))") == 51
    @test Evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    @test Evaluate("2 * 3 + (4 * 5)") == 26
    @test Evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    @test Evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
end

function HasPrecedence(op, rel)
    if op == '+' && rel == '*'
        return true
    end
    return false
end

function ShuntingYard(line)
    statements = strip(filter(c->c!=' ',line))
    output = []
    operator = []
    for (i,t) in enumerate(statements)
        if t in join(string.(Array(0:9)))
            push!(output, parse(Int, t))
        elseif t in "+-*/"
            while length(operator) > 0 && HasPrecedence(operator[end], t) && t != '('
                push!(output, pop!(operator))
            end
            push!(operator, t)
        elseif t == '('
            push!(operator, t)
        elseif t == ')'
            while length(operator) > 0 && operator[end] != '('
                push!(output, pop!(operator))
            end
            if operator[end] == '('
                pop!(operator)
            end
        end
    end
    while length(operator) > 0
        push!(output, pop!(operator))
    end

    output
end

function SolveReversePolish(line)
    values = []
    for c in ShuntingYard(line)
        @match c begin
            0:9 => push!(values, c)
            '*' => push!(values, pop!(values) * pop!(values))
            '+' => push!(values, pop!(values) + pop!(values))
            _ => println("Unknown")
        end
    end
    pop!(values)
end


@testset "SolveReversePolish" begin
    @test ShuntingYard("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == [5, 9, 7, 3, 3, 9, '+', 3, 8, 6, '+', 4, '*', '+', '*', '*', '*', '*', '*']
    @test SolveReversePolish("(1 + 2) * (3 + 4) * 5 + 6") == 231
    @test SolveReversePolish("1 + (2 * 3) + (4 * (5 + 6))") == 51
    @test SolveReversePolish("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 1445
    @test SolveReversePolish("(2 * 3 + (4 * 5))") == 46
    @test SolveReversePolish("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 669060
    @test SolveReversePolish("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 23340
end


# Part 1
partOne(file="input.txt") = sum(map(v->Evaluate(v), readlines(file)))

@test partOne("test.txt") == 26335
@test partOne() == 18213007238947

println(string("Part one: ", partOne()))
@time partOne()

# # Part 2
partTwo(file="input.txt") = sum(map(v->SolveReversePolish(v), readlines(file)))

@test partTwo("test.txt") == 693891
@test partTwo() == 388966573054664

println(string("Part two: ", partTwo())) # Answer too high
@time partTwo()
