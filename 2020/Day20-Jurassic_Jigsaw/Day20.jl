# Day 20 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/20
#
using Test
using Match
using BenchmarkTools

function LoadInitial(file="input.txt")
    lines=readlines(file)
    a = []
    y = 0
    tileNo = 0
    tiles = Dict()
    for line in lines
        if startswith(line, "Tile")
            tileNo = parse(Int, split(split(line)[2], ':')[1])
            a = falses(10, 10)
            y = 0
        elseif line == "" && tileNo != 0
            push!(tiles, tileNo=>a)
        else
            y += 1
            for x in 1:length(line)
                a[y,x] = line[x] == '#' ? true : false
           end
        end
    end
    push!(tiles, tileNo=>a)
    tiles
end

function Edges(tile)
    edges = []
    push!(edges, join(map(s->s==true ? '1' : '0', view(tile, :, 1))))
    push!(edges, join(map(s->s==true ? '1' : '0', view(tile, :, 10))))
    push!(edges, join(map(s->s==true ? '1' : '0', view(tile, 1, :))))
    push!(edges, join(map(s->s==true ? '1' : '0', view(tile, 10,:))))
    edges
end

function CommonEdges(tileNo, tiles)
    edges = Edges(tiles[tileNo])
    result = []
    for edge in edges
        for t in tiles
            if t[1] == tileNo
                continue
            elseif edge in Edges(t[2]) || reverse(edge) in Edges(t[2])
                push!(result, edge)
            end
        end
    end
    result
end

monster = [
"                  # ",
"#    ##    ##    ###",
" #  #  #  #  #  #   "]

function LoadMonster(m=monster)
    (dimY,) = size(m)
    a = falses(dimY, length(m[1]))
    for y in 1:dimY, x in 1:length(m[y])
        a[y,x] = m[y][x] == '#' ? true : false
    end
    a
end

function Bordering(t, tiles)
    bordering = Dict()
    for b in t[2]
        for n in tiles
            if b in n[2]
                push!(bordering,n[1]=>'N')
            elseif b in reverse.(n[2])
                push!(bordering,n[1]=>'F')
            end
        end
    end
    bordering
end
function ArrayToDict(list)
    out = Dict()
    for i in list
        push!(out, i)
    end
    out
end

function BuildImage(tiles)
    #   3
    # 1   2
    #   4
    corners = filter(x->length(x[2]) == 2, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    edges   = filter(x->length(x[2]) == 3, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    centres = filter(x->length(x[2]) == 4, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    allImgs = ArrayToDict(map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))

    # refs = zeros(Int, 2+length(edges)÷4, 2+length(edges)÷4)
    refs = Array{Any}(undef, 2+length(edges)÷4, 2+length(edges)÷4)
    img = corners[1]
    refs[1,1] = img[1]
    (dimX, dimY) = size(refs)
    for x in 1:dimX, y in 1:dimY
        if x == 1 && y == 1         # corner upper left
            refs[x,y] = img[1]
            corners = filter(t->t[1] != refs[x,y], corners)
        elseif x == 1 && y == dimY  # corner lower left
            above = refs[x,y-1]
            c = Bordering(above=>allImgs[above], corners)
            refs[x,y] = pop!(c)[1]
            corners = filter(t->t[1] != refs[x,y], corners)
        elseif x == 1               # First column edge
            above = refs[x,y-1]
            c = Bordering(above=>allImgs[above], edges)
            refs[x,y] = pop!(c)[1]
            edges = filter(t->t[1] != refs[x,y], edges)
        elseif x == dimX && y == 1  # corner upper right
            left = refs[x-1,y]
            d = Bordering(left=>allImgs[left], corners)
            refs[x,y] = pop!(d)[1]
            corners = filter(t->t[1] != refs[x,y], corners)
        elseif x == dimX && y == dimY  # corner lower right
            left = refs[x-1,y]
            d = Bordering(left=>allImgs[left], corners)
            refs[x,y] = pop!(d)[1]
            corners = filter(t->t[1] != refs[x,y], corners)
        elseif x == dimX               # Last column edge
            above = refs[x,y-1]
            c = Bordering(above=>allImgs[above], edges)
            refs[x,y] = pop!(c)[1]
            edges = filter(t->t[1] != refs[x,y], edges)
        elseif y == 1               # First row edge
            left = refs[x-1,y]
            d = Bordering(left=>allImgs[left], edges)
            refs[x,y] = pop!(d)[1]
            edges = filter(t->t[1] != refs[x,y], edges)
        elseif y == dimY               # Last row edge
            left = refs[x-1,y]
            d = Bordering(left=>allImgs[left], edges)
            refs[x,y] = pop!(d)[1]
            edges = filter(t->t[1] != refs[x,y], edges)
        else
            above = refs[x,y-1]
            c = Bordering(above=>allImgs[above], centres)
            left = refs[x-1,y]
            d = Bordering(left=>allImgs[left], centres)
            id = collect(intersect(keys(c), keys(d)))[1]
            refs[x,y] = id
            centres = filter(t->t[1] != id, centres)
        end
    end
    refs
end

@testset "Tiles" begin
    tiles = LoadInitial("test.txt")
    @test length(tiles) == 9
    @test length(Edges(tiles[3079])) == 4
    @test length(CommonEdges(3079, tiles)) == 2
    @test length(CommonEdges(1427, tiles)) == 4
    @test length(CommonEdges(1489, tiles)) == 3
    @test count(view(LoadMonster(), :, 8:11)) == 2
    corners = filter(x->length(x[2]) == 2, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    edges   = filter(x->length(x[2]) == 3, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    @test length(Bordering(corners[1], edges)) == 2
    @test BuildImage(tiles) == [3079 2473 1171; 2311 1427 1489; 1951 2729 2971]
    @test count(v->v !== undef, BuildImage(tiles)) == 9
end


# Part 1
function partOne(file="input.txt")
    tiles = LoadInitial(file)
    prod(map(v->v[1], filter(x->x[2] == 2, map(t->(t[1]=>length(CommonEdges(t[1], tiles))), collect(keys(tiles))))))
end

@test partOne("test.txt") == 20899048083289
@test partOne() == 64802175715999

println(string("Part one: ", partOne()))
@time partOne()

# # Part 2
# partTwo(file="input.txt") = sum(map(v->SolveReversePolish(v), readlines(file)))

# @test partTwo("test.txt") == 693891
# @test partTwo() == 388966573054664

# println(string("Part two: ", partTwo())) # Answer too high
# @time partTwo()
