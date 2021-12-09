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
	var count int
	sort.Ints(bsn)
	for _,b := range bsn[len(bsn)-3:] {
		count = count * b
	}

	return count
}

func GetBasins(pts []Point, m [][]int) []int {
	
	var bs []int

	return bs
}

func GetBasin() {

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

func isBasin(p Point, pts []Point, m [][]int) bool {

	return true
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