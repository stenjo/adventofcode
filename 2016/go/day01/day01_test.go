package day01_test

import (
	"fmt"
	"testing"

	"example.com/aoc2016/day01"
)

func TestDay01_test(t *testing.T) {
	var p complex64 = complex(0,0)
	var d complex64 = complex(0,1)
	var next, nd = day01.NextPos(d, p, "R2")
	if real(next) != 2 {
		t.Fatal("Wrong turn")
	}
	next, nd = day01.NextPos(nd, next, "L3")
	if real(next) != 2 || imag(next) != 3 {
		t.Fatal("Wrong turn")
	}
	fmt.Println(nd)

}

func TestDay01_test2(t *testing.T) {
	var result,_ = day01.RunString("R2, L3")
	if result != complex(2,3) {
		t.Fatal("Ended up in wrong place")
	}
	result,_ = day01.RunString("R2, R2, R2")
	if result != complex(0,-2) {
		t.Fatal("Ended up in wrong place")
	}
	var _,blocks = day01.RunString("R5, L5, R5, R3")
	if blocks != 12 {
		t.Fatal("Ended up in wrong place")
	}
}