package day11

import (
	"reflect"
	"testing"
)

var testData = []string{
	"5483143223",
	"2745854711",
	"5264556173",
	"6141336146",
	"6357385478",
	"4167524645",
	"2176841721",
	"6882881134",
	"4846848554",
	"5283751526",
}

func TestGetFlashes(t *testing.T) {
	type args struct {
		str   []string
		steps int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"00000", "00000", "00900", "00000", "00000"}, steps: 1}, 1},
		{"2", args{str: []string{"00000", "00000", "00000", "00090", "00000"}, steps: 1}, 1},
		{"3", args{str: []string{"00000", "00000", "00000", "00000", "00009"}, steps: 1}, 1},
		{"4", args{str: []string{"00000", "00000", "00000", "00000", "00000"}, steps: 1}, 0},
		{"5", args{str: []string{"11111", "19991", "19191", "19991", "11111"}, steps: 1}, 9},
		{"6", args{str: []string{"45654", "51115", "61116", "51115", "45654"}, steps: 1}, 0},
		{"7", args{str: testData, steps: 2}, 35},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetFlashes(tt.args.str, tt.args.steps); got != tt.want {
				t.Errorf("GetFlashes() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestOctoMap_RunStep(t *testing.T) {
	tests := []struct {
		name string
		m    *OctoMap
		want int
	}{
		// TODO: Add test cases.
		// {"1", OctoMap{
		// 	{6,5,9,4,2,5,4,3,3,4},
		// 	{3,8,5,6,9,6,5,8,2,2},
		// 	{6,3,7,5,6,6,7,2,8,4},
		// 	{7,2,5,2,4,4,7,2,5,7},
		// 	{7,4,6,8,4,9,6,5,8,9},
		// 	{5,2,7,8,6,3,5,7,5,6},
		// 	{3,2,8,7,9,5,2,8,3,2},
		// 	{7,9,9,3,9,9,2,2,4,5},
		// 	{5,9,5,7,9,5,9,6,6,5},
		// 	{6,3,9,4,8,6,2,6,3,7},
		// }, 35},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.m.RunStep(); got != tt.want {
				t.Errorf("OctoMap.RunStep() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseOctos(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want OctoMap
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"45654", "51115", "61116", "51115", "45654"}}, OctoMap{
			{{4, false}, {5, false}, {6, false}, {5, false}, {4, false}},
			{{5, false}, {1, false}, {1, false}, {1, false}, {5, false}},
			{{6, false}, {1, false}, {1, false}, {1, false}, {6, false}},
			{{5, false}, {1, false}, {1, false}, {1, false}, {5, false}},
			{{4, false}, {5, false}, {6, false}, {5, false}, {4, false}}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseOctos(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseOctos() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestOctoMap_Increase(t *testing.T) {
	type args struct {
		x int
		y int
	}
	tests := []struct {
		name string
		m    *OctoMap
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.m.Increase(tt.args.x, tt.args.y)
		})
	}
}

func TestOctoMap_IncreaseNeighbours(t *testing.T) {
	type args struct {
		x int
		y int
	}
	tests := []struct {
		name string
		m    *OctoMap
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.m.IncreaseNeighbours(tt.args.x, tt.args.y)
		})
	}
}

func TestSimultanFlash(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"7", args{str: testData}, 195},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := SimultanFlash(tt.args.str); got != tt.want {
				t.Errorf("SimultanFlash() = %v, want %v", got, tt.want)
			}
		})
	}
}
