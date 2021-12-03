package day03

import "strings"

func BitPopularity(str []string, bit int) int {
	var freq int
	for i := 0; i < len(str); i++ {
		if str[i][bit] == '1' {
			freq++
		}
	}
	return freq
}

func MostCommonBit(str []string, bit int) int {
	var onescount = BitPopularity(str, bit)
	if onescount >= len(str)-onescount {
		return 1
	}
	return 0
}

func GetGammaRate(str []string) int {
	var rate int
	for i := 0; i < len(str[0]); i++ {
		rate = rate << 1
		if MostCommonBit(str, i) == 1 {
			rate = rate | 0x01
		}
	}
	return rate
}

func GetEpsilonRate(str []string) int {
	var rate int
	for i := 0; i < len(str[0]); i++ {
		rate = rate << 1
		if MostCommonBit(str, i) == 0 {
			rate = rate | 0x01
		}
	}
	return rate
}

func GetPowerConsumption(str []string) int {
	return GetGammaRate(str) * GetEpsilonRate(str)
}

func FilterList(str []string, filter string) []string {
	var newList = []string{}

	for _, s := range str {
		if strings.HasPrefix(s, filter) {
			newList = append(newList, s)
		}
	}
	return newList
}

func GetOxygenRate(str []string) int {

	var filter string
	var list = str
	var rate int
	for i := 0; i < len(str[0]); i++ {
		rate = rate << 1
		if MostCommonBit(list, i) == 1 {
			filter += "1"
			rate = rate | 0x01
		} else {
			filter += "0"
		}
		list = FilterList(list, filter)
	}
	return rate
}

func GetCo2Rate(str []string) int {

	var filter string
	var list = str
	var rate int
	for i := 0; i < len(str[0]); i++ {
		rate = rate << 1
		if len(list) == 1 {
			if list[0][i] == '1' {
				rate = rate | 0x01
			}
		} else {
			if MostCommonBit(list, i) == 1 {
				filter += "0"
			} else {
				filter += "1"
				rate = rate | 0x01
			}
			list = FilterList(list, filter)
		}
	}
	return rate
}

func GetLifeSupportRating(str []string) int {
	return GetOxygenRate(str) * GetCo2Rate(str)
}
