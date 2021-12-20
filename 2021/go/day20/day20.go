package day20

import (
	"fmt"
	"regexp"
	"strings"
)
type Enhancement string

type TrenchMap map[int]string

func GetCountBy2Enhancements(str []string) int {
	enh, trMap := loadData(str)
	var count int
	for i := 0; i < 2; i++ {
		count = trMap.refine(enh)
		// trMap.print()
	}
	return count
}

func GetCountBy50Enhancements(str []string) int {
	enh, trMap := loadData(str)
	var count int
	for i := 0; i < 50; i++ {
		count = trMap.refine(enh)
		// trMap.print()
	}
	return count
}

func loadData(data []string) (Enhancement, TrenchMap) {
	enhancement := Enhancement(data[0])
	trenchMap := make(TrenchMap)
	for i := 2; i < len(data); i++ {
		trenchMap[i-2] = data[i]
	}
	return enhancement, trenchMap
}

func (tm *TrenchMap) refine(e Enhancement) int {

	(*tm).expand()
	original := (*tm)

	for y:=0; y < len(original)-2; y++ {
		for x:=0; x < len(original[y])-2; x++ {
			str := (*tm)[y]
			str = str[:x] + e.getChar((original.getSubMap(x,y)).calcIndex()) + str[x+1:]
			(*tm)[y] = str
		}
	}
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
	subMap := TrenchMap{}
	subMap[0] = m[y][x:x+3]
	subMap[1] = m[y+1][x:x+3]
	subMap[2] = m[y+2][x:x+3]

	return subMap
}

func (m *TrenchMap) expand() {
	newMap := make(TrenchMap)
	var yOffsetTop int
	var xOffsetLeft string
	var xOffsetRight string
	if strings.Contains((*m).colAsStr(0), "#") || strings.Contains((*m).colAsStr(1), "#") {
		xOffsetLeft = ".."
	}
	if strings.Contains((*m).colAsStr(len((*m)[0])-1), "#") || strings.Contains((*m).colAsStr(len((*m)[0])-2), "#") {
		xOffsetRight = ".."
	}
	if strings.Contains((*m)[0], "#") || strings.Contains((*m)[1], "#"){
		yOffsetTop = 2
		newMap[0] = xOffsetLeft + strings.Repeat(".",len((*m)[0])) + xOffsetRight
		newMap[1] = xOffsetLeft + strings.Repeat(".",len((*m)[1])) + xOffsetRight
	}
	for i := 0; i < len(*m); i++ {
		newMap[i+yOffsetTop] = xOffsetLeft + (*m)[i] + xOffsetRight
	}

	if strings.Contains((*m)[len(*m)-1], "#") || strings.Contains((*m)[len(*m)-2], "#"){
		l := len(newMap)
		newMap[l] = xOffsetLeft + strings.Repeat(".",len((*m)[0])) + xOffsetRight
		newMap[l+1] = xOffsetLeft + strings.Repeat(".",len((*m)[1])) + xOffsetRight
	}

	(*m) = newMap
}

func (m TrenchMap) colAsStr(x int) string {
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