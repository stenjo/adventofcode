package day01

import "strconv"

func ResultingFrequency(str []string) int {

	var result int
	for _, v := range str {
		f, _ := strconv.Atoi(v)
		result += f
	}
	return int(result)
}

func FrequencyReachedTwice(str []string) int {

	var result int
	var visited = []int{0}
	for i:=0; ; i++{
		var v = str[i%len(str)]
		f, _ := strconv.Atoi(v)
		result += f
		if contains(result, visited) {
			return result
		}
		visited = append(visited,result)
	}
}

func contains(result int, visited []int) bool {
	for _,p := range visited {
		if p == result {
			return true
		}
	}
	return false
}
