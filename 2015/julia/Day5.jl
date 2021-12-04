using Base
using Test
using BenchmarkTools
using MD5


function HasThreeVowels(str)
    v = 0
    for (i,c) in enumerate(str)
        if c in "aeiouy"
            v += 1
        end
    end

    if v > 2
        return true
    end

    return false
end

function ContainsDoubleLetters(str)
    chr = '.'
    for (i,c) in enumerate(str)
        if c == chr
            return true
        end
        chr = c
    end

    false
end

function HasSubStrings(str)
    noList = ["ab", "cd", "pq", "xy"]

    for p in noList
        if occursin(p, str)
            return true
        end
    end

    false
end


function NiceString(str)

    if HasThreeVowels(str) == true && ContainsDoubleLetters(str) == true && HasSubStrings(str) == false
        return true
    end
    false
end

@test NiceString("ugknbfddgicrmopn") == true
@test NiceString("aaa") == true
@test NiceString("jchzalrnumimnmhp") == false
@test NiceString("haegwjzuvuyypxyu") == false
@test NiceString("dvszwmarrgswjxmb") == false

function CountNice(strings = readlines("day05.txt"))

    nice = 0
    for l in strings
        if NiceString(l) == true && length(l) > 2
            nice += 1
        end
    end
    return nice
end

@test CountNice(["3"]) == 0

CountNice()
