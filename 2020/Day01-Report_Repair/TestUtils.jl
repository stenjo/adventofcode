module TestUtils
using Test
using BenchmarkTools
import Statistics: mean
import Markdown: Table, MD

export btest

function init()
    BenchmarkTools.DEFAULT_PARAMETERS.seconds = 1
    global table = [["Title", "Mem [MiB]", "Allocs", "Time [ms]"]]

    if "AOC_PERF" in keys(ENV)
        println(join(table[1], "\t"))
    end
end

function btest(fun, title)
    @test fun()
    if "AOC_PERF" in keys(ENV)
        r = @benchmark $fun()
        row = string.([title,
                       round(r.memory/(1024^2); digits=2),
                       r.allocs,
                       round(mean(r.times)/1000000; digits=2)])
        push!(table, row)
        println(join(row, "\t"))
    end
end

function output(fname)
    if "AOC_PERF" in keys(ENV)
        open(fname, "w") do f
            write(f, string(MD(Table(table, [:l,:r,:r,:r]))))
        end
    end
end

end #module