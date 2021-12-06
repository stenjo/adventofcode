package day06

import (
	"reflect"
	"testing"
)

func TestRunLanternFishDay(t *testing.T) {
	type args struct {
		fish []int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
		{"1", args{fish: []int{3, 4, 3, 1, 2}}, []int{2, 3, 2, 0, 1}},
		{"2", args{fish: []int{2, 3, 2, 0, 1}}, []int{1, 2, 1, 6, 0, 8}},
		{"3", args{fish: []int{1, 2, 1, 6, 0, 8}}, []int{0, 1, 0, 5, 6, 7, 8}},
		{"4", args{fish: []int{0, 1, 0, 5, 6, 7, 8}}, []int{6, 0, 6, 4, 5, 6, 7, 8, 8}},
		{"5", args{fish: []int{6, 0, 6, 4, 5, 6, 7, 8, 8}}, []int{5, 6, 5, 3, 4, 5, 6, 7, 7, 8}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RunLanternFishDay(tt.args.fish); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("RunLanternFishDay() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestParseFish(t *testing.T) {
	type args struct {
		s string
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
			if got := ParseFish(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ParseFish() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRunLanternFishGens(t *testing.T) {
	type args struct {
		s    string
		gens int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{s: "3,4,3,1,2", gens: 80}, 5934},
		// {"2", args{s: "3,4,3,1,2", gens:256}, 26984457539},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RunLanternFishGens(tt.args.s, tt.args.gens); got != tt.want {
				t.Errorf("RunLanternFishGens() = %v, want %v", got, tt.want)
			}
		})
	}
}


func TestRunLanternFishCycles(t *testing.T) {
	type args struct {
		s    string
		gens int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{s: "3,4,3,1,2", gens: 2}, 6},
		{"2", args{s: "3,4,3,1,2", gens: 3}, 7},
		{"3", args{s: "3,4,3,1,2", gens: 80}, 5934},
		{"4", args{s: "3,4,3,1,2", gens: 256}, 26984457539},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RunLanternFishCycles(tt.args.s, tt.args.gens); got != tt.want {
				t.Errorf("RunLanternFishCycles() = %v, want %v", got, tt.want)
			}
		})
	}
}
