package day05

import (
	"strconv"
	"strings"
)

type Point struct {
	X int
	Y int
}

type Line struct {
	start Point
	end   Point
}

func GetOverlappingPoints(str []string) int {
	var ventmap [1000][1000]int
	lines := removeDiagonals(parseLines(str))
	for _,line := range lines {
		var points = getPoints(line)
		for _, point := range points {
			ventmap[point.X][point.Y]++
		}
	}

	var twoOrHigher int
	for _, line := range ventmap {
		for _, point := range line {
			if point > 1 {
				twoOrHigher++
			}
		}
	}
	return twoOrHigher
}
func GetDagonalOverlappingPoints(str []string) int {
	var ventmap [1000][1000]int
	lines := parseLines(str)
	for _,line := range lines {
		var points = getDiagonalPoints(line)
		for _, point := range points {
			ventmap[point.X][point.Y]++
		}
	}

	var twoOrHigher int
	for _, line := range ventmap {
		for _, point := range line {
			if point > 1 {
				twoOrHigher++
			}
		}
	}
	return twoOrHigher
}

func removeDiagonals(line []Line) []Line{
	var remaining []Line
	for _, l := range line {
		if (l.end.X == l.start.X) || (l.start.Y == l.end.Y) {
			remaining = append(remaining, l)
		}
	}
	return remaining
}

func getPoints(line Line) []Point {
	var points []Point
	
	var xDir int
	var yDir int
	if line.end.X - line.start.X < 0 {
		xDir = -1
	} else {
		xDir = 1
	}
	if line.end.Y - line.start.Y < 0 {
		yDir = -1
	} else {
		yDir = 1
	}
	for x := line.start.X; x != line.end.X + xDir; x+=xDir {
		for y := line.start.Y; y != line.end.Y + yDir; y+=yDir {
			points = append(points, Point{x, y})
		}
	}
	// points = append(points, line.end)
	return points
}

func getDiagonalPoints(line Line) []Point {
	var points []Point
	
	var xDir int
	var yDir int
	if line.end.X - line.start.X < 0 {
		xDir = -1
	} else if line.end.X - line.start.X > 0 {
		xDir = 1
	} else {
		xDir = 0
	}
	if line.end.Y - line.start.Y < 0 {
		yDir = -1
	} else if line.end.Y - line.start.Y > 0 {
		yDir = 1
	} else {
		yDir = 0
	}
	for x,y := line.start.X, line.start.Y;; {
		points = append(points, Point{x, y})
		if x == line.end.X && y == line.end.Y {
			break
		}
		if xDir != 0 {
			x += xDir
		}
		if yDir != 0 {
			y += yDir
		}
	}
	// points = append(points, line.end)
	return points
}

func parseLines(str []string) []Line {
	var lines []Line
	for _, l := range str {
		elmts := strings.Split(l, " ")
		sx, _ := strconv.Atoi(strings.Split(elmts[0], ",")[0])
		sy, _ := strconv.Atoi(strings.Split(elmts[0], ",")[1])
		ex, _ := strconv.Atoi(strings.Split(elmts[2], ",")[0])
		ey, _ := strconv.Atoi(strings.Split(elmts[2], ",")[1])
		lines = append(lines, Line{start:Point{X:sx,Y:sy}, end:Point{X:ex,Y:ey}})
	}
	return lines
}