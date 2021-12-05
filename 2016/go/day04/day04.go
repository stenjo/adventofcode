package day04

import (
	"sort"
	"strconv"
	"strings"
)

type Ename struct {
	encrypted string
	sectorId  int
	checksum  string
}

func RealRoomSectorIdSums(strList []string) int {

	var enames = []Ename{}

	enames = parseEnames(strList)

	var sumOfIds int
	for _, n := range enames {
		if valid(n) {
			sumOfIds += n.sectorId
		}
	}

	return sumOfIds
}

func NortPoleObjectsId(strList []string) int {

	enames := parseEnames(strList)
	for _, n := range enames {
		encrypted := "northpole-object-storage"
		if ReverseEncrypt(n.encrypted, n.sectorId) == encrypted {
			return n.sectorId
		}
	}
	return 0
}

func ReverseEncrypt(s string, n int) string {
	var ret string
	for _,c := range strings.ToLower(s) {
		if c == ' ' || c == '-' {
			ret = ret + "-"
		}else {
			ret = ret + string(Rotate(c, n, false))
		}
	}
	return ret
}

func Rotate(r rune, n int, left bool) rune{
	alphabet := "abcdefghijklmnopqrstuvwxyz"
	max := len(alphabet)
	pos := strings.Index(alphabet, string(r))
	if left {
		return rune(alphabet[(pos+(n/max+1)*max-n) % max])
	} else {
		return rune(alphabet[(pos+n) % max])
	}
}

func valid(n Ename) bool {
	
	return n.checksum == getCheckSum(n.encrypted)
}

func getCheckSum(s string) string {

	stripped := strings.ReplaceAll(s,"-", "")
	sorted := SortStringByCharacter(stripped)
	plain := singles(sorted)
	count := make([]int, len(plain))
	for _,c := range sorted {
		count[strings.Index(plain, string(c))]++
	}

	var max int
	for _,v := range count {
		if v > max {
			max = v
		}
	}

	var checksum string
	for n := max; n > 0; n-- {
		for i,c := range plain {
			if count[i] == n {
				checksum = checksum + string(c)
			}
			sorted = strings.ReplaceAll(sorted, string(c), "")
		}
	}

	checksum = checksum + sorted

	return checksum[:5]
}

func singles(s string) string {

	ret := s[:1]

	for _,c := range s {
		if rune(ret[len(ret)-1]) != c {
			ret = ret + string(c)
		}

	}
	return ret
}


func StringToRuneSlice(s string) []rune {
	var r []rune
	for _, runeValue := range s {
			r = append(r, runeValue)
	}
	return r
}

func SortStringByCharacter(s string) string {
	r := StringToRuneSlice(s)
	sort.Slice(r, func(i, j int) bool {
			return r[i] < r[j]
	})
	return string(r)
}

func parseEnames(strList []string) []Ename {

	var names = []Ename{}
	for _, n := range strList {
		names = append(names, parseName(n))
	}
	return names
}

func parseName(str string) Ename {
	var name Ename
	// rawRev := reverse(strings.ReplaceAll(str, "]", "["))
	parts := strings.Split(strings.ReplaceAll(str, "]", "["), "[")

	name.checksum = parts[1]
	remainder := strings.Split(strings.Replace(reverse(parts[0]), "-", " ", 1), " ")
	// encrypted := strings.Split(strings.Replace(reverse(parts[0]), "-", " ", 1), " ")[1]
	name.encrypted = reverse(remainder[1])
	sectorId, _ := strconv.Atoi(reverse(remainder[0]))
	name.sectorId = sectorId

	return name
}

func reverse(s string) string {
	var reversed string
	for _, c := range s {
		reversed = string(c) + reversed
	}
	return reversed
}