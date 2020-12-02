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
    min::Int64
    max::Int64
    letter:: Char
    pass:: String
end

function validPassword(passString)

    m = match(r"(?<min>\d+)-(?<max>\d+) (?<letter>\D+): (?<pass>\w+)", passString)
    minCnt, maxCnt, letter, pass = m.captures
    passWord = PassWord(parse(Int64, minCnt), parse(Int64, maxCnt), letter[1], pass)

    cnt = count(i->(i == passWord.letter), passWord.pass)

    return passWord.min <= cnt <= passWord.max

end

function validPassword2(passString)

    m = match(r"(?<min>\d+)-(?<max>\d+) (?<letter>\D+): (?<pass>\w+)", passString)
    minCnt, maxCnt, letter, pass = m.captures
    passWord = PassWord(parse(Int64, minCnt), parse(Int64, maxCnt), letter[1], pass)

    cnt = count(i->(i == passWord.letter), passWord.pass)

    return (passWord.pass[passWord.min] == passWord.letter && passWord.pass[passWord.max] != passWord.letter) || (passWord.pass[passWord.min] != passWord.letter && passWord.pass[passWord.max] == passWord.letter)

end

function partOne(list)
    count = 0
    for input in list
        if validPassword(input)
            count += 1
        end
    end
    return count
end

function partTwo(list)
    count = 0
    for input in list
        if validPassword2(input)
            count += 1
        end
    end
    return count
end


println(partOne(inputdata))
println(partTwo(inputdata))

# end # module