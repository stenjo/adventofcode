package day06

func GetErrorCorrected(strList []string) string {

	var msg string
	t := transpose(strList)
	for i := 0; i < len(t); i++ {
		c, _ := findPopular(t[i])
		msg = msg + string(c)
	}
	return msg
}

func GetModifiedCorrected(strList []string) string {

	var msg string
	t := transpose(strList)
	for i := 0; i < len(t); i++ {
		c, _ := findLeastPopular(t[i])
		msg = msg + string(c)
	}
	return msg
}

func transpose(s []string) []string {

	t := make([]string, len(s[0]))
	for _, l := range s {
		if len(l) > len(s[0]) {
			panic("Irregular data: " + l)
		}
		for i, v := range l {
			t[i] = t[i] + string(v)
		}
	}
	return t
}

func findPopular(s string) (rune, int) {

	kvmap := make(map[rune]int)
	var max int
	var pop rune
	for _, v := range s {
		kvmap[v] += 1
		if kvmap[v] > max {
			max = kvmap[v]
			pop = v
		}
	}

	return pop, max
}

func findLeastPopular(s string) (rune, int) {

	var pop rune
	kvmap := make(map[rune]int)
	min := len(s)
	for _, v := range s {
		kvmap[v] += 1
	}
	for k, _ := range kvmap {
		if kvmap[k] <= min {
			min = kvmap[k]
			pop = k
		}

	}

	return pop, min
}
