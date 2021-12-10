package day10

import (
	"sort"
	"strings"
)

func GetSyntaxErrorPoints(str []string) int {

	return sum(errorPoints(str))

}

func GetCompletionScore(str []string) int {
	return middle(CompletionScores(str))
}

func middle(i []int) int {
	if len(i) == 0 {
		return 0
	}
	sort.Ints(i)
	return i[len(i)/2]
}

func CompletionScores(str []string) []int {
	var scores []int

	for _, s := range str {
		hasError := GetSyntaxError(s)
		if  hasError == '_' {
			compl := GetCompletionString(s)
			scores = append(scores,GetScore(compl))
		}
	}

	return scores
}

func GetScore(compl string) int {
	var score int

	for _,c := range compl {
		score = score * 5 + strings.Index(" )]}>", string(c))
	}
	return score
}

func GetCompletionString(s string) string {

	var compl string
	var delimiters Stack

	for _, delim := range s {
		if strings.Contains("([{<", string(delim)) {
			delimiters.Push(rune(delim))
		} else if strings.Contains(")]}>", string(delim)) {
			d,ok := delimiters.Pop()
			m := matching(d)
			if ok && delim != m {
				return ""
			} else if !ok {
				return ""
			}
		}
	}

	for  {
		r,nonEmpty := delimiters.Pop()
		if !nonEmpty {
			return compl
		}
		compl = compl + string(matching(r))
	}
}

func sum(i []int) int {

	var s int
	for _, n := range i {
		s += n
	}
	return s
}

func errorPoints(str []string) []int {
	var points []int

	for _, line := range str {
		switch GetSyntaxError(line) {

		case ')':
			points = append(points, 3)
		case ']':
			points = append(points, 57)
		case '}':
			points = append(points, 1197)
		case '>':
			points = append(points, 25137)
		}
	}
	return points
}

func GetSyntaxError(line string) rune {

	var delimiters Stack

	for _, delim := range line {
		if strings.Contains("([{<", string(delim)) {
			delimiters.Push(rune(delim))
		} else if strings.Contains(")]}>", string(delim)) {
			d,ok := delimiters.Pop()
			m := matching(d)
			if ok && delim != m {
				return delim
			} else if !ok {
				return '_'
			}
		}
	}
	return '_'
}

func matching(d rune) rune {
	switch d {
	case '{': return '}'
	case '(': return ')'
	case '[': return ']'
	case '<': return '>'
	}
	return '_'
}

type Stack []rune

// IsEmpty: check if stack is empty
func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

// Push a new value onto the stack
func (s *Stack) Push(r rune) {
	*s = append(*s, r) // Simply append the new value to the end of the stack
}

// Remove and return top element of stack. Return false if stack is empty.
func (s *Stack) Pop() (rune, bool) {
	if s.IsEmpty() {
		return '_', false
	} else {
		index := len(*s) - 1   // Get the index of the top most element.
		element := (*s)[index] // Index into the slice and obtain the element.
		*s = (*s)[:index]      // Remove it from the stack by slicing it off.
		return element, true
	}
}
