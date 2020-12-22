# Day 2 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/2
# 
using DelimitedFiles
using Test
using BenchmarkTools

testinput = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

inputdata = readdlm("input.txt", '\t', String, '\n')

struct PassWord 
    first :: Int
    last :: Int
    letter :: Char
    pass :: String
    
    function PassWord(passwordline:: String)
        m = match(r"(?<first>\d+)-(?<last>\d+) (?<letter>\D+): (?<pass>\w+)", passwordline)
        new(parse(Int, m["first"]), parse(Int, m["last"]), m["letter"][1], m["pass"])
    end
end

# Part 1
ValidPassWord(f::PassWord) = f.first <= count(i->(i == f.letter), f.pass) <= f.last

partOne(list=inputdata) = count(ValidPassWord.(PassWord.(list)))

@test partOne(testinput) == 2   # According to the puzzle text
@test partOne(inputdata) == 410   # According to the puzzle text

println("Part one: ", partOne(inputdata))
@time partOne()

# Part 2
ValidPassWord2(f::PassWord) = (f.pass[f.first] == f.letter && f.pass[f.last] != f.letter) || (f.pass[f.first] != f.letter && f.pass[f.last] == f.letter)

partTwo(list=inputdata) = count(ValidPassWord2.(PassWord.(list)))

@test partTwo(testinput) == 1
@test partTwo() == 694

println("Part two: ", partTwo(inputdata))
@time partTwo()
