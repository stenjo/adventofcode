#!/bin/bash

function runjulia {
    INPUT=$1
    SUBSTRING=$(echo $INPUT| cut -d'-' -f 1)
    if [[ "$SUBSTRING" =~ ^Day.* ]]; then
        echo
        echo Running $SUBSTRING 
        cp $1*.txt .
        cp $1*.jl .
        julia --color=yes --check-bounds=yes $SUBSTRING.jl
        # /c/Users/sten.johnsen/AppData/Local/Programs/Julia\ 1.5.3/bin/julia.exe  $SUBSTRING.jl
        status=$?
        if test $status -ne 0; then
            exit $status
        fi
        rm *.jl
        rm *.txt
    fi
}

for directory in */; do  
    runjulia $directory
done;
