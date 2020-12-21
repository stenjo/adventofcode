# Day 21 of Advent of Code puzzle:
# https://adventofcode.com/2020/day/21
#
using Test
using Match
using BenchmarkTools

mutable struct Food
    ingredients :: Array{String}
    allergens :: Array{String}
    function Food(line) 
        parts = split(line, "(contains ")
        ingr = split(strip(parts[1]))
        alrg = split(strip(parts[2][1:end-1]), ",")
        new(strip.(ingr), strip.(alrg))
    end
end

function LoadFood(file="input.txt")
    lines=readlines(file)
    a = []
    for l in lines
        f = Food(l)
        push!(a,f)
    end
    a
end

function Allergens(foods)
    alrgns = Dict()
    for f in foods
        for i in f.allergens
            alrgns[strip(i)] = get(alrgns, i, 0) + 1
        end
    end
    alrgns
end

function AllergenMap(foods)
    a = Dict()
    for f in foods
        for n in f.allergens
            if !(n in keys(a))
                a[n] = []
            end
            push!(a[n], f.ingredients)
        end
    end
    a
    b=Dict()
    for (alrgn,ingrs) in a
        ingr = copy(ingrs[1])
        for i in ingrs[2:end]
            intersect!(ingr, i)
        end
        b[alrgn] = ingr
    end
    b
end

function IngredientsMap(foods)
    a = Dict()
    for f in foods
        for n in f.ingredients
            if !(n in keys(a))
                a[n] = []
            end
            push!(a[n], f.allergens)
        end
    end
    a
    b=Dict()
    for (ingr, alrgns) in a
        alrgn = copy(alrgns[1])
        for i in alrgns[2:end]
            union!(alrgn, i)
        end
        b[ingr] = alrgn
        # empty!(alrgn)
    end
    b
end

function Ingredients(foods)
    ingrs = Dict()
    for f in foods
        for i in f.ingredients
            ingrs[i] = get(ingrs, i, 0) + 1
        end
    end
    ingrs
end

function ReduceIngredients(ingredients, allergens)
    while length(filter(v->length(v[2])==1, allergens)) > 0
        for (al,in) in filter(v->length(v[2])==1, allergens)
            ingredients = filter(a->a[1] != in[1], ingredients)
            for (i,alist) in ingredients
                ingredients[i] = filter(a->a != al, alist)
            end
            for (a,ingList) in allergens
                allergens[a] = filter(i->i != in[1], ingList)
            end
        end
    end
    keys(ingredients)
end

function GetDangerList(ingredients, allergens)
    result = Dict{String,String}()
    while length(filter(v->length(v[2]) > 1, allergens)) > 0
        for (al,in) in filter(v->length(v[2])==1, allergens)
            # ingredients = filter(a->a[1] != in[1], ingredients)
            push!(result, al=>in[1])
            for (i,alist) in ingredients
                if i != in[1]
                    ingredients[i] = filter(a->a != al, alist)
                end
            end
            for (a,ingList) in allergens
                allergens[a] = filter(i->i != in[1], ingList)
            end
        end
    end
    for (k,i) in filter(i->length(i[2]) > 0, allergens)
        push!(result, k=>i[1])
    end
    result
end

@testset "Allergens" begin
    @test length(LoadFood("test.txt")) == 4
    @test length(AllergenMap(LoadFood("test.txt"))) == 3
    @test length(IngredientsMap(LoadFood("test.txt"))) == 7
end

# Part 1
function partOne(file="input.txt")
    foods = LoadFood(file)
    ingredients = IngredientsMap(foods)
    allergens = AllergenMap(foods)
    shortlist = ReduceIngredients(ingredients, allergens)
    sum(j->count(i->j in i, map(f->f.ingredients,foods)),shortlist)
end

@test partOne("test.txt") == 5
@test partOne() == 1882

println(string("Part one: ", partOne()))
@time partOne()

# # Part 2
function partTwo(file="input.txt")
    foods = LoadFood(file)
    ingredients = IngredientsMap(foods)
    allergens = AllergenMap(foods)
    shortlist = GetDangerList(ingredients, allergens)
    join(map(a->shortlist[a], sort(collect(keys(shortlist)))),',')
end

@test partTwo("test.txt") == "mxmxvkd,sqjhc,fvjkl"
@test partTwo() == "xgtj,ztdctgq,bdnrnx,cdvjp,jdggtft,mdbq,rmd,lgllb"

println(string("Part two: ", partTwo())) # Answer too high
@time partTwo()
