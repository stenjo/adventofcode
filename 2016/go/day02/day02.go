package day02

func KeypadDecode(strList []string) int {

	var key = 5
	var code int
	for _, v := range strList {
		for _, k := range v {
			switch k {
			case 'U':
				if key > 3 {
					key -= 3
				}
			case 'L':
				if key%3 != 1 {
					key -= 1
				}
			case 'R':
				if key%3 != 0 {
					key += 1
				}
			case 'D':
				if key < 7 {
					key += 3
				}
			}
		}

		code *= 10
		code += key
	}
	return code
}

func NightmareKeypadDecode(strList []string) string {

	var x, y = 0, 2
	var keypad = []string{
		"  1  ",
		" 234 ",
		"56789",
		" ABC ",
		"  D  ",
	}
	var code string
	for _, v := range strList {
		for _, k := range v {
			switch k {
			case 'U':
				if y > 0 && keypad[y-1][x] != ' ' {
					y -= 1
				}
			case 'L':
				if x > 0 && keypad[y][x-1] != ' ' {
					x -= 1
				}
			case 'R':
				if x < len(keypad[0])-1 && keypad[y][x+1] != ' ' {
					x += 1
				}
			case 'D':
				if y < len(keypad)-1 && keypad[y+1][x] != ' ' {
					y += 1
				}
			}
		}

		code = code + string(keypad[y][x])
	}
	return code
}