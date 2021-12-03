package day02

type CodeKey struct {
	count int
	chr   rune
}

func ExactlyNum(boxIds []string, num int) int {
	var ids int
	var letters []CodeKey
	for _, id := range boxIds {
		for i := 0; i < len(id); i++ {
			letters = addCount(rune(id[i]), letters)
		}

		for _, l := range letters {
			if l.count == num {
				ids++
				break
			}
		}

		letters = []CodeKey{}
	}

	return ids
}

func addCount(r rune, letters []CodeKey) []CodeKey {

	for i, c := range letters {
		if c.chr == r {
			c.count += 1
			letters[i] = c
			return letters
		}
	}
	letters = append(letters, CodeKey{1, r})
	return letters
}

func CheckSum(str []string) int {

	return ExactlyNum(str, 2) * ExactlyNum(str, 3)
}

func isInList(c rune, list []CodeKey) bool {
	for _, id := range list {
		if rune(id.chr) == c {
			return true
		}
	}
	return false
}
func CommonLetters(str []string) string {

	for i, a := range str {
		for j, b := range str {
			if i != j && compare(a, b) == 1 {
				return common(a, b)
			}
		}
	}
	return ""
}

func common(a, b string) string {
	var cmn string
	for i, c := range a {
		if c == rune(b[i]) {
			cmn += string(c)
		}
	}
	return cmn

}

func compare(a, b string) int {
	diff := 0
	for i, c := range a {
		if c != rune(b[i]) {
			diff++
		}
	}
	return diff
}