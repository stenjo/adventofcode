package day08

import (
	"sort"
	"strings"
)

type Note struct {
	signals []string
	digits  []string
}

func parseNotes(strlns []string) []Note {
	var notes = []Note{}

	for _, s := range strlns {
		elmts := strings.Split(s, " | ")
		note := Note{
			sortByLen(sortStrElements(strings.Split(elmts[0], " "))), 
			sortStrElements(strings.Split(elmts[1], " "))}
		notes = append(notes, note)
	}

	return notes
}

func sortByLen(s []string) []string {
	var out []string
	for i := 1; i < 10; i++ {
		for _, v := range s {
			if len(v) == i {
				out = append(out, v)
			}
		}
	}
	return out
}

func GetUniqueSegmentsDigitCount(str []string) int {

	var count int
	notes := parseNotes(str)
	for _, s := range notes {
		for _, d := range s.digits {
			if intInList(len(d), []int{2,3,4,7}) { // 1:2, 7:3, 4:4, 8:7
				count ++
			}
		}
	}
	return count
}

func GetOutputValueSum(str []string) int64 {

	var sum int64
	notes := parseNotes(str)
	for _, note := range notes {
		sum += int64(note.decode())
	}
	return sum
}

func (n Note)decode() int {
	var num int
	var segMap = make(map[string]int)

	n.signals = sortStrElements(n.signals)
	for ;len(n.signals) > 0; {
		// l:=len(n.signals)
		for _,s := range n.signals {
			// s := SortString(su)
			var value int
			switch len(s) {
				case 2: 
					value = 1
				case 3: 
					value = 7
				case 4: 
					value = 4
				case 5: 		// Either 2, 3 or 5
					if hasCommonWith(s, getSegsForVal(1, segMap)) == 2 {
						value = 3
					} else if hasCommonWith(s, getSegsForVal(9, segMap)) == 5 {
						value = 5
					} else if hasCommonWith(s, getSegsForVal(9, segMap)) == 4 {
						value = 2
					} else {
						continue
					}
				case 6: 		// Either 0, 6 or 9
					if hasCommonWith(s, getSegsForVal(1, segMap)) == 1 {
						value = 6
					} else if hasCommonWith(s, getSegsForVal(4, segMap)) == 4 {
						value = 9
					} else if hasCommonWith(s, getSegsForVal(4, segMap)) == 3 {
						value = 0
					} else {
						continue
					}
				case 7: 
					value = 8
				default: continue
			}
			segMap[s] = value
			n.signals = remove(n.signals, s)
		}
	}

	for _, su := range n.digits {
		s := SortString(su)
		v, ok := segMap[s]
		if ok {
			num = num * 10 + v
		}
	}
	return num
}

func remove(s []string, str string) []string {
	for i := 0; i < len(s); i++ {
		if s[i] == str {
			s[i] = s[len(s)-1]
		}
	}
    return s[:len(s)-1]
}

func sortStrElements(str []string) []string {
	var s []string
	for _, v := range str {
		s = append(s, SortString(v))
	}
	return s
}

func hasCommonWith(s1, s2 string) int {
	var count int
	if len(s1) == 0 || len(s2) == 0 {
		return 0
	}
	for _, v := range s1 {
		if strings.Contains(s2, string(v)) {
			count ++
		}
	}
	return count

}

func getSegsForVal(val int, m map[string]int) string {
	for s, v := range m {
		if v == val {
			return s
		}
	}
	return ""
}

func intInList(i int, list []int) bool {

	for _, d := range list {
		if d == i {
			return true
		}
	}
	return false
}

type sortRunes []rune

func (s sortRunes) Less(i, j int) bool {
    return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
}

func (s sortRunes) Len() int {
    return len(s)
}

func SortString(s string) string {
    r := []rune(s)
    sort.Sort(sortRunes(r))
    return string(r)
}
