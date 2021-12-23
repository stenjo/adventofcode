package day20

import (
	"fmt"
	"regexp"
	"strings"
)
type Enhancement string

type TrenchMap []string

// Still does not work on real data - only the test data...
func GetCountBy2Enhancements(str []string) int {
	return getCountByXEnhancements(str, 2)
}

func GetCountBy50Enhancements(str []string) int {
	return getCountByXEnhancements(str, 50)
}

func getCountByXEnhancements(str []string, x int) int {
	enh, trMap := loadData(str)
	var count int
	for i := 0; i < x; i++ {
		count = trMap.refine(enh)
	}
	return count
}

func loadData(data []string) (Enhancement, TrenchMap) {
	enhancement := Enhancement(data[0])
	trenchMap := make(TrenchMap,len(data)-2)
	for i := 2; i < len(data); i++ {
		trenchMap[i-2] = data[i]
	}
	return enhancement, trenchMap
}

func (tm *TrenchMap) refine(e Enhancement) int {

	(*tm) = tm.expand()
	new := make(TrenchMap, len(*tm))
	width := len((*tm)[0])
	height := len(*tm)
	new[0] = strings.Repeat(".", width)
	for y:=1; y < height-1; y++ {
		new[y] = strings.Repeat(".", width)
		for x:=1; x < len(*tm)-1; x++ {
			sm := (*tm).getSubMap(x-1,y-1)
			i := sm.calcIndex()
			str := new[y]
			str = str[:x] + e.getChar(i) + str[x+1:]
			new[y] = str
			// if i > 0 {
			// 	fmt.Println(fmt.Sprint("x:", x, " y:", y, " index:", i))
			// 	sm.print()
			// }
		}
	}
	new[height-1] = strings.Repeat(".", width)
	(*tm) = new
	return tm.count()
}

func (tm TrenchMap) count() int {
	var cnt int
	hashes := regexp.MustCompile("#")
	for _,v := range tm {
		matches := hashes.FindAllStringIndex(v, -1)
		cnt += len(matches)
	}
	return cnt
}

func (pixels TrenchMap)calcIndex() int {

	var index int
	bitstring := pixels[0] + pixels[1] + pixels[2]
	bitstring = strings.Replace(bitstring,".","0",-1)
	bitstring = strings.Replace(bitstring, "#", "1", -1)
	fmt.Sscanf(bitstring, "%b", &index)
	return index
}

func (e Enhancement) getChar(index int) string {
	if index >= len(e) {
		panic("Index out of enhancement range")
		// return "."
	}
	if index < 0 {
		panic("Negative index")
	}
	// if rune(e[index]) == '.' {
	// 	return "+"
	// }
	return string(e[index])
}

func (m TrenchMap) getSubMap(x,y int) TrenchMap {
	subMap := make(TrenchMap,3)
	subMap[0] = m[y][x:x+3]
	subMap[1] = m[y+1][x:x+3]
	subMap[2] = m[y+2][x:x+3]

	return subMap
}

func (m TrenchMap) expand() TrenchMap {
	var yOffsetTop int
	var xOffsetLeft string
	var xOffsetRight string
	height := len(m)
	width := len(m[0])
	newMap := make(TrenchMap, height)
	if strings.Contains(m.col(0), "#") || strings.Contains(m.col(1), "#") {
		xOffsetLeft = ".."
	}
	if strings.Contains(m.col(width-1), "#") || strings.Contains(m.col(width-2), "#") {
		xOffsetRight = ".."
	}
	if strings.Contains(m[0], "#") || strings.Contains(m[1], "#"){
		yOffsetTop = 2
		newMap = append(newMap,[]string{"",""}...)
		newMap[0] = xOffsetLeft + strings.Repeat(".",width) + xOffsetRight
		newMap[1] = xOffsetLeft + strings.Repeat(".",width) + xOffsetRight
	}
	for i := 0; i < height; i++ {
		newMap[i+yOffsetTop] = xOffsetLeft + m[i] + xOffsetRight
	}

	if strings.Contains(m[height-1], "#") || strings.Contains(m[height-2], "#"){
		l := height + yOffsetTop
		newMap = append(newMap,[]string{"",""}...)
		newMap[l] = xOffsetLeft + strings.Repeat(".",width) + xOffsetRight
		newMap[l+1] = xOffsetLeft + strings.Repeat(".",width) + xOffsetRight
	}

	return newMap
}

func (m TrenchMap) col(x int) string {
	var str string
	if x < 0 || x >= len(m) {
		panic("Column out of range")
		// return strings.Repeat(".", len(m))
	}
	for i := 0; i < len(m); i++ {
		str = str + string(m[i][x])
	}
	return str
}

func (m TrenchMap)print() {
	for _,s := range m {
		fmt.Println(s)
	}
	fmt.Println("")
}