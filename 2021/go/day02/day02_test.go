package day02_test

import (
	"testing"

	"example.com/aoc2021/day02"
	"github.com/stretchr/testify/assert"
)

func TestMoveSub(t *testing.T) {

	// var data = strings.Split("1 2", " ")
	var hpos int
	var vpos int

	hpos, vpos = day02.MoveSub(hpos, vpos, "forward 5")
	assert.Equal(t, hpos, 5)
	hpos, vpos = day02.MoveSub(hpos, vpos, "down 5")
	assert.Equal(t, vpos, 5)
	hpos, vpos = day02.MoveSub(hpos, vpos, "forward 8")
	assert.Equal(t, hpos, 13)
	hpos, vpos = day02.MoveSub(hpos, vpos, "up 3")
	assert.Equal(t, vpos, 2)
	hpos, vpos = day02.MoveSub(hpos, vpos, "down 8")
	assert.Equal(t, vpos, 10)
	hpos, vpos = day02.MoveSub(hpos, vpos, "forward 2")
	assert.Equal(t, hpos, 15)
	assert.Equal(t, vpos, 10)
	
}

func TestMoveTo(t *testing.T) {
	var data = []string {"forward 5","down 5","forward 8","up 3","down 8","forward 2"}
	var hpos, vpos, product = day02.MoveTo(data)

	assert.Equal(t, hpos, 15)
	assert.Equal(t, vpos, 10)

	assert.Equal(t, product, 15*10)


}

func TestMoveSubAim(t *testing.T) {

	// var data = strings.Split("1 2", " ")
	var hpos int
	var vpos int
	var aim int

	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "forward 5")
	assert.Equal(t, hpos, 5)
	assert.Equal(t, aim, 0)

	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "down 5")
	assert.Equal(t, aim, 5)
	assert.Equal(t, vpos, 0)

	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "forward 8")
	assert.Equal(t, hpos, 13)
	assert.Equal(t, aim, 5)
	assert.Equal(t, vpos, 40)

	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "up 3")
	assert.Equal(t, aim, 2)
	assert.Equal(t, vpos, 40)

	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "down 8")
	assert.Equal(t, aim, 10)
	assert.Equal(t, vpos, 40)
	
	hpos, vpos, aim = day02.MoveSubAim(hpos, vpos, aim, "forward 2")
	assert.Equal(t, 15, hpos)
	assert.Equal(t, 10, aim)
	assert.Equal(t, 60, vpos)
	
}

func TestAimTo(t *testing.T) {
	var data = []string {"forward 5","down 5","forward 8","up 3","down 8","forward 2"}
	var hpos, vpos, product = day02.AimTo(data)

	assert.Equal(t, 15, hpos)
	assert.Equal(t, 60, vpos)

	assert.Equal(t, 15*60, product)
}