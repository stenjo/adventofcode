package day01

import (
	"math"
	"strconv"
	"strings"
)

func NextPos(dir complex64, pos complex64, instruction string) (complex64, complex64) {

	var lr = instruction[:1]
	const rotate = complex(0, -1)
	var l, _ = strconv.ParseComplex(instruction[1:], 64)
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
	var list []string = strings.Split(str, ",")
	var pos complex64 = complex(0, 0)
	var dir complex64 = complex(0, 1)
	for i := 0; i < len(list); i++ {
		pos, dir = NextPos(dir, pos, strings.TrimSpace(list[i]))
	}
	return pos, (math.Abs(float64(real(pos))) + math.Abs(float64(imag(pos))))
}

func VisitedTwice(str string) (complex64, int) {
	var list []string = strings.Split(str, ",")
	var pos complex64 = complex(0, 0)
	var dir complex64 = complex(0, 1)
	var locations = []complex64{complex(0, 0)}
	for i := 0 ; i < len(list); i++ {
		pos, dir = NextPos(dir, pos, strings.TrimSpace(list[i]))
		path := createPositions(locations[len(locations)-1], pos)
		hasCrossing,cross  := pathsCrosses(path, locations) 
		if !hasCrossing {
			locations = append(locations, path...)
		// }
		// if !posInList(pos, locations) {
		// 	last := locations[len(locations)-1]
		// 	positions := createPositions(last, pos)
		// 	locations = append(locations, positions...)
		// 	// fmt.Println(locations)
		} else {
			pos = cross
			break
		}
	}
	return pos, int(math.Abs(float64(real(pos))) + math.Abs(float64(imag(pos))))
}

func pathsCrosses(path []complex64, locations []complex64) (bool,complex64) {
	for _,p := range path {
		if posInList(p, locations) {
			return true,p
		}
	}
	return false,(0+0i)
}

func createPositions(last, pos complex64) []complex64 {
	
	diff := pos - last
	var l []complex64
	if real(diff) != 0 {
		dir := real(diff)/float32(math.Abs(float64(real(diff))))
		for i := real(last) + 1*dir; i != (real(pos)+dir); i+=dir  {
			l = append(l, complex(i, imag(pos)))
		}
	}
	if imag(diff) != 0 {
		dir := imag(diff)/float32(math.Abs(float64(imag(diff))))
		for i := imag(last) + 1*dir; i != (imag(pos)+dir); i+=dir  {
			l = append(l, complex(real(pos), i))
		}
	}
	return l
}

func posInList(p complex64, l []complex64) bool {
	for _, b := range l {
		if b == p {
			return true
		}
	}
	return false
}



