package day01

import "strconv"

func CountDepth(strList []string) int {

	var numDepths int
	var depths []int
	for i := 0; i < len(strList); i++ {
		var depth, _ = strconv.Atoi(strList[i])
		if len(depths) != 0 && depths[len(depths)-1] < depth {
			numDepths += 1
		}
		depths = append(depths, depth)

	}

	return numDepths

}

func SlidingDepth(strList []string) int {
	var numDepths int
	var depths []int
	var slidingDepths []int

	for i := 0; i < len(strList); i++ {
		var depth, _ = strconv.Atoi(strList[i])
		depths = append(depths, depth)
	}

	for i,j := 3,0; i <= len(depths); i++ {
		var depth = sum(depths[i-3:i])
		if len(slidingDepths) != 0 && slidingDepths[j-1] < depth {
			numDepths ++
		}
		slidingDepths = append(slidingDepths, depth)
		j++
	}

	return numDepths
}


func sum(array []int) int {  
	result := 0  
	for _, v := range array {  
	 result += v  
	}  
	return result  
}  