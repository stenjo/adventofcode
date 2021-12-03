package day03

func BitPopularity(str []string, bit int) int {
	var freq int
	for i := 0; i < len(str); i++ {
		if str[i][bit] == '1' {
			freq++
		}
	}
	return freq
}

func MostCommonBit(str []string, bit int) int {

	if BitPopularity(str, bit) > len(str) {
		return 1
	}
	return 0
}