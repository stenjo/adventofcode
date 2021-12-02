package day03

type position struct {
	x int // x position
	y int // y position
}

func PresentDelivery(str string) int {

	var pos position = position{0, 0}
	var houses = []position{pos}
	for _, d := range str {
		switch d {
		case '>':
			pos.x += 1
		case '<':
			pos.x -= 1
		case '^':
			pos.y += 1
		case 'v':
			pos.y -= 1
		}

		if houseInList(pos, houses) == false {
			houses = append(houses, pos)
		}
	}
	return len(houses)
}

func houseInList(h position, list []position) bool {
	for _, p := range list {
		if p == h {
			return true
		}
	}
	return false
}

func RoboSanta(str string) int {

	var santa position = position{0, 0}
	var robo position = position{0, 0}
	var houses = []position{pos}
	for i, d := range str {
		if i == 0 {
			switch d {
			case '>':
				santa.x += 1
			case '<':
				santa.x -= 1
			case '^':
				santa.y += 1
			case 'v':
				santa.y -= 1
			}
		}

		if houseInList(pos, houses) == false {
			houses = append(houses, pos)
		}
	}
	return len(houses)
}
