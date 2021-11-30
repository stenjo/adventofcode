
using Base

function main()
    lines=readlines("day01.txt")
    flr::Int = 0
    line = join(lines)
    for (i,c) in enumerate(line)
        if c == '('
            flr +=1
        elseif c == ')'
            flr -= 1
        end
        if flr == -1
            println(i)
        end

    end
    println(flr)
end

main()
