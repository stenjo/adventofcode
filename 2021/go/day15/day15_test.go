package day15

import (
	"reflect"
	"testing"
)

var testData = []string{
	"1163751742",
	"1381373672",
	"2136511328",
	"3694931569",
	"7463417111",
	"1319128137",
	"1359912421",
	"3125421639",
	"1293138521",
	"2311944581",
}

func TestGetLowestRiskPath(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want uint64
	}{
		{"0", args{str: []string{
			"12345",
			"23456",
			"34567",
			"45678",
			"56789"}}, 44},
		{"1", args{str: []string{
			"123",
			"213",
			"231"}}, 7},
		{"2", args{str: testData}, 40},
		{"3", args{str: []string{
			"19999",
			"19111",
			"11191"}}, 8},
		{"4", args{str: []string{
			"1122334455",
			"1122334455",
			"2233445566",
			"2233445566",
			"3344556677",
			"3344556677",
			}}, 56},
		}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetLowestRiskPath(tt.args.str); got != tt.want {
				t.Errorf("GetLowestRiskPath() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseInput(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name  string
		args  args
		want  Grid
		want1 uint64
		want2 uint64
	}{
		// {"1", args{str: []string{"123", "213", "231"}}, Grid{
		// 	{{{0,0}:1}, {pos:{0,0},2}, {{0,0},3}},
		// 	{{{0,0},2}, {{0,0},1}, {{0,0},3}},
		// 	{{{0,0},2}, {{0,0},3}, {{0,0},1}},
		// 	}, 2, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1, got2 := parseInput(tt.args.str)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseInput() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("parseInput() got1 = %v, want %v", got1, tt.want1)
			}
			if got2 != tt.want2 {
				t.Errorf("parseInput() got2 = %v, want %v", got2, tt.want2)
			}
		})
	}
}


func TestGetLowestRiskPathExtended(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want uint64
	}{
		{"0", args{str: []string{
			"1"}}, 44},
		{"1", args{str: []string{
			"123",
			"213",
			"231"}}, 121},
		{"2", args{str: []string{
			"11",
			"11",
			}}, 90},
		{"3", args{str: testData}, 315},
		{"4", args{str: []string{
			"19999",
			"19111",
			"11191"}}, 158},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetLowestRiskPathExtended(tt.args.str); got != tt.want {
				t.Errorf("GetLowestRiskPathExtended() = %v, want %v", got, tt.want)
			}
		})
	}
}



// func Test_modRem(t *testing.T) {
// 	type args struct {
// 		x int
// 		y int
// 	}
// 	tests := []struct {
// 		name  string
// 		args  args
// 		want  int
// 		want1 int
// 	}{
// 		// TODO: Add test cases.
// 		{"1", args{x: 17, y: 10}, 1, 7},
// 		{"1", args{x: 18, y: 10}, 1, 8},
// 		{"1", args{x: 19, y: 10}, 1, 9},
// 		{"1", args{x: 20, y: 10}, 2, 0},
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			got, got1 := modRem(tt.args.x, tt.args.y)
// 			if got != tt.want {
// 				t.Errorf("modRem() got = %v, want %v", got, tt.want)
// 			}
// 			if got1 != tt.want1 {
// 				t.Errorf("modRem() got1 = %v, want %v", got1, tt.want1)
// 			}
// 		})
// 	}
// }

// func Test_limRisk(t *testing.T) {
// 	type args struct {
// 		v int
// 	}
// 	tests := []struct {
// 		name string
// 		args args
// 		want int
// 	}{
// 		{"1", args{7}, 7},
// 		{"2", args{8}, 8},
// 		{"3", args{9}, 9},
// 		{"4", args{10}, 1},
// 		{"5", args{18}, 9},
// 		{"6", args{19}, 1},
// 		{"7", args{20}, 2},
// 	}
// 	for _, tt := range tests {
// 		t.Run(tt.name, func(t *testing.T) {
// 			if got := limRisk(tt.args.v); got != tt.want {
// 				t.Errorf("limRisk() = %v, want %v", got, tt.want)
// 			}
// 		})
// 	}
// }
