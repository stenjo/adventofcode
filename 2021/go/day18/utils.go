package day18

import "strconv"

type Chars []rune

func atoi(s rune) int {
	val, _ := strconv.Atoi(string(s))
	return val
}