package day18

func GetMagnitude(str []string) int {
	return finalSum(str)
}

type Fish struct {
	val   int
	depth int
}

func parseFishPairs(str string) []Fish {
	rawStr := Chars(str)
	fish := []Fish{}

	depth := 0

	for i := 0; i < len(rawStr); i++ {
		switch rawStr[i] {
		case '[':
			depth++
			continue
		case ']':
			depth--
			continue
		case ',':
			continue
		default:
			value := atoi(rawStr[i])
			fish = append(fish, Fish{val: value, depth: depth})
		}
	}
	return fish
}

func finalSnailFish(raw []string) []Fish {

	fishList := parseFishPairs(raw[0])
	raw = raw[1:]

	reduced := true

	for reduced {

		reduced = false
		for i := range fishList {
			if fishList[i].depth == 5 {
				if i > 0 {
					fishList[i-1].val += fishList[1].val
				}
				if i+2 < len(fishList) {
					fishList[i+2].val += fishList[i+1].val
				}
				fishList[i].val = 0
				fishList[i].depth--
				fishList = append(fishList[:i+1], fishList[i+2:]...)
				reduced = true
				break
			}
		}
		if reduced {
			continue
		}
		for i := range fishList {
			if fishList[i].val >= 10 {
				fishList[i].depth++
				fish := Fish{val: fishList[i].val, depth: fishList[i].depth}
				fishList[i].val /= 2
				appendFish := append([]Fish{}, fishList[i+1:]...)
				fishList = append(fishList[:i+1], fish)
				fishList = append(fishList, appendFish...)
				reduced = true
				break
			}
		}
		if reduced {
			continue
		}

		if len(raw) > 0 {
			reduced = true
			fishList = append(fishList, parseFishPairs(raw[0])...)
			raw = raw[1:]

			for i := range fishList {
				fishList[i].depth++
			}
		}
	}
	return fishList
}

func finalSum(raw []string) int {
	finalFish := finalSnailFish(raw)

	for depth := 4; depth >= 0; {
		found := false
		if len(finalFish) == 1 {
			break
		}
		for i := range finalFish {
			if finalFish[i].depth == depth {
				finalFish[i].depth--
				finalFish[i].val = 3*finalFish[i].val + 2*finalFish[i+1].val
				found = true
				newFish := append([]Fish{}, finalFish[:i+1]...)
				if len(finalFish) > i+2 {
					newFish = append(newFish, finalFish[i+2:]...)
				}
				finalFish = newFish
				break
			}
		}
		if !found {
			depth--
		}
	}
	return finalFish[0].val
}
