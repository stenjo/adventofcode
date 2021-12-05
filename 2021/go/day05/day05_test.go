package day05

import (
	"reflect"
	"testing"
)

func TestGetOverlappingPoints(t *testing.T) {
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
			"0,9 -> 5,9",
			"8,0 -> 0,8",
			"9,4 -> 3,4",
			"2,2 -> 2,1",
			"7,0 -> 7,4",
			"6,4 -> 2,0",
			"0,9 -> 2,9",
			"3,4 -> 1,4",
			"0,0 -> 8,8",
			"5,5 -> 8,2",
		}}, 5},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetOverlappingPoints(tt.args.str); got != tt.want {
				t.Errorf("GetOverlappingPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseLines(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want []Line
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"0,9 -> 5,9"}}, []Line{{start: Point{0, 9}, end: Point{5, 9}}}},
		{"2", args{str: []string{"8,0 -> 0,8"}}, []Line{{start: Point{8, 0}, end: Point{0, 8}}}},
		{"3", args{str: []string{"0,0 -> 8,8"}}, []Line{{start: Point{0, 0}, end: Point{8, 8}}}},
		{"4", args{str: []string{"119,453 -> 282,453"}}, []Line{{start: Point{119, 453}, end: Point{282, 453}}}},
		{"5", args{str: []string{"2,0 -> 0,0"}}, []Line{{start: Point{2, 0}, end: Point{0, 0}}}},
		{"6", args{str: []string{"9,7 -> 7,7"}}, []Line{{start: Point{9, 7}, end: Point{7, 7}}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseLines(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseLines() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getPoints(t *testing.T) {
	type args struct {
		line Line
	}
	tests := []struct {
		name string
		args args
		want []Point
	}{
		// TODO: Add test cases.
		{"1", args{line: Line{start: Point{0, 9}, end: Point{2, 9}}}, []Point{{0, 9}, {1, 9}, {2, 9}}},
		{"2", args{line: Line{start: Point{2, 9}, end: Point{0, 9}}}, []Point{{2, 9}, {1, 9}, {0, 9}}},
		{"3", args{line: Line{start: Point{9, 7}, end: Point{7, 7}}}, []Point{{9, 7}, {8, 7}, {7, 7}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getPoints(tt.args.line); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetDagonalOverlappingPoints(t *testing.T) {
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
			"0,9 -> 5,9",
			"8,0 -> 0,8",
			"9,4 -> 3,4",
			"2,2 -> 2,1",
			"7,0 -> 7,4",
			"6,4 -> 2,0",
			"0,9 -> 2,9",
			"3,4 -> 1,4",
			"0,0 -> 8,8",
			"5,5 -> 8,2",
		}}, 12},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetDagonalOverlappingPoints(tt.args.str); got != tt.want {
				t.Errorf("GetDagonalOverlappingPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_removeDiagonals(t *testing.T) {
	type args struct {
		line []Line
	}
	tests := []struct {
		name string
		args args
		want []Line
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := removeDiagonals(tt.args.line); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("removeDiagonals() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getDiagonalPoints(t *testing.T) {
	type args struct {
		line Line
	}
	tests := []struct {
		name string
		args args
		want []Point
	}{
		{"1", args{line: Line{start: Point{0, 9}, end: Point{2, 9}}}, []Point{{0, 9}, {1, 9}, {2, 9}}},
		{"2", args{line: Line{start: Point{2, 9}, end: Point{0, 9}}}, []Point{{2, 9}, {1, 9}, {0, 9}}},
		{"3", args{line: Line{start: Point{9, 7}, end: Point{7, 7}}}, []Point{{9, 7}, {8, 7}, {7, 7}}},
		{"4", args{line: Line{start: Point{0, 7}, end: Point{2, 9}}}, []Point{{0, 7}, {1, 8}, {2, 9}}},
		{"5", args{line: Line{start: Point{2, 9}, end: Point{0, 7}}}, []Point{{2, 9}, {1, 8}, {0, 7}}},
		{"6", args{line: Line{start: Point{9, 7}, end: Point{7, 5}}}, []Point{{9, 7}, {8, 6}, {7, 5}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getDiagonalPoints(tt.args.line); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getDiagonalPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}
