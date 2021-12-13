package day13

import (
	"reflect"
	"testing"
)

func TestDotsWhenFoldedOnce(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{"6,10", "0,14", "9,10", "0,3", "10,4", "4,11", "6,0", "6,12", "4,1", "0,13", "10,12", "3,4", "3,0", "8,4", "1,10", "2,14", "8,10", "9,0", "", "fold along y=7", "fold along x=5"}}, 17},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := DotsWhenFoldedOnce(tt.args.str); got != tt.want {
				t.Errorf("DotsWhenFoldedOnce() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGrid_Fold(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		grid *Grid
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.grid.Fold(tt.args.str)
		})
	}
}

func TestGrid_CountDots(t *testing.T) {
	tests := []struct {
		name string
		grid *Grid
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.grid.CountDots(); got != tt.want {
				t.Errorf("Grid.CountDots() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestParseInput(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name  string
		args  args
		want  Grid
		want1 []string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := ParseInput(tt.args.str)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ParseInput() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("ParseInput() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestDotsWhenFoldedAll(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{"6,10", "0,14", "9,10", "0,3", "10,4", "4,11", "6,0", "6,12", "4,1", "0,13", "10,12", "3,4", "3,0", "8,4", "1,10", "2,14", "8,10", "9,0", "", "fold along y=7", "fold along x=5"}}, 16},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := DotsWhenFoldedAll(tt.args.str); got != tt.want {
				t.Errorf("DotsWhenFoldedAll() = %v, want %v", got, tt.want)
			}
		})
	}
}
