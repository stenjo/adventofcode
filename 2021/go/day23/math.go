package day23

import (
	"math"
)

func MaxInt(n ...int) int {
	if len(n) == 0 {
		return math.MaxInt32
	}

	max := n[0]
	for _, a := range n {
		if a > max {
			max = a
		}
	}
	return max
}

func MinInt(n ...int) int {
	if len(n) == 0 {
		return math.MinInt32
	}

	min := n[0]
	for _, a := range n {
		if a < min {
			min = a
		}
	}
	return min
}

func AbsInt(n int) int {
	if n < 0 {
		return -n
	}
	return n
}