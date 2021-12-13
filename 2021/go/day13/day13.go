package day13

import (
	"fmt"
	"strconv"
	"strings"
)

type Grid [][]int

func DotsWhenFoldedOnce(str []string) int {

	grid, fold := ParseInput(str)

	for _, f := range fold {
		grid.Fold(f)
		break
	}

	return grid.CountDots()
}

func DotsWhenFoldedAll(str []string) int {

	grid, fold := ParseInput(str)

	for _, f := range fold {
		grid.Fold(f)
	}

	grid.PrintDots()
	return grid.CountDots()
}

func (grid *Grid) PrintDots() {
	xSize, ySize := grid.Size()

	for y:=0; y < ySize; y++ {
		var line string
		for x:=0; x < xSize; x++ {
			if (*grid)[y][x] == 1 {
				line = line + "O"
			} else {
				line = line + " "
			}
		}
		fmt.Println(line)
	}
}

func (grid *Grid) Fold(str string) {

	parts := strings.Split(str, " ")
	line := strings.Split(parts[len(parts)-1], "=")

	split,_ := strconv.Atoi(line[1])
	if line[0] == "y" {	// Horizontal split
		for y:=0; y < split; y++ {
			for x:=0; x < len((*grid)[y]); x++ {
				mirrorY := 2 * split - y
				if mirrorY > len(*grid)-1 { continue }
				if (*grid)[mirrorY][x] == 1 {
					(*grid)[y][x] = 1
					(*grid)[mirrorY][x] = 0
				}
			}
		}
	} else if line[0] == "x" { // Vertical split
		for y:=0; y < len(*grid); y++ {
			for x:=0; x < split; x++ {
				mirrorX := 2 * split - x
				if mirrorX > len((*grid)[y])-1 { continue }
				if (*grid)[y][mirrorX] == 1 {
					(*grid)[y][x] = 1
					(*grid)[y][mirrorX] = 0
				}
			}
		}
	}

}

func (grid *Grid) CountDots() int {
	var count int
	for y := 0; y < len(*grid); y++ {
		for x := 0; x < len((*grid)[y]); x++ {
			if (*grid)[y][x] == 1 {
				count++
			}
		}
	}
	return count
}

func (grid *Grid) Size() (int, int) {
	var xSize int
	var ySize int

	for y:=0; y < len(*grid); y++ {
		for x:=0; x < len((*grid)[y]); x++ {
			if (*grid)[y][x] == 1 {
				if xSize < x { xSize = x}
				if ySize < y { ySize = y}
			}
		}
	}

	return xSize+1,ySize+1

}
func ParseInput(str []string) (Grid, []string) {

	var xArr []int
	var yArr []int
	var xSize int
	var ySize int

	var instr []string
	for n, s := range str {
		pos := strings.Split(s, ",")
		if len(pos) < 2 {
			instr = str[n+1:]
			break
		}
		y, _ := strconv.Atoi(pos[1])
		yArr = append(yArr, y)
		if ySize < y {
			ySize = y
		}

		x, _ := strconv.Atoi(pos[0])
		xArr = append(xArr, x)
		if xSize < x { xSize = x}

	}
	grid := make(Grid, ySize+1)
	for y := 0; y < ySize + 1; y++ {
		grid[y] = make([]int, xSize + 1)
	}
	for i:= 0; i < len(yArr); i++ {
		grid[yArr[i]][xArr[i]] = 1
	}

	return grid, instr

}