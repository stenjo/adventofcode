package day02_test

import (
	"testing"

	"example.com/adventofcode/day02"
)

func Test(t *testing.T) {

	if day02.WrappingPaper("2x3x4") != 58 {
		t.Fatal("Failed")
	}
	if day02.WrappingPaper("1x1x10") != 43 {
		t.Fatal("Failed")
	}
	if day02.WrappingPaper("10x1x1") != 43 {
		t.Fatal("Failed")
	}
	if day02.Ribbon("10x1x1") != 14 {
		t.Fatal("Failed")
	}
	if day02.Ribbon("1x1x10") != 14 {
		t.Fatal("Failed")
	}
	if day02.Ribbon("2x3x4") != 34 {
		t.Fatal("Failed")
	}
}