# Day 12 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/12
#
# using DelimitedFiles
using Test

mutable struct Instruction
    oper :: Char
    arg  :: Int
    Instruction(o,a) = new(o,a)
end

mutable struct Waypoint 
    ns :: Int
    ew :: Int
    # dir :: Char
    Waypoint(a=-1, b=10, d='e') = new(a,b)
end

mutable struct Ferry 
    ptr :: Int
    ns :: Int
    ew :: Int
    dir :: Char
    wp :: Waypoint
    pathLog :: Vector{Int}
    path :: Vector{Instruction}
    Ferry(p=1,a=0, b=0, d='e', wp=Waypoint()) = new(p,a,b,d,wp,[],[])
end


function AddInst(i::Instruction,c::Ferry)
    push!(c.path, i)
end

function LoadPath(file="input.txt")
    ferry = Ferry()
    for i in readlines(file)
        oper = i[1]
        arg = i[2:end]
        inst = Instruction(oper,parse(Int,arg))
        AddInst(inst, ferry)
    end
    ferry
end
@testset "LoadPath" begin
    cpu = LoadPath("testdata.txt")
    @test cpu.path[1].oper == 'F'
    @test cpu.path[1].arg == 10
    @test cpu.path[5].oper == 'F'
    @test cpu.path[5].arg == 11
    @test cpu.path[4].oper == 'R'
    @test cpu.path[4].arg == 90
end

function TurnWaypoint(lr :: Char, deg :: Int, f :: Ferry)
    ns = f.wp.ns
    ew = f.wp.ew
    # R90, L270, R180
    if deg == 180
        f.wp.ns *= -1
        f.wp.ew *= -1
    elseif lr == 'R' && deg == 90 || lr == 'L' && deg == 270
        f.wp.ns = ew
        f.wp.ew = ns * -1
    elseif lr == 'L' && deg == 90 || lr == 'R' && deg == 270
        f.wp.ns = ew * -1
        f.wp.ew = ns
    end
end
@testset "TurnWaypoint" begin
    f = Ferry() # ns = 0, ew = 0
    # f.wp : ns = -1, ew = 10
    @test f.dir == 'e'
    TurnWaypoint('R',  90, f)
    @test f.wp.ns == 10
    @test f.wp.ew == 1
    TurnWaypoint('R',  180, f)
    @test f.wp.ns == -10
    @test f.wp.ew == -1
    TurnWaypoint('L',  180, f)
    @test f.wp.ns == 10
    @test f.wp.ew == 1
end

function RotateWayPoint(lr :: Char, deg :: Int, f :: Ferry)
    ns = f.wp.ns
    ew = f.wp.ew
    # R90, L270, R180
    deg = lr == 'L' ? 360 - deg : deg
    f.wp.ew = round(Int, cosd(deg) * ew - sind(deg) * ns)
    f.wp.ns = round(Int, sind(deg) * ew + cosd(deg) * ns)
end
@testset "RotateWayPoint" begin
    f = Ferry() # ns = 0, ew = 0
    # f.wp : ns = -1, ew = 10
    @test f.dir == 'e'
    RotateWayPoint('R',  90, f)
    @test f.wp.ns == 10
    @test f.wp.ew == 1
    RotateWayPoint('R', 180, f)
    @test f.wp.ns == -10
    @test f.wp.ew == -1
    RotateWayPoint('L', 180, f)
    @test f.wp.ns == 10
    @test f.wp.ew == 1
    RotateWayPoint('L',  90, f)
    @test f.wp.ns == -1
    @test f.wp.ew == 10
end


function TurnFerry(lr :: Char, deg :: Int, f :: Ferry)
    # R90, L270, R180
    dirs = "NESW"

    p = first(findfirst(string(f.dir), lowercase(dirs)))
    d = trunc(Int, deg / 90)
    if lr == 'R'
        f.dir = lowercase(dirs)[mod(p+d-1,4)+1]
    elseif lr == 'L'
        f.dir = lowercase(dirs)[mod(p-d-1+4, 4)+1]
    end
    f
end
@testset "TurnFerry" begin
    f = Ferry()
    @test f.dir == 'e'
    @test TurnFerry('R', 90, f).dir == 's'
    @test TurnFerry('R', 180, f).dir == 'n'
    @test TurnFerry('R', 270, f).dir == 'w'
    @test TurnFerry('L', 90, f).dir == 's'
    @test TurnFerry('L', 180, f).dir == 'n'
    @test TurnFerry('L', 270, f).dir == 'e'
end

function Execute(ferry :: Ferry)
    oper = ferry.path[ferry.ptr]
    push!(ferry.pathLog,ferry.ptr)
    if oper.oper == 'F'
        if ferry.dir == 'n' ferry.ns -= oper.arg end
        if ferry.dir == 's' ferry.ns += oper.arg end
        if ferry.dir == 'e' ferry.ew += oper.arg end
        if ferry.dir == 'w' ferry.ew -= oper.arg end
    elseif oper.oper == 'N'
        ferry.ns -= oper.arg
    elseif oper.oper == 'S'
        ferry.ns += oper.arg
    elseif oper.oper == 'E'
        ferry.ew += oper.arg
    elseif oper.oper == 'W'
        ferry.ew -= oper.arg
    elseif oper.oper in "LR"
        TurnFerry(oper.oper, oper.arg, ferry)
    end
    ferry.ptr +=1
    ferry
end
@testset "RunProgram" begin
    ferry = LoadPath("testdata.txt")
    @test Execute(ferry).ptr == 2
    @test Execute(ferry).ns == -3
    @test ferry.ew == 10
    @test Execute(ferry).ew == 17
    @test Execute(ferry).dir == 's'
    @test (ferry.ns,ferry.ew) == (-3, 17)

end

function MoveToWaypoint(arg::Int, f::Ferry)
    f.ns += arg * f.wp.ns
    f.ew += arg * f.wp.ew
    f
end

function ExecuteByWaypoint(ferry :: Ferry)
    oper = ferry.path[ferry.ptr]
    push!(ferry.pathLog,ferry.ptr)
    if oper.oper == 'F'
        MoveToWaypoint(oper.arg, ferry)
    elseif oper.oper == 'N'
        ferry.wp.ns -= oper.arg
    elseif oper.oper == 'S'
        ferry.wp.ns += oper.arg
    elseif oper.oper == 'E'
        ferry.wp.ew += oper.arg
    elseif oper.oper == 'W'
        ferry.wp.ew -= oper.arg
    elseif oper.oper in "LR"
        RotateWayPoint(oper.oper, oper.arg, ferry)
    end
    ferry.ptr +=1
    ferry
end
@testset "ExecuteByWaypoint" begin
    ferry = LoadPath("testdata.txt")
    ExecuteByWaypoint(ferry) # First step F10
    @test ferry.ptr == 2
    @test ferry.ew == 100
    @test ferry.ns == -10
    ExecuteByWaypoint(ferry) # Second step N3
    @test ferry.ew == 100 
    @test ferry.ns == -10
    @test ferry.wp.ns == -4
    @test ferry.wp.ew == 10
    ExecuteByWaypoint(ferry) # Third step F7
    @test ferry.ew == 170 && ferry.ns == -38
    @test ferry.wp.ns == -4
    @test ferry.wp.ew == 10
    ExecuteByWaypoint(ferry) # Forth step R90
    @test ferry.ew == 170 && ferry.ns == -38
    @test ferry.wp.ns == 10
    @test ferry.wp.ew == 4
    ExecuteByWaypoint(ferry) # Fifth step F11
    @test ferry.wp.ns == 10 && ferry.wp.ew == 4
    @test ferry.ew == 214 
    @test ferry.ns == 72

end

function RestartProgram(f::Ferry)
    f.ptr = 1
    f.ns = 0
    f.ew = 0
    empty!(f.pathLog)
end

function RunToEnd(f :: Ferry)
    RestartProgram(f)
    while (f.ptr in f.pathLog) == false  && 0 < f.ptr <= length(f.path)
        lastPtr = f.ptr
        Execute(f)
    end
    (f, f.ptr == length(f.path) + 1) 
end
@testset "RunToEnd" begin
    @test RunToEnd(LoadPath("testdata.txt"))[1].ew == 17
    @test RunToEnd(LoadPath("testdata.txt"))[1].ns == 8
end


function RunByWaypointToEnd(f ::Ferry)
    RestartProgram(f)
    while (f.ptr in f.pathLog) == false  && 0 < f.ptr <= length(f.path)
        lastPtr = f.ptr
        ExecuteByWaypoint(f)
    end
    (f, f.ptr == length(f.path) + 1) 
end

@testset "RunByWaypointToEnd" begin
    @test RunByWaypointToEnd(LoadPath("testdata.txt"))[1].ew == 214
    @test RunByWaypointToEnd(LoadPath("testdata.txt"))[1].ns == 72
end

# Part 1
function partOne(file="input.txt")
    f = RunToEnd(LoadPath(file))[1]
    abs(f.ew) + abs(f.ns)
end

@test partOne("testdata.txt") == 25
@test partOne() == 445
println(string("Part one: ", partOne()))

# Part 2
function partTwo(file="input.txt")
    f = RunByWaypointToEnd(LoadPath(file))[1]
    abs(f.ew) + abs(f.ns)
end

@test partTwo("testdata.txt") == 286
@test partTwo() == 42495
println(string("Part two: ", partTwo()))
