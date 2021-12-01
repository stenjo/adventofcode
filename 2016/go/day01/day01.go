package day01

import (
	"math"
	"strconv"
	"strings"
)

func NextPos(dir complex64, pos complex64, instruction string) (complex64, complex64) {

	var lr = instruction[:1]
	const rotate = complex(0, -1)
	var l,_ = strconv.ParseComplex(instruction[1:], 64)
	if lr == "R" {
		dir = dir * rotate
		// pos += dir * complex64(l) + pos
	} else if lr == "L" {
		dir = dir * rotate * rotate * rotate
	}

	pos += dir * complex64(l)

	return pos, dir
}

func RunString(str string) (complex64, float64) {
	var list []string = strings.Split(str,",")
	var pos complex64 = complex(0,0)
	var dir complex64 = complex(0,1)
	for i := 0; i < len(list); i++ {
		pos, dir = NextPos(dir, pos, strings.TrimSpace(list[i]))
	}
	return pos, (math.Abs(float64(real(pos))) + math.Abs(float64(imag(pos))))
}