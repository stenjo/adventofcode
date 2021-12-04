package day04

import (
	"reflect"
	"testing"
)
var num = Number{v:1}
var nums = [5][5]Number{
	{Number{v:1}, Number{v:1}}, 
	{Number{v:1}, Number{v:1, m:true}},
}
var brd = Board{numbers: nums, score:0}
func TestBoard_Score(t *testing.T) {
	tests := []struct {
		name string
		b    Board
		want int
	}{
		// TODO: Add test cases.
		{"1", Board{numbers:nums}, 3},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.b.Score(); got != tt.want {
				t.Errorf("Board.Score() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBoard_Parse(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		b    *Board
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", &Board{}, args{str: []string{"1 2", "3 4"}}, 10},
		{"2", &Board{}, args{str: []string{"-1 2", "3 4"}}, 8},
		{"3", &Board{}, args{str: []string{"14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20", "22 11 13  6  5", "2  0 12  3  7"}}, 325},
		{"4", &Board{}, args{str: []string{" 3 15  0  2 22", " 9 18 13 17  5", "19  8  7 25 23", "20 11 10 24  4", "14 21 16 12  6"}}, 324},
		{"5", &Board{}, args{str: []string{"22 13 17 11  0", " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19"}}, 300},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.b.Parse(tt.args.str); got != tt.want {
				t.Errorf("Board.Parse() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBoard_Mark(t *testing.T) {
	type args struct {
		v int
	}
	tests := []struct {
		name string
		b    *Board
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.b.Mark(tt.args.v)
		})
	}
}

func TestFinalScore(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		// {"1", args{strList:[]string{"1,2,3"," ","1 1 1","1 1 2","4 3 2"}},0},
		{"1", args{strList: []string{"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", " ", "14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20", "22 11 13  6  5", " 2  0 12  3  7"}}, 4512},
		{"2", args{strList: []string{"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", " ", "22 13 17 11  0", " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19"}}, 2192},
		{"3", args{strList: []string{
			"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", " ",
			"22 13 17 11  0", " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19", " ",
			" 3 15  0  2 22", " 9 18 13 17  5", "19  8  7 25 23", "20 11 10 24  4", "14 21 16 12  6", " ",
			"14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20", "22 11 13  6  5", " 2  0 12  3  7",
		}}, 4512},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FinalScore(tt.args.strList); got != tt.want {
				t.Errorf("FinalScore() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_removeEmptyStrings(t *testing.T) {
	type args struct {
		s []string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := removeEmptyStrings(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("removeEmptyStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestLastWinnerScore(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"3", args{strList: []string{
			"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1", " ",
			"22 13 17 11  0", " 8  2 23  4 24", "21  9 14 16  7", " 6 10  3 18  5", " 1 12 20 15 19", " ",
			" 3 15  0  2 22", " 9 18 13 17  5", "19  8  7 25 23", "20 11 10 24  4", "14 21 16 12  6", " ",
			"14 21 17 24  4", "10 16 15  9 19", "18  8 23 26 20", "22 11 13  6  5", " 2  0 12  3  7",
		}}, 1924},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := LastWinnerScore(tt.args.strList); got != tt.want {
				t.Errorf("LastWinnerScore() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		array []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sum(tt.args.array); got != tt.want {
				t.Errorf("sum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBoard_Won(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		b    *Board
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.b.Won(tt.args.n); got != tt.want {
				t.Errorf("Board.Won() = %v, want %v", got, tt.want)
			}
		})
	}
}
