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
                a[x,y] = line[x] == '#' ? true : false
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
    GetPieces(edges::Int) = filter(x->length(x[2]) == edges, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    corners = GetPieces(2) # filter(x->length(x[2]) == 2, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    edges   = GetPieces(3) # filter(x->length(x[2]) == 3, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    centres = GetPieces(4) # filter(x->length(x[2]) == 4, map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))
    allImgs = ArrayToDict(map(t->(t[1]=>CommonEdges(t[1], tiles)), collect(keys(tiles))))

    # refs = zeros(Int, 2+length(edges)÷4, 2+length(edges)÷4)
    refs = Array{Any}(undef, 2+length(edges)÷4, 2+length(edges)÷4)
    img = last(corners)
    refs[1,1] = img[1]
    (dimX, dimY) = size(refs)
    for y in 1:dimY, x in 1:dimX
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
    # Rotate cw -> transpose(m)[1:1:end, end:-1:1]
    # Flip y -> transpose(transpose(m)[1:1:end, end:-1:1])
    # Flip x -> transpose(transpose(m)[end:-1:1,1:1:end])
    # Rotate ccw -> transpose(m)[end:-1:1,1:1:end]

end

const LEFT   = 1
const RIGHT  = 2
const TOP    = 3
const BOTTOM = 4
EdgeIsIn(t, tile, side) = Edges(t)[side] in Edges(tile) || Edges(t)[side] in reverse.(Edges(tile)) ? true : false

RotateCW(m)  = transpose(m)[1:1:end, end:-1:1]
RotateCCW(m) = transpose(m)[end:-1:1,1:1:end]
FlipX(m) = transpose(transpose(m)[end:-1:1,1:1:end])
FlipY(m) = transpose(transpose(m)[1:1:end, end:-1:1])

function MatchTiles1(left, right, dir=RIGHT, bottom=nothing)
    # Try straight
    if EdgeIsIn(left, right, dir)
        return left
    elseif EdgeIsIn(RotateCW(left), right, dir)
        return RotateCW(left)
    elseif EdgeIsIn(RotateCW(RotateCW(left)), right, dir)
        return RotateCW(RotateCW(left))
    elseif EdgeIsIn(RotateCCW(left), right, dir)
        return RotateCCW(left)
    elseif EdgeIsIn(FlipX(left), right, dir)
        return FlipX(left)
    elseif EdgeIsIn(RotateCW(FlipX(left)), right, dir)
        return RotateCW(FlipX(left))
    elseif EdgeIsIn(RotateCW(RotateCW(FlipX(left))), right, dir)
        return RotateCW(RotateCW(FlipX(left)))
    elseif EdgeIsIn(RotateCCW(FlipX(left)), right, dir)
        return RotateCCW(FlipX(left))
    else
        println(Edges(left)[dir], " does not match ", Edges(right))
    end
end

function MatchTiles(tile, right, dir=RIGHT, second=nothing, sdir=BOTTOM)
    left = copy(tile)
    for _ in 1:2
        for __ in 1:5
            if EdgeIsIn(left, right, dir) && (second !== nothing ? EdgeIsIn(left, second, sdir) : true)
                return left
            end
            left = RotateCW(left)
        end
        left =FlipX(left)
    end
    println(Edges(left)[dir], " does not match ", Edges(right))
end



function PatchImage(refs, tiles)
    A = []
    (dimX,dimY) = size(refs)
    (dx,dy) = size(tiles[refs[1,1]])
    row = []
    for y in 1:dimY, x in 1:dimX
        if x == 1 && y == 1             # Top left corner
            row =           view(MatchTiles(tiles[refs[x,y]], tiles[refs[x+1,y]], RIGHT, tiles[refs[x,y+1]]), 2:dx-1, 2:dy-1)
        elseif x == dimX && y == 1      # Top Right corner
            row = cat(row,  view(MatchTiles(tiles[refs[x,y]], tiles[refs[x-1,y]], LEFT, tiles[refs[x,y+1]]), 2:dx-1, 2:dy-1), dims=(2,2))
            A = copy(row)
        elseif x == 1                 # Left edge
            row =           view(MatchTiles(tiles[refs[x,y]], tiles[refs[x+1,y]], RIGHT, tiles[refs[x,y-1]], TOP), 2:dx-1, 2:dy-1)
        elseif x == dimX                # Right edge
            row = cat(row, view(MatchTiles(tiles[refs[x,y]], tiles[refs[x-1,y]],   LEFT, tiles[refs[x,y-1]], TOP), 2:dx-1, 2:dy-1), dims=(2,2))
            A = vcat(A,row)
        elseif y == 1
            row = cat(row, view(MatchTiles(tiles[refs[x,y]], tiles[refs[x+1,y]],  RIGHT, tiles[refs[x,y+1]]), 2:dx-1, 2:dy-1), dims=(2,2))
        else
            row = cat(row, view(MatchTiles(tiles[refs[x,y]], tiles[refs[x+1,y]],  RIGHT, tiles[refs[x,y-1]], TOP), 2:dx-1, 2:dy-1), dims=(2,2))
        end
        # println("x:", x, " y:", y, " row:", size(row))
    end
    A
end

function FindMonster(monster, image)
    (dimX, dimY) = size(image)
    for __ in 1:2
        for _ in 1:4
            found=[]
            (mDimX, mDimY) = size(monster)
            # println("M:",size(monster))
            for x in 1:dimX-mDimX, y in 1:dimY-mDimY
                # println(size(view(image, x:x+mDimX-1, y:y+mDimY-1)))
                if collect(view(image, x:x+mDimX-1, y:y+mDimY-1)) .& collect(monster) == collect(monster)
                    push!(found, (x,y))
                end
            end
            if length(found) > 0
                return count(image) - count(monster)*length(found)
            end
            monster = RotateCW(monster)
        end
        monster = FlipX(monster)
    end
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
    @test BuildImage(tiles) == [1951 2311 3079; 2729 1427 2473; 2971 1489 1171]
    @test count(v->v !== undef, BuildImage(tiles)) == 9
    @test Edges(MatchTiles(tiles[1951], tiles[2311], RIGHT, tiles[2729]))[RIGHT]  == "0100111110"
    @test Edges(MatchTiles(tiles[3079], tiles[2311],  LEFT, tiles[2473]))[BOTTOM] == "0010111000"
    @test Edges(MatchTiles(tiles[2473], tiles[1427],  LEFT, tiles[1171]))[BOTTOM] == "0110001111"
    @test Edges(MatchTiles(tiles[1171], tiles[1489], LEFT))[LEFT] == "0100100000"
    @test size(PatchImage(BuildImage(tiles), tiles)) == (24,24)
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
function partTwo(file="input.txt")
    tiles = LoadInitial(file)
    refs = BuildImage(tiles)
    image = PatchImage(refs, tiles)
    FindMonster(LoadMonster(), image)
end

@test partTwo("test.txt") == 273
@test partTwo() == 2146

println(string("Part two: ", partTwo()))
@time partTwo()
