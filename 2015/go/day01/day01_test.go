package day01_test

import (
	"testing"

	"example.com/adventofcode/day01"
)

func TestDay01(t *testing.T) {
	if day01.FindFloor("()()") != 0 {
		t.Fatal("Failed")
	}

	if day01.FindFloor("(())") != 0 {
		t.Fatal("Failed")
	}

	if day01.FindFloor("(((") != 3 {
		t.Fatal("Failed")
	}
	if day01.FindFloor("(()(()(") != 3 {
		t.Fatal("Failed")
	}
	if day01.FindFloor("))(((((") != 3 {
		t.Fatal("Failed")
	}

	if day01.FindFloor("())") != -1 {
		t.Fatal("Failed")
	}
	if day01.FindFloor("))(") != -1 {
		t.Fatal("Failed")
	}

	if day01.FindFloor(")))") != -3 {
		t.Fatal("Failed")
	}
	if day01.FindFloor(")())())") != -3 {
		t.Fatal("Failed")
	}
}

