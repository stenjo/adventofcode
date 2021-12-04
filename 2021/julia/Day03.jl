
using Base
using Test
using BenchmarkTools

function NextPosition(position, c)
    if c == '>'
        return position + 1
    elseif c == '<'
        return position - 1
    elseif c == 'v'
        return position - 1im
    elseif c  == '^'
        return position + 1im
    end
    return position
end

function Visits(instructions = readlines("day03.txt"))
    
    santa::Complex = 0+0im
    # robot::Complex = 0+0im

    houses = Vector{Complex}()
    append!(houses, santa)
    for (i,c) in enumerate(join(instructions))
        # if isodd(i)
        santa = NextPosition(santa, c)
        if (santa in houses) == false
            append!(houses, santa)
        end
        # else
        #     robot = NextPosition(robot, c)
        #     if robot in houses == false
        #         append!(houses, robot)
        #     end
        # end
    end
    return length(houses)
end

@test Visits(">") == 2
@test Visits("^>v<") == 4
@test Visits("^v^v^v^v^v") == 2
println(Visits())

function VisitsWithRobot(instructions = readlines("day03.txt"))
    
    santa::Complex = 0+0im
    robot::Complex = 0+0im

    houses = Vector{Complex}()
    append!(houses, santa)
    # append!(houses, robot)
    for (i,c) in enumerate(join(instructions))
        if isodd(i)
            santa = NextPosition(santa, c)
            if (santa in houses) == false
                append!(houses, santa)
            end
        else
            robot = NextPosition(robot, c)
            if (robot in houses) == false
                append!(houses, robot)
            end
        end
    end
    return length(houses)
end

@test VisitsWithRobot("^>") == 3
@test VisitsWithRobot("^>v<") == 3
@test VisitsWithRobot("^v^v^v^v^v") == 11
println(VisitsWithRobot())
