package day02

import (
	"sort"
	"strconv"
	"strings"
)

func WrappingPaper(dims string) int {

	var a []string = strings.Split(dims, "x")
	var d = make([]int, 3)
	for i :=0; i < len(a); i++ {
		d[i],_ = strconv.Atoi(a[i])
	}
	sort.Ints(d)
	l,w,h := d[0],d[1],d[2]
	return 2*l*w + 2*w*h + 2*h*l + l*w
}

func TotalPaper(dims []string) int {

	var p int = 0
	for _, dim := range dims {
		p += WrappingPaper(dim)
	}
	return p
}

func Ribbon(dims string) int {
	var a []string = strings.Split(dims, "x")
	var d = make([]int, 3)
	for i :=0; i < len(a); i++ {
		d[i],_ = strconv.Atoi(a[i])
	}
	sort.Ints(d)
	l,w,h := d[0],d[1],d[2]
	return 2*(l+w) + l*w*h
}

func TotalRibbon(dims []string) int {

	var p int = 0
	for _, dim := range dims {
		p += Ribbon(dim)
	}
	return p
}
