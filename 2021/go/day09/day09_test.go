package day09

import (
	"reflect"
	"testing"
)

func TestGetRiskLevelSum(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{
			"2199943210",
			"3987894921",
			"9856789892",
			"8767896789",
			"9899965678"}}, 15},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetRiskLevelSum(tt.args.str); got != tt.want {
				t.Errorf("GetRiskLevelSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseData(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{"1", args{str: []string{"219", "398"}}, [][]int{{2, 1, 9}, {3, 9, 8}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseData(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseData() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestFindLowPoints(t *testing.T) {
	type args struct {
		m [][]int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"3", args{m: [][]int{
			{2, 1, 9, 9, 9, 4, 3, 2, 1, 0},
			{3, 9, 8, 7, 8, 9, 4, 9, 2, 1},
			{9, 8, 5, 6, 7, 8, 9, 8, 9, 2},
			{8, 7, 6, 7, 8, 9, 6, 7, 8, 9},
			{9, 8, 9, 9, 9, 6, 5, 6, 7, 8},
		}}, []int{1, 0, 5, 5}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindLowPoints(tt.args.m); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FindLowPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isLow(t *testing.T) {
	type args struct {
		x int
		y int
		m [][]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{"1", args{x: 1, y: 0, m: [][]int{{2, 1, 9}, {3, 9, 8}}}, true},
		{"2", args{x: 9, y: 0, m: [][]int{{2, 1, 9, 9, 9, 4, 3, 2, 1, 0}, {3, 9, 8, 7, 8, 9, 4, 9, 2, 1}}}, true},
		{"3", args{x: 2, y: 2, m: [][]int{
			{2, 1, 9, 9, 9, 4, 3, 2, 1, 0},
			{3, 9, 8, 7, 8, 9, 4, 9, 2, 1},
			{9, 8, 5, 6, 7, 8, 9, 8, 9, 2},
			{8, 7, 6, 7, 8, 9, 6, 7, 8, 9},
			{9, 8, 9, 9, 9, 6, 5, 6, 7, 8},
		}}, true},
		{"4", args{x: 3, y: 2, m: [][]int{
			{2, 1, 9, 9, 9, 4, 3, 2, 1, 0},
			{3, 9, 8, 7, 8, 9, 4, 9, 2, 1},
			{9, 8, 5, 6, 7, 8, 9, 8, 9, 2},
			{8, 7, 6, 7, 8, 9, 6, 7, 8, 9},
			{9, 8, 9, 9, 9, 6, 5, 6, 7, 8},
		}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isLow(tt.args.x, tt.args.y, tt.args.m); got != tt.want {
				t.Errorf("isLow() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetBasinProducst(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{
			"2199943210",
			"3987894921",
			"9856789892",
			"8767896789",
			"9899965678"}}, 1134},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetBasinProducst(tt.args.str); got != tt.want {
				t.Errorf("GetBasinProducst() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetBasin(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			GetBasin()
		})
	}
}

func TestGetLowBasinPoints(t *testing.T) {
	type args struct {
		m [][]int
	}
	tests := []struct {
		name string
		args args
		want []Point
	}{
		{"3", args{m: [][]int{
			{2, 1, 9, 9, 9, 4, 3, 2, 1, 0},
			{3, 9, 8, 7, 8, 9, 4, 9, 2, 1},
			{9, 8, 5, 6, 7, 8, 9, 8, 9, 2},
			{8, 7, 6, 7, 8, 9, 6, 7, 8, 9},
			{9, 8, 9, 9, 9, 6, 5, 6, 7, 8},
		}}, []Point{{1, 0, 1}, {9, 0, 0}, {2, 2, 5}, {6, 4, 5}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetLowBasinPoints(tt.args.m); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetLowBasinPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isBasin(t *testing.T) {
	type args struct {
		p   Point
		pts []Point
		m   [][]int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isBasin(tt.args.p, tt.args.pts, tt.args.m); got != tt.want {
				t.Errorf("isBasin() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetBasins(t *testing.T) {
	type args struct {
		pts []Point
		m   [][]int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetBasins(tt.args.pts, tt.args.m); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetBasins() = %v, want %v", got, tt.want)
			}
		})
	}
}
