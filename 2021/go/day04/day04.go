package day04

import (
	"strconv"
	"strings"
)

type Number struct {
	value  int  //
	marked bool //
}

type Board struct {
	numbers [5][5]Number
	score     int //
	winningNumber int
	totalScore int
}

func (b Board) Score() int {
	var score int
	for _, row := range b.numbers {
		for _, num := range row {
			if !num.marked {
				score += num.value
			}
		}
	}
	return score
}

func (b *Board) Won(n int) bool {

	if b.totalScore != 0 {
		return false
	}
	var rowWin = []int{1,1,1,1,1}
	for _, row := range b.numbers {
		lineWin := true
		for x,num := range row {
			if !num.marked {
				lineWin = false
				rowWin[x] = 0
			}
		}
		if lineWin {
			b.score = b.Score()
			b.winningNumber = n
			b.totalScore = b.score*n
			return true
		}
	}
	if sum(rowWin) > 0 {
		b.score = b.Score()
		b.winningNumber = n
		b.totalScore = b.score*n
		return true
	}
	return false
}

func (b *Board) Parse(str []string) int{
	for y,line := range str {
		row := removeEmptyStrings(strings.Split(line, " "))
		for x,num := range row {
			n,_ := strconv.Atoi(num)
			b.numbers[y][x] = Number{n, false}
		}
	}
	return b.Score()
}

func (b *Board) Mark(v int) {
	for y,row := range b.numbers {
		for x,num := range row {
			if num.value == v {
				num.marked = true
				b.numbers[y][x] = num
			}
		}
	}
}

func FinalScore(strList []string) int {
	var drawStrings = removeEmptyStrings(strings.Split(strList[0], ","))
	var draws []int
	var boards []Board

	for _,str := range drawStrings {
		v,_ := strconv.Atoi(str)
		draws = append(draws,v)
	}
	strList = append(strList, "")
	var batch []string
	for i:=1; i < len(strList); i++ {
		line := strings.TrimSpace(strList[i])
		if (len(line) == 0 && len(batch) != 0) || i == len(strList) - 1{
			var b Board
			b.Parse(batch)
			boards = append(boards, b)
		}
		if len(line) == 0 {
			batch = []string{}
		} else {
			batch = append(batch, line)
		}
	}
	for _,draw := range draws {
		for i, b := range boards {
			b.Mark(draw)
			boards[i] = b
			if b.Won(draw) {
				return b.Score()*draw
			}
		}
	}
	return 0
}

func LastWinnerScore(strList []string) int {
	var drawStrings = removeEmptyStrings(strings.Split(strList[0], ","))
	var draws []int
	var boards []Board

	for _,str := range drawStrings {
		v,_ := strconv.Atoi(str)
		draws = append(draws,v)
	}
	strList = append(strList, "")
	var batch []string
	for i:=1; i < len(strList); i++ {
		line := strings.TrimSpace(strList[i])
		if (len(line) == 0 && len(batch) != 0) || i == len(strList) - 1{
			var b Board
			b.Parse(batch)
			boards = append(boards, b)
		}
		if len(line) == 0 {
			batch = []string{}
		} else {
			batch = append(batch, line)
		}
	}
	var lastwin int
	for _,draw := range draws {
		for i, b := range boards {
			b.Mark(draw)
			if b.Won(draw) {
				lastwin = i
			}
			boards[i] = b
		}
	}
	return boards[lastwin].totalScore
}
func removeEmptyStrings(s []string) []string {
	var r []string
	for _, str := range s {
		if str != "" {
			r = append(r, str)
		}
	}
	return r
}

func sum(array []int) int {  
	result := 0  
	for _, v := range array {  
		result += v  
	}  
	return result  
}  