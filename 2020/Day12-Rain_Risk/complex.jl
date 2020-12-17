using Match

function PartTwo()
    ship = Complex(0,0)
    waypoint = Complex(10,1)
    lines=readlines("input.txt")
    mapComplex = Array{Complex}([Complex(1,0), Complex(0,-1), Complex(-1,0), Complex(0,1)])
    for (dir,val) in map(v->(v[1:1][1], parse(Int,v[2:end])), lines)
        if round(Int,val/90)+1 == 0 || 4 - round(Int,val/90) == 0
            println(dir, " ", val)
            continue
        end
        @match dir begin
            'E' => begin waypoint += Complex(val, 0) end
            'W' => begin waypoint -= Complex(val, 0) end
            'N' => begin waypoint += Complex(0, val) end
            'S' => begin waypoint -= Complex(0, val) end
            'F' => begin ship += val*waypoint end
            'R' => begin waypoint *= mapComplex[1 + round(Int,val/90)] end
            'L' => begin waypoint *= mapComplex[5 - round(Int,val/90)] end
            _  => "nothing"
        end
    end
    abs(ship.re)+abs(ship.im)
end

println(PartTwo())

