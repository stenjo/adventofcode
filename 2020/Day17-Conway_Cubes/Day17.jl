# Day 17 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/17
#
# using DelimitedFiles
using Test
using BenchmarkTools
# using Primes

function LoadInitial(file="input.txt")
    lines=readlines(file)
    a = falses(length(lines[1]), length(lines), 1)
    for y in 1:length(lines), x in 1:length(lines[y])
        if lines[y][x] == '#'
            a[y,x,1,1] = true 
        end
    end
    a
end

function Cycle(a)
    dimX = length(view(a, :, 1, 1))
    dimY = length(view(a, 1, :, 1))
    dimZ = length(view(a, 1, 1, :))

    A = falses(dimX+2, dimY+2, dimZ+2)
    for x in 1:dimX, y in 1:dimY, z in 1:dimZ
        A[x+1, y+1, z+1] = a[x,y,z]
    end

    b = falses(dimX+2, dimY+2, dimZ+2)

    for x in 1:dimX+2, y in 1:dimY+2, z in 1:dimZ+2
        dx = (x-1 <= 1 ? 1 : x-1):(x+1 >= dimX+2 ? dimX+2 : x+1)
        dy = (y-1 <= 1 ? 1 : y-1):(y+1 >= dimY+2 ? dimY+2 : y+1)
        dz = (z-1 <= 1 ? 1 : z-1):(z+1 >= dimZ+2 ? dimZ+2 : z+1)
        cnt = count(view(A,dx,dy,dz))
        active = A[x,y,z]
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        if active == true && cnt-1 in [2,3]
            b[x, y, z] = true
        else
            b[x, y, z] = false
        end

        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        if active == false && cnt == 3
            b[x, y, z] = true
        end
    end
    b
end

function Cycle4Dim(a)
    dimX = length(view(a, :, 1, 1, 1))
    dimY = length(view(a, 1, :, 1, 1))
    dimZ = length(view(a, 1, 1, :, 1))
    dimW = length(view(a, 1, 1, 1, :))
    
    A = falses(dimX+2, dimY+2, dimZ+2, dimW+2)
    for y in 1:dimY, x in 1:dimX, z in 1:dimZ, w in 1:dimW
        A[x+1, y+1, z+1, w+1] = a[x,y,z,w]
    end

    b = falses(dimX+2, dimY+2, dimZ+2, dimW+2)

    for x in 1:dimX+2, y in 1:dimY+2, z in 1:dimZ+2, w in 1:dimW+2
        dx = (x-1 <= 1 ? 1 : x-1):(x+1 >= dimX+2 ? dimX+2 : x+1)
        dy = (y-1 <= 1 ? 1 : y-1):(y+1 >= dimY+2 ? dimY+2 : y+1)
        dz = (z-1 <= 1 ? 1 : z-1):(z+1 >= dimZ+2 ? dimZ+2 : z+1)
        dw = (w-1 <= 1 ? 1 : w-1):(w+1 >= dimW+2 ? dimW+2 : w+1)
        cnt = count(view(A,dx,dy,dz,dw))
        active = A[x,y,z,w]
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
        if active == true && cnt-1 in [2,3]
            b[x, y, z, w] = true
        else
            b[x, y, z, w] = false
        end
        # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
        if active == false && cnt == 3
            b[x, y, z, w] = true
        end
    end
    b
end

# Part 1
function partOne(cycles=6, file="input.txt")
    a = LoadInitial(file)
    for i in 1:cycles
        a = Cycle(a)
    end
    count(a)
end

@test partOne(6,"test.txt") == 112
@test partOne() == 338

println(string("Part one: ", partOne()))
@time partOne()

# Part 2
function partTwo(cycles=6, file="input.txt")
    a = LoadInitial(file)
    for i in 1:cycles
        a = Cycle4Dim(a)
    end
    count(a)
end

@test partTwo(6,"test.txt") == 848
@test partTwo() == 2440

println(string("Part two: ", partTwo())) # Answer too high
@time partTwo()
