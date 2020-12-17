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
    for y in 1:length(lines)
        for x in 1:length(lines[y])
            if lines[y][x] == '#'
                a[y,x,1,1] = true 
            end
        end
    end
    a
end

function Cycle(a)
    dimY = length(view(a, :, 1, 1))
    dimX = length(view(a, 1, :, 1))
    dimZ = length(view(a, 1, 1, :))
    b = falses(dimY+2, dimX+2, dimZ+2)
    A = falses(dimY+2, dimX+2, dimZ+2)

    for y in 1:dimY
        for x in 1:dimX
            for z in 1:dimZ
                A[y+1, x+1, z+1] = a[y,x,z]
            end
        end
    end
    for y in 1:dimY+2
        dy = (y-1 <= 1 ? 1 : y-1):(y+1 >= dimY+2 ? dimY+2 : y+1)
        for x in 1:dimX+2
            dx = (x-1 <= 1 ? 1 : x-1):(x+1 >= dimX+2 ? dimX+2 : x+1)
            for z in 1:dimZ+2
                dz = (z-1 <= 1 ? 1 : z-1 ):(z+1 >= dimZ+2 ? dimZ+2 : z+1)
                cnt = count(view(A,dy,dx,dz))
                active = A[y,x,z]
                # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                if active == true && cnt-1 in [2,3]
                    b[y, x, z] = true
                else
                    b[y, x, z] = false
                end

                # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                if active == false && cnt == 3
                    b[y, x, z] = true
                end
            end
        end
    end
    b
end

function Cycle4Dim(a)
    dimY = length(view(a, :, 1, 1, 1))
    dimX = length(view(a, 1, :, 1, 1))
    dimZ = length(view(a, 1, 1, :, 1))
    dimW = length(view(a, 1, 1, 1, :))
    b = falses(dimY+2, dimX+2, dimZ+2, dimW+2)
    A = falses(dimY+2, dimX+2, dimZ+2, dimW+2)

    for y in 1:dimY
        for x in 1:dimX
            for z in 1:dimZ
                for w in 1:dimW
                    A[y+1, x+1, z+1, w+1] = a[y,x,z,w]
                end
            end
        end
    end
    for y in 1:dimY+2
        dy = (y-1 <= 1 ? 1 : y-1):(y+1 >= dimY+2 ? dimY+2 : y+1)
        for x in 1:dimX+2
            dx = (x-1 <= 1 ? 1 : x-1):(x+1 >= dimX+2 ? dimX+2 : x+1)
            for z in 1:dimZ+2
                dz = (z-1 <= 1 ? 1 : z-1 ):(z+1 >= dimZ+2 ? dimZ+2 : z+1)
                for w in 1:dimW+2
                    dw = (w-1 <= 1 ? 1 : w-1 ):(w+1 >= dimW+2 ? dimW+2 : w+1)
                    cnt = count(view(A,dy,dx,dz,dw))
                    active = A[y,x,z,w]
                    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. Otherwise, the cube becomes inactive.
                    if active == true && cnt-1 in [2,3]
                        b[y, x, z, w] = true
                    else
                        b[y, x, z, w] = false
                    end

                    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise, the cube remains inactive.
                    if active == false && cnt == 3
                        b[y, x, z, w] = true
                    end
                end
            end
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
