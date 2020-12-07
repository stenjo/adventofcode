# Day 7 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/7
#

using DelimitedFiles
using Test

# Test information from the puzzle
testlines = readlines("test.txt")

# Actual personallized data
inputdata = readlines("input.txt")

function GetInput(file="input.txt")
    strip.(s->(s in ['.']),readlines(file))
end

@test length(GetInput("test.txt")) == 9
# println(GetInput())

mutable struct BagNode
    colour :: String
    children :: Vector{Tuple{Int, BagNode}}
    function BagNode(str)
        m=match(r"^(?<attrib>\w+) (?<colour>\w+) bag", strip(str))
        new(join([m["attrib"],m["colour"]], ' '), [])
    end
end

@test BagNode(readlines("test.txt")[4]).colour == "muted yellow"

function GetBagNodesFromString(str)
    # muted yellow bags contain 2 shiny gold bags, 9 faded blue bags
    bags=[]
    push!(bags, (0, BagNode(strip(split(str,"contain")[1]))))
    contains = strip(split(str,"contain")[2])
    if split(contains)[1] == "no" return bags end
    for b in strip.(split(contains, ','))
        count = parse(Int, split(b)[1])
        push!(bags, (count, BagNode(join(split(b)[2:end], ' '))))
    end
    bags
end
@testset "GetBagNodesFromString" begin
    @test length(GetBagNodesFromString(readlines("test.txt")[1])) == 3
    @test length(GetBagNodesFromString(readlines("test.txt")[3])) == 2
    @test length(GetBagNodesFromString(readlines("test.txt")[8])) == 1
    @test length(GetBagNodesFromString(readlines("test.txt")[9])) == 1
end

function CreateBagNodeTree(file = "input.txt")
    tree = BagNode("top node bag")
    for spec in readlines(file)
        bags = GetBagNodesFromString(spec)
        bag = bags[1][2]
        push!(tree.children, (1,bag))
        for (n, b) in bags[2:end]
            push!(bag.children,(n,b))
        end
    end

    for (c,bag) in tree.children
        for (n, child) in bag.children
            t = filter(c->c[2].colour == child.colour, tree.children)
            child.children = pop!(t)[2].children
        end
    end

    tree
end

function FindBagNode(colour, bag)
    for (n,b) in bag.children
        if b.colour == colour
            return colour
        elseif FindBagNode(colour, b) != ""
            return join([b.colour,FindBagNode(colour, b)], " -> ")
        end
    end
    return ""
end

function CountBagsInBagNode(bag)
    if length(bag.children) > 0
        sum = 0
        for (n,b) in bag.children
            sum += n + n * CountBagsInBagNode(b)
        end
        return sum
    else
        return 0
    end
end

function CountBags(colour, file = "input.txt")
    tree = CreateBagNodeTree(file)
    t = filter(c->c[2].colour == colour, tree.children)
    bag = pop!(t)[2]
    CountBagsInBagNode(bag)
end
@testset "CountBags" begin
    @test CountBags("shiny gold", "test.txt") == 32
    @test CountBags("shiny gold", "test2.txt") == 126
end

function GetTopNodeBags(colour, file="input.txt")
    tree = CreateBagNodeTree(file)
    paths = []
    for (n,topNode) in tree.children
        if topNode.colour != colour
            p = FindBagNode(colour, topNode)
            if p != ""
                p = join([topNode.colour, p], " : ")
                push!(paths, p)
            end
        end
    end
    paths
end


# println.(GetTopNodeBags("dark violet","test2.txt"))

@testset "GetTopNodeBags" begin
    @test length(GetTopNodeBags("shiny gold", "test.txt")) == 4
    @test length(GetTopNodeBags("vibrant plum", "test.txt")) == 5
    @test length(GetTopNodeBags("faded blue", "test.txt")) == 7
    @test length(GetTopNodeBags("dotted black", "test.txt")) == 7
end

# println.(GetTopNodeBags("vibrant plum", "test.txt"))
println(sort(GetTopNodeBags("shiny gold"), by=t->length(t), rev=true)[1])
# println.(GetTopNodeBags("dotted black", "test.txt"))
# println.(GetTopNodeBags("faded blue", "test.txt"))

# Part 1
partOne(colour, file="input.txt") = length(GetTopNodeBags(colour, file))

@test partOne("shiny gold","test.txt") == 4
@test partOne("shiny gold") == 287
println(string("Part one: ", partOne("shiny gold")))

# Part 2
partTwo(colour, file="input.txt") = CountBags(colour, file)

@test partTwo("shiny gold") == 48160
println(string("Part two: ", partTwo("shiny gold")))
# println(sum(length.(map(g->join(intersect(g...)), map(split, split(read("input.txt", String), "\r\n\r\n")) ))))
