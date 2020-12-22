#!/bin/bash

function runjulia {
    INPUT=$1
    SUBSTRING=$(echo $INPUT| cut -d'-' -f 1)
    if [[ "$SUBSTRING" =~ ^Day.* ]]; then
        cp $1* .
        julia $SUBSTRING.jl
        status=$?
        if test $status -ne 0
            exit $status
        fi
        rm *.jl
        rm *.txt
        # /c/Users/sten.johnsen/AppData/Local/Programs/Julia\ 1.5.3/bin/julia.exe Day21.jl
    fi
}

for directory in */; do  
    runjulia $directory
done;
