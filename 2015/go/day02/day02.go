package day02

import (
	"sort"
	"strconv"
	"strings"
)

func WrappingPaper(dims string) int {

	var a []string = strings.Split(dims, "x")
	var d []string = sort.StringSlice(a)
	l,_ := strconv.Atoi(d[0])
	w,_ := strconv.Atoi(d[1])
	h,_ := strconv.Atoi(d[2])
	return 2*l*w + 2*w*h + 2*h*l + l*w
}

func TotalPaper(dims []string) int {

	var p int = 0
	for _, dim := range dims {
		p += WrappingPaper(dim)
	}
	return p
}