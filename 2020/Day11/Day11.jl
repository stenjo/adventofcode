# Day 11 of Advent of Code puzzle: 
# https://adventofcode.com/2020/day/11
# 

using BenchmarkTools
using DelimitedFiles
using Test

# Actual personallized data
SwapSeat(c) = c == 'L' ? '#' : c == '#' ? 'L' : c

@test SwapSeat('L') == '#'
@test SwapSeat('#') == 'L'
@test SwapSeat('.') == '.'

function OccupiedSeats(index, row)
    b = index <= 1 ? 1 : index - 1
    e = index >= length(row) ? length(row) : index + 1

    sum(x->x == '#', row[b:e])
end

@test OccupiedSeats(3, "L.LL.LL.LL") == 0
@test OccupiedSeats(3, "#.##.##.##") == 2
@test OccupiedSeats(3, "#######.##") == 3
@test OccupiedSeats(5, "#.##.##.##") == 2
@test OccupiedSeats(1, "#.##.##.##") == 1
@test OccupiedSeats(10, "#.##.##.##") == 2


function AdjacentOccupiedSeats(colNum, rowNum, seats)
    l = length(seats)
    if rowNum == 1
        OccupiedSeats(colNum, seats[1]) + OccupiedSeats(colNum, seats[2])
    elseif rowNum == l
        OccupiedSeats(colNum, seats[l]) + OccupiedSeats(colNum, seats[l-1])
    else
        OccupiedSeats(colNum, seats[rowNum-1]) + OccupiedSeats(colNum, seats[rowNum]) + OccupiedSeats(colNum, seats[rowNum+1])
    end
end

@test AdjacentOccupiedSeats(2, 2, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 6
@test AdjacentOccupiedSeats(1, 1, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 2
@test AdjacentOccupiedSeats(3, 2, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 6
@test AdjacentOccupiedSeats(10, 3, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 2
@test AdjacentOccupiedSeats(6, 3, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 2
@test AdjacentOccupiedSeats(5, 1, ["#L##.##.L#","#.##.LL.LL","#.###L#.##"]) == 3

function RunRound(seats)
    newSeats = []
    for (n,row) in enumerate(seats)
        newRow = ""
        for (r,s) in enumerate(row)
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if s == 'L' && AdjacentOccupiedSeats(r, n, seats) == 0
                newRow *= SwapSeat(s)
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            elseif s == '#' && AdjacentOccupiedSeats(r, n, seats) >= 5 # seatLine[i-1] != '#' && seatLine[i+1] != '#'
                newRow *= SwapSeat(s)
            else
            # Otherwise, the seat's state does not change.
                newRow *= s
            end
            # println(s)
        end
        push!(newSeats, newRow)
    end
    newSeats
end
@testset "RunRound" begin
    testSeats = readlines("test.txt")
    @test RunRound(["#.LL.L#.##","#LLLLLL.L#"]) == ["#.##.L#.##","#L###LL.L#"]
    @test RunRound(testSeats)[3] == "#.#.#..#.."
    @test RunRound(RunRound(testSeats))[3] == "L.L.L..L.."
    @test RunRound(RunRound(RunRound(testSeats)))[3] == "L.#.#..#.."
    @test RunRound(RunRound(RunRound(RunRound(testSeats))))[3] == "L.L.L..#.."
end

function RunToEndPart1(file="input.txt")
    inputSet = readlines(file)
    resultSet = RunRound(inputSet)

    while resultSet != inputSet
        inputSet = resultSet
        resultSet = RunRound(inputSet)
    end

    resultSet
end

function SeatAt(dir, col, row, hall)
    # Sanity check
    if  !(1 <= row <= length(hall)) || 
        !(1 <= col <= length(hall[row])) ||
        'N' in dir && row <= 1 || 
        'S' in dir && row >= length(hall) || 
        'W' in dir && col <= 1 || 
        'E' in dir && col >= length(hall[row])
        return 'X'
    end 

    row += 'N' in dir ? -1 : 'S' in dir ? 1 : 0
    col += 'W' in dir ? -1 : 'E' in dir ? 1 : 0
    
    return hall[row][col]
end

@testset "SeatAt" begin
    t = [['1','2','3'],['4','5','6'],['7','8','9']]
    @test SeatAt( "N",2,2, t) == '2'
    @test SeatAt("NE",2,2, t) == '3'
    @test SeatAt( "E",2,2, t) == '6'
    @test SeatAt("SE",2,2, t) == '9'
    @test SeatAt( "S",2,2, t) == '8'
    @test SeatAt("SW",2,2, t) == '7'
    @test SeatAt( "W",2,2, t) == '4'
    @test SeatAt("NW",2,2, t) == '1'
    @test SeatAt( "N",1,1, t) == 'X'
    @test SeatAt( "NW",1,1, t) == 'X'
    @test SeatAt( "S",1,3, t) == 'X'
    @test SeatAt( "SE",3,3, t) == 'X'
    @test SeatAt( "N",3,3, t) == '6'
end

function LineOfSight(seat :: Char, col :: Int, row :: Int, hall, dir :: String)
    # Sanity check
    if !(1 <= row <= length(hall)) || !(1 <= col <= length(hall[row]))
        return 0
    end
    
    # Find seat
    c = SeatAt(dir, col, row, hall) 

    # Prepare next position
    row += 'S' in dir ? 1 : 'N' in dir ? -1 : 0
    col += 'E' in dir ? 1 : 'W' in dir ? -1 : 0

    # Recursive in the direction
    c == seat ? 1 : c in "XL" ? 0 : LineOfSight(seat, col, row, hall, dir)

end

@testset "LineOfSight" begin
    @test LineOfSight('#', 4, 5, readlines("test21.txt"), "NW") == 1
end

LineOfSightOccupiedSeats(column, row, seats) = sum(dir->LineOfSight('#', column, row, seats, dir), ["N", "NE", "E", "SE", "S", "SW", "W", "NW"])

@testset "LineOfSightOccupiedSeats" begin
    @test LineOfSightOccupiedSeats(4, 5, readlines("test21.txt")) == 8
    @test LineOfSightOccupiedSeats(2, 2, readlines("test22.txt")) == 0
    @test LineOfSightOccupiedSeats(4, 4, readlines("test23.txt")) == 0
end

function RunRoundPart2(seats)
    newSeats = []
    for (r,row) in enumerate(seats)
        newRow = ""
        for (c,s) in enumerate(row)
            if s in "L#"
                os = LineOfSightOccupiedSeats(c, r, seats)
                if s == 'L' && os == 0
                    # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                    newRow *= '#'
                elseif s == '#' && os >= 5
                    newRow *= 'L'
                else
                    # Otherwise, the seat's state does not change.
                    newRow *= s
                end
            else
                # Otherwise, the seat's state does not change.
                newRow *= s
            end
        end
        push!(newSeats, newRow)
    end
    newSeats
end
@testset "RunRoundPart2" begin
    testSeats = readlines("test.txt")
    @test RunRoundPart2(testSeats)[3] == "#.#.#..#.."
    @test RunRoundPart2(RunRoundPart2(testSeats))[3] == "L.L.L..L.."
    @test RunRoundPart2(RunRoundPart2(RunRoundPart2(testSeats)))[3] == "L.#.#..#.."
    @test RunRoundPart2(RunRoundPart2(RunRoundPart2(RunRoundPart2(testSeats))))[3] == "L.L.L..#.."
end

function RunToEndPart2(file="input.txt")
    inputSet = readlines(file)
    resultSet = RunRoundPart2(inputSet)

    while resultSet != inputSet
        inputSet = resultSet
        resultSet = RunRoundPart2(inputSet)
    end

    resultSet
end


# Part 1
partOne(file = "input.txt") = count(x->x == '#', join(join.(RunToEndPart1(file))))
@test partOne("test.txt") == 37
@test partOne() == 2321
println(string("Part one: ", partOne()))

# Part 2
partTwo(file = "input.txt") = count(x->x == '#', join(join.(RunToEndPart2(file))))

@test partTwo("test.txt") == 26
@test partTwo() == 2102
println(string("Part two: ", partTwo()))

# stats = Dict()
# jbench = @benchmark partOne()
# stats["partOne"] = minimum(jbench.times)/1e6
# jbench = @benchmark partTwo()
# stats["partTwo"] = minimum(jbench.times)/1e6

# for (key, value) in sort(collect(stats), by=last)
#     println(rpad(key, 10, " "), lpad(round(value; digits=1), 6, " "), " s")
# end
