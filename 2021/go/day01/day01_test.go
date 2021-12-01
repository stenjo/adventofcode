package day01_test

import (
	"testing"

	"example.com/aoc2021/day01"
	"github.com/stretchr/testify/assert"
)

func TestCountDepth(t *testing.T) {

	depths := []string{"199", "200", "208", "210", "200", "207", "240", "269", "260", "263"}

	assert.Equal(t, day01.CountDepth(depths), 7)
	
}

func TestSlidingDepth(t *testing.T) {

	depths := []string{"199", "200", "208", "210", "200", "207", "240", "269", "260", "263"}

	assert.Equal(t, day01.SlidingDepth(depths), 5, "Should be same")
	
}