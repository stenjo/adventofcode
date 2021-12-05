package day03

import (
	"reflect"
	"testing"
)

func TestFindValidTriangles(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{"  5 10 25"}}, 0},
		{"2", args{strList: []string{"10 25   5", "  407  630  900"}}, 1},
		{"3", args{strList: []string{"  25 10 5", "  194   69  754"}}, 0},
		{"3", args{strList: []string{"25 10 5", "   785  516  744", "  407  630  900", "  602  117  311", "  194   69  754"}}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FindValidTriangles(tt.args.strList); got != tt.want {
				t.Errorf("FindValidTriangles() = %v, want %v", got, tt.want)
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

func Test_getIntsFromStrings(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{"1 1 1", "2 2 2"}}, [][]int{{1, 1, 1}, {2, 2, 2}}},
		{"2", args{strList: []string{"10 25   5", "  407  630  900"}}, [][]int{{10, 25, 5}, {407, 630, 900}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getIntsFromStrings(tt.args.strList); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getIntsFromStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestFindValidVerticalTriangles(t *testing.T) {
	type args struct {
		strList []string
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
			if got := FindValidVerticalTriangles(tt.args.strList); got != tt.want {
				t.Errorf("FindValidVerticalTriangles() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_validTriangle(t *testing.T) {
	type args struct {
		v []int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{v:[]int{1, 1, 1}}, true},
		{"1", args{v:[]int{3, 1, 1}}, false},

	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := validTriangle(tt.args.v); got != tt.want {
				t.Errorf("validTriangle() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getTriangles(t *testing.T) {
	type args struct {
		a [][]int
	}
	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{"1", args{a:[][]int{{1, 1, 1}, {2, 2, 2}, {3, 3, 3}}}, [][]int{{1, 2, 3}, {1, 2, 3}, {1, 2, 3}}},
		{"2", args{a:[][]int{{1, 2, 3}, {2, 3, 4}, {3, 4, 5}}}, [][]int{{1, 2, 3}, {2, 3, 4}, {3, 4, 5}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getTriangles(tt.args.a); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("getTriangles() = %v, want %v", got, tt.want)
			}
		})
	}
}
