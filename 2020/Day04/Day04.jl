# Day 4 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/4
# 

using DelimitedFiles
using Test

# Test information from the puzzle
testinput = ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f",
"",
"eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
"",
"eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
"",
"iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946",
"",
"hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
"",
"hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007",
"",
"hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022",
"",
"iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",]

# Actual personallized data

inputdata = readdlm("input.txt", '\t', String, '\n', skipblanks=false)


# pos(x,y,l) = x*(y-1)%l+1

# function Slope(right::Int64, down::Int64, inputList::Array)
#     trees = 0
#     for (i,input) in enumerate(inputList[1:down:end])
#         trees += input[pos(right, i, length(input))] == '#' ? 1 : 0
#     end
#     trees
# end

struct PassPort
    byr # (Birth Year)
    iyr # (Issue Year)
    eyr # (Expiration Year)
    hgt # (Height)
    hcl # (Hair Color)
    ecl # (Eye Color)
    pid # (Passport ID)
    cid # (Country ID)
    fields # Dict containing all fields
    function PassPort(raw)
        # "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
        fields = split.(split(raw), ':')
        d = Dict(fields[i][1]=>fields[i][2] for i in 1:1:length(fields))
        new( 
            parse(Int, get(d,"byr", "0")), 
            parse(Int, get(d,"iyr", "0")), 
            parse(Int, get(d,"eyr", "0")), 
            get(d,"hgt", ""), 
            get(d,"hcl", ""), 
            get(d,"ecl", ""), 
            get(d,"pid", ""), 
            get(d,"cid", ""), 
            d)
    end
end

function IsValidHeight(heightString)
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    m = match(r"^(?<height>\d+)(?<unit>\D{2})$", heightString)
    if m != nothing
        ( m["unit"] == "cm" && 150 <= parse(Int, m["height"]) <= 193) || 
        ( m["unit"] == "in" &&  59 <= parse(Int, m["height"]) <=  76) 
    else
        false
    end
end
function IsFieldsPresent(pass::PassPort)
    pass.byr > 0 && 
    pass.iyr > 0  && 
    pass.eyr > 0 && 
    pass.hgt != "" && 
    pass.hcl != "" && 
    pass.ecl != "" && 
    pass.pid != ""

end

function IsValid(pass::PassPort)

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    1920 <= pass.byr <= 2002 &&
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    2010 <= pass.iyr <= 2020 &&
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    2020 <= pass.eyr <= 2030 &&
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    IsValidHeight(pass.hgt) &&
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    occursin(r"^#[0-9,a-f]{6}$", pass.hcl) &&
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pass.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] &&
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    occursin(r"^\d{9}$", pass.pid)
    # cid (Country ID) - ignored, missing or not.

end

function CleanUpInput(input)
    chunk = []
    output = []
    for item in input
        if item == ""
            push!(output, join(chunk, ' '))
            empty!(chunk)
        else
            push!(chunk, item)
        end
    end
    push!(output, join(chunk, ' '))
    # output
end

# Part 1
function partOne(rawList)
    list = CleanUpInput(rawList)
    passports = [PassPort(list[i]) for i in 1:length(list)]
    count(p->IsFieldsPresent(p), passports)
end

@test partOne(testinput) == 8
@test partOne(inputdata) == 202
println(string("Part one: ", partOne(inputdata)))

# Part 2
function partTwo(rawList)
    list = CleanUpInput(rawList)
    passports = [PassPort(list[i]) for i in 1:length(list)]
    count(p->(IsValid(p) && IsFieldsPresent(p)), passports)
end

@test partTwo(testinput) == 4
@test partTwo(inputdata) == 137
println(string("Part two: ", partTwo(inputdata)))
