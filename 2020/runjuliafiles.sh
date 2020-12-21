#!/bin/bash
# /c/Users/sten.johnsen/AppData/Local/Programs/Julia\ 1.5.3/bin/julia.exe Day21.jl
input=*/

function runjulia {
    INPUT=$1
    SUBSTRING=$(echo $INPUT| cut -d'-' -f 1)
    if [[ "$SUBSTRING" =~ ^Day.* ]]; then
        cp $1* .
        /c/Users/sten.johnsen/AppData/Local/Programs/Julia\ 1.5.3/bin/julia.exe $SUBSTRING.jl
    fi
#    for f in $1/*.jl; do FILENAME=${f%%.*};  echo ${FILENAME};  done;
}

for directory in */; do  
    runjulia $directory
done;
