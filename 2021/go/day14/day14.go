package day14

import "strings"

type Polymer map[string]int

func GetElementDiff(str []string) int {
	template := str[0]
	rules := ParseRules(str[2:])
	elements := ParsePolymer(template)
	for i := 0; i < 10; i++ {
		elements.RunStep(rules)
	}
	return elements.max() - elements.min()
}

func ParsePolymer(template string) Polymer {
	polymer := Polymer{}

	for i := 0; i < len(template)-1; i++ {
		polymer[template[i:i+2]] = 1
	}

	return polymer
}

func GetElementDiff40(str []string) int {
	template := str[0]
	rules := ParseRules(str[2:])
	elements := ParsePolymer(template)
	for i := 0; i < 40; i++ {
		elements.RunStep(rules)
	}
	return elements.max() - elements.min()
}

func (e *Polymer) RunStep(rules map[string]string) {
	result := Polymer{}
	// var last Polymer
	for pair,val := range (*e) {
		result[string(pair[0]) + rules[pair]] += val 
		result[rules[pair] + string(pair[1])] += val
	}
	(*e) = result
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
	var maxVal int
	for _,v := range e {
		if v > maxVal {
			maxVal = v
		}
	}
	return maxVal
}

func (e Polymer) min() int {
	minVal := len(e)
	for _, v := range e {
		if v < minVal {
			minVal = v
		}
	}
	return minVal
}