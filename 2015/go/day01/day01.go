package day01

func FindFloor(floors string) int {
	var f int
	for i := 0; i < len(floors); i++ {
		var c = floors[i : i+1]
		switch c {
		case "(":
			f++
		case ")":
			f--
		}
	}
	return f
}
