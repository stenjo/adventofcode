using Base
using Test
using BenchmarkTools
using MD5


function mine(key = "bgvyzdsv" )
    for i in 1:10000000
        hash = bytes2hex(md5(string(key, "", string(i))))
        if SubString(hash, 1,5) ==  "00000"
            return(i)
        end
    end
end

@test mine("abcdef") == 609043
@test mine("pqrstuv") == 1048970
println(mine())

function mineLong(key = "bgvyzdsv" )
    for i in 1:10000000000
        hash = bytes2hex(md5(string(key, "", string(i))))
        if SubString(hash, 1,5) ==  "000000"
            return(i)
        end
    end
end

println(mineLong())
