package day05

import "strings"

func GetNiceStrings(strList []string) int {
	var nice int

	for _, str := range strList {
		if !containsDisallowed(str) && containsDouble(str) && containsWovels(str) {
			nice += 1
		}
	}

	return nice
}

func containsDisallowed(str string) bool {

	var disallowed = []string{"ab", "cd", "pq", "xy"}
	for _, dis := range disallowed {
		if strings.Contains(str, dis) {
			return true
		}
	}
	return false
}

func containsDouble(str string) bool {

	for i:=1; i<len(str); i++ {
		if str[i] == str[i-1] {
			return true
		}
	}
	return false
}

func containsWovels(str string) bool {
	var count int
	for _, v := range str {
		if strings.ContainsAny(string(v), "aeiou") {
			count++
		}
	}
	return count > 2
}

func hasPairTwice(str string) bool {

	for i:=2; i<len(str)-1; i++ {
		if strings.Contains(str[i:], str[i-2:i]) {
			return true 
		}
	}
	return false
}

func hasRepeatChar(str string) bool {
	
	for i:=2; i<len(str); i++ {
		if str[i-2] == str[i] {
			return true 
		}
	}
	return false
}

func GetRealNiceStrings(strList []string) int {
	var nice int

	for _, str := range strList {
		if hasRepeatChar(str) && hasPairTwice(str) {
			nice += 1
		}
	}

	return nice
}
