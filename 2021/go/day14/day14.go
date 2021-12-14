package day14

import "strings"

type Polymer string

func GetElementDiff(str []string) int {
	template := str[0]
	rules := ParseRules(str[2:])
	elements := Polymer(template)
	for i := 0; i < 10; i++ {
		elements.RunStep(rules)
	}
	return elements.max() - elements.min()
}

func GetElementDiff40(str []string) int {
	template := str[0]
	rules := ParseRules(str[2:])
	elements := Polymer(template)
	for i := 0; i < 40; i++ {
		elements.RunStep(rules)
	}
	return elements.max() - elements.min()
}

func (e *Polymer) RunStep(rules map[string]string) {
	var result Polymer
	var last Polymer
	for i:=0; i < len(*e)-1; i++ {
		pair := string((*e)[i:i+2])
		ins := rules[pair]
		result = result + Polymer(pair[0]) + Polymer(ins) // + Polymer(pair[1]) 
		last = Polymer(pair[1]) 
	}
	(*e) = result + last
}

func ParseRules(str []string) map[string]string {

	rules := make(map[string]string, len(str))
	for _, s := range str {
		parts := strings.Split(s, " -> ")
		rules[parts[0]] = parts[1]
	}
	return rules
}

func (e Polymer) max() int {
	scores := make(map[rune]int, len(e))
	var maxVal int
	for _, c := range e {
		scores[c]++
	}
	for _, r := range scores {
		if r > maxVal {
			maxVal = r
		}
	}
	return maxVal
}

func (e Polymer) min() int {
	scores := make(map[rune]int, len(e))
	minVal := len(e)
	for _, c := range e {
		scores[c]++
	}
	for _, r := range scores {
		if r < minVal {
			minVal = r
		}
	}
	return minVal
}