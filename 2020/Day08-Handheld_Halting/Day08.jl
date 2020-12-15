# Day 8 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/8
#
# using DelimitedFiles
using Test

mutable struct Instruction
    oper :: String
    arg  :: Int
    Instruction(o,a) = new(o,a)
end

mutable struct Cpu 
    ptr :: Int
    acc :: Int
    exeLog :: Vector{Int}
    program :: Vector{Instruction}
    Cpu(p=1,a=0) = new(p,a,[],[])
end

function AddInst(i::Instruction,c::Cpu)
    push!(c.program, i)
end

function LoadComputer(file="input.txt")
    cpu = Cpu()
    for i in readlines(file)
        oper,arg = split(i)
        inst = Instruction(oper,parse(Int,arg))
        AddInst(inst, cpu)
    end
    cpu
end
@testset "LoadProgram" begin
    cpu = LoadComputer("testdata.txt")
    @test cpu.program[1].oper == "nop"
    @test cpu.program[1].arg == 0
    @test cpu.program[5].oper == "jmp"
    @test cpu.program[5].arg == -3
    @test cpu.program[9].oper == "acc"
    @test cpu.program[9].arg == 6
end

function Execute(cpu :: Cpu)
    oper = cpu.program[cpu.ptr]
    push!(cpu.exeLog,cpu.ptr)
    if oper.oper == "nop"
        cpu.ptr +=1
    elseif oper.oper == "acc"
        cpu.acc += oper.arg
        cpu.ptr +=1
    elseif oper.oper == "jmp"
        cpu.ptr += oper.arg
    end
    cpu
end
@testset "RunProgram" begin
    cpu = LoadComputer("testdata.txt")
    @test Execute(cpu).ptr == 2
    @test Execute(cpu).acc == 1
    @test Execute(cpu).ptr == 7
end

function RestartProgram(cpu::Cpu)
    cpu.ptr = 1
    cpu.acc = 0
    empty!(cpu.exeLog)
end

function RunToEnd(cpu :: Cpu)
    RestartProgram(cpu)
    while (cpu.ptr in cpu.exeLog) == false  && 0 < cpu.ptr <= length(cpu.program)
        lastPtr = cpu.ptr
        Execute(cpu)
    end
    (cpu, cpu.ptr == length(cpu.program) + 1) 
end
@testset "RunToEnd" begin
    @test RunToEnd(LoadComputer("testdata.txt"))[1].acc == 5
    cpu = LoadComputer("testdata.txt")
    result = RunToEnd(cpu)
    @test result[2] == false
    @test cpu.acc == 5
    cpu = LoadComputer("testdata2.txt")
    result = RunToEnd(cpu)
    @test result[2] == true
    @test result[1] == cpu
    @test cpu.acc == 8
end

function SwapInst(cpu :: Cpu, ptr :: Int)
    if cpu.program[ptr].oper == "nop"
        cpu.program[ptr].oper = "jmp"
    elseif cpu.program[ptr].oper == "jmp"
        cpu.program[ptr].oper = "nop"
    end
end
@testset "SwapInst" begin
    cpu = Cpu()
    AddInst(Instruction("acc", 0), cpu)
    AddInst(Instruction("jmp", 0), cpu)
    AddInst(Instruction("nop", 0), cpu)
    SwapInst(cpu, 1)
    @test cpu.program[1].oper == "acc"
    SwapInst(cpu, 2)
    @test cpu.program[2].oper == "nop"
    SwapInst(cpu, 3)
    SwapInst(cpu, 3)
    @test cpu.program[3].oper == "nop"
end

function FixAndRun(cpu :: Cpu)
    result = RunToEnd(cpu)
    backtrack = copy(cpu.exeLog)

    while result[2] == false && length(backtrack) > 0
        changedInstruction = pop!(backtrack)
        SwapInst(cpu, changedInstruction)
        result = RunToEnd(cpu)
        SwapInst(cpu, changedInstruction)
    end
    result[1]
end

@test FixAndRun(LoadComputer("testdata.txt")).acc == 8

# Part 1
partOne(file="input.txt") = RunToEnd(LoadComputer(file))[1].acc

@test partOne("testdata.txt") == 5
@test partOne() == 1262
println(string("Part one: ", partOne()))

# Part 2
partTwo(file="input.txt") = FixAndRun(LoadComputer(file)).acc

@test partTwo() == 1643
println(string("Part two: ", partTwo()))
