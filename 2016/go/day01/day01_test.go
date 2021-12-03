package day01_test

import (
	"testing"

	"example.com/aoc2016/day01"
	"github.com/stretchr/testify/assert"
)

func TestNextPos(t *testing.T) {
	var p complex64 = complex(0, 0)
	var d complex64 = complex(0, 1)
	var next, nd = day01.NextPos(d, p, "R2")
	assert.Equal(t, real(next), float32(2.0))
	next, _ = day01.NextPos(nd, next, "L3")
	assert.Equal(t, real(next), float32(2.0))
	assert.Equal(t, imag(next), float32(3.0))

}

func TestRunString(t *testing.T) {
	var result, _ = day01.RunString("R2, L3")
	assert.Equal(t, result, complex64(complex(2, 3)))
	result, _ = day01.RunString("R2, R2, R2")
	assert.Equal(t, result, complex64(complex(0, -2)))
	var _, blocks = day01.RunString("R5, L5, R5, R3")
	assert.Equal(t, blocks, 12.0)
}

func TestVisitedTwice(t *testing.T) {
	var input = "R8, R4, R4, R8"

	var _, blocks = day01.VisitedTwice(input)

	assert.Equal(t, 4, blocks)
}
