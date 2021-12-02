package day02

import (
	"strconv"
	"strings"
)

func splitinst(str string) (int, string) {

	var s = strings.Split(str, " ")
	var n,_ = strconv.Atoi(s[1]) 
	return n, s[0]

}


func MoveSub(h int, v int, str string) (int, int) {

	var len, dir = splitinst(str)
	switch dir {
	case "forward":
		h += len
	case "down":
		v += len
	case "up":
		v -= len
	}

	return h, v
}

func MoveTo(strList []string) (int, int, int) {
	var hpos int
	var vpos int

	for i := 0; i < len(strList); i++ {
		hpos, vpos = MoveSub(hpos, vpos, strList[i])
	}
	return hpos, vpos, hpos*vpos
}

func MoveSubAim(h int, v int, a int, str string) (int, int, int) {

	var len, dir = splitinst(str)
	switch dir {
	case "forward":
		h += len
		v += a*len
	case "down":
		// v += len
		a += len
	case "up":
		a -= len
	}

	return h, v, a
}

func AimTo(strList []string) (int, int, int) {
	var hpos int
	var vpos int
	var aim int

	for i := 0; i < len(strList); i++ {
		hpos, vpos, aim = MoveSubAim(hpos, vpos, aim, strList[i])
	}
	return hpos, vpos, hpos*vpos
}