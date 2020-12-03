# module Day02
# export part1, part2
# Day 2 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/2
# 

using DelimitedFiles
# include("utils.jl")

testinput = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]
inputdata = readdlm("input.txt", '\t', String, '\n')

struct PassWord 
    first::Int64
    last::Int64
    letter:: Char
    pass:: String
    
    function PassWord(passwordline:: String)
        m = match(r"(?<min>\d+)-(?<max>\d+) (?<letter>\D+): (?<pass>\w+)", passwordline)
        minCnt, maxCnt, letterString, passLine = m.captures
        new(parse(Int64, minCnt), parse(Int64, maxCnt), letterString[1], passLine)
    end

end

function ValidPassWord(f::PassWord) 
    f.first <= count(i->(i == f.letter), f.pass) <= f.last
end

function ValidPassWord2(f::PassWord)
    (f.pass[f.first] == f.letter && f.pass[f.last] != f.letter) || (f.pass[f.first] != f.letter && f.pass[f.last] == f.letter)
end

function partOne(list)
    count = 0
    for input in list
        if ValidPassWord(PassWord(input))
            count += 1
        end
    end
    return count
end

function partTwo(list)
    count = 0
    for input in list
        if ValidPassWord2(PassWord(input))
            count += 1
        end
    end
    return count
end


println(partOne(inputdata))
println(partTwo(inputdata))

# end # module