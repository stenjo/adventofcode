package day09

import (
	"sort"
	"strconv"
	"strings"
)
type Point struct {
	x int
	y int
	v int
}
func GetRiskLevelSum(str []string) int {

	m := parseData(str)
	pts := FindLowPoints(m)
	var count int

	for _,p := range pts {
		count += p + 1
	}

	return count
}

func GetBasinProducst(str [] string) int{
	m := parseData(str)
	pts := GetLowBasinPoints(m)
	bsn := GetBasins(pts, m)
	count := 1
	sort.Ints(bsn)
	if len(bsn) < 3 {
		return count
	}
	for _,b := range bsn[len(bsn)-3:] {
		count = count * b
	}

	return count
}

func GetBasins(pts []Point, m [][]int) []int {
	
	var bs []int
	bsp := GetLowBasinPoints(m)
	for _,lp := range bsp {
		b := GetBasin(lp, m)
		bs = append(bs,b)
	}
	return bs
}

func GetBasin(p Point, m [][]int)  int {

	return len(GetBasinPoints([]Point{p}, m))

}

func GetLowBasinPoints(m [][]int) []Point {

	var points []Point

	for y:=0;y < len(m); y++ {
		for x:=0; x < len(m[y]); x++ {
			if isLow(x,y,m) {
				points = append(points,Point{x,y,m[y][x]})
			}
		}
	}
	return points
}

func GetBasinPoints(points []Point, m [][]int) []Point {
	pts := points
	done := false
	for !done {
		done = true
		for _, p := range pts {
			for _, p2 := range GetAdjacingPoints(p, m) {
				if !inPointsList(p2, pts) {
					pts = append(pts,p2)
					done = false
				}
			}
		}
	}
	return pts
}

func inPointsList(p2 Point, points []Point) bool {

	for _, p := range points {
		if p2 == p {
			return true
		}
	}
	return false
}

func GetAdjacingPoints(p Point, m [][]int) []Point {

	var list []Point

	startY := p.y - 1
	endY := p.y + 1

	startX := p.x - 1
	endX := p.x + 1

	if startY < 0 {
		startY = 0
	}

	if endY > len(m)-1 {
		endY = len(m)-1 
	}

	if startX < 0 {
		startX = 0
	}

	if endX > len(m[p.y])-1 {
		endX = len(m[p.y])-1
	}
	for y := startY; y <= endY; y++ {
		for x := startX; x <= endX; x++ {
			if m[y][x] != 9 && ((x == p.x && y != p.y) || (x != p.x && y == p.y))  {
				list = append(list, Point{x, y, m[y][x]})
			}
		}
	}

	return list
}


func parseData(str []string) [][]int {

	data := make([][]int, len(str))
	for y, l := range str {
		data[y] = make([]int, len(str[y]))
		parts := strings.Split(l, "")
		for x, i := range parts {
			v, _ := strconv.Atoi(i)
			data[y][x] = v		
		}
	}

	return data
}

func FindLowPoints(m [][]int) []int {

	var points []int

	for y:=0;y < len(m); y++ {
		for x:=0; x < len(m[y]); x++ {
			if isLow(x,y,m) {
				points = append(points,m[y][x])
			}
		}
	}
	return points

}

func isLow(x, y int, m [][]int) bool {

	xi := x-1
	if xi < 0 {
		xi = 0
	}
	yi := y-1
	if yi < 0 {
		yi = 0
	}

	xm := x+2
	if xm >= len(m[y]) {
		xm = len(m[y])
	}

	ym := y+2
	if ym >= len(m) {
		ym = len(m)
	}

	p := m[y][x]

	for i := yi; i < ym; i++ {
		for j := xi; j < xm; j++ {
			if m[i][j] < p {
				return false
			}
		}
	}
	return true
}