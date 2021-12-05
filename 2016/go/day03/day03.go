package day03

import (
	"sort"
	"strconv"
	"strings"
)

func FindValidTriangles(strList []string) int {
	var validTriangles int
	for _, arr := range strList {
		var edgeStrArr = removeEmptyStrings(strings.Split(arr, " "))
		var edges []int
		for _, edge := range edgeStrArr {
			n,_ := strconv.Atoi(strings.TrimSpace(edge))
			edges = append(edges, n)
		}
		sort.Ints(edges[:])

		if edges[0] + edges[1] > edges[2] {
			validTriangles++
		}
	
	}

	return validTriangles
}

func FindValidVerticalTriangles(strList []string) int {
	var validTriangles int
	a := getIntsFromStrings(strList)
	t := getTriangles(a)
	for _, v := range t {
		if validTriangle(v) {
			validTriangles++
		}
	}
	return validTriangles
}

func validTriangle(v []int) bool {
	panic("unimplemented")
}

func getTriangles(a [][]int) [][]int {
	panic("unimplemented")

}

func getIntsFromStrings(strList []string) [][]int {
	var intArray [][]int
	for _, arr := range strList {
		var edgeStrArr = removeEmptyStrings(strings.Split(arr, " "))
		var edges []int
		for _, edge := range edgeStrArr {
			n,_ := strconv.Atoi(strings.TrimSpace(edge))
			edges = append(edges, n)
		}
		intArray = append(intArray,edges)
	}
	return intArray
}
// removeEmptyStrings - Use this to remove empty string values inside an array. 
// This happens when allocation is bigger and empty
func removeEmptyStrings(s []string) []string {
	var r []string
	for _, str := range s {
		if str != "" {
			r = append(r, str)
		}
	}
	return r
}