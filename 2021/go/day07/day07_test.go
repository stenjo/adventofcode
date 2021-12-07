package day07

import (
	"reflect"
	"testing"
)

func TestParseCrabs(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"1", args{s: "16,1,2,2,14"}, []int{16, 1, 2, 2, 14}},
		{"2", args{s: "16,1,2,0,4,2,7,1,2,14"}, []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ParseCrabs(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ParseCrabs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		list []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{list: []int{16, 1, 2, 2, 14}}, 35},
		{"2", args{list: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}}, 49},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sum(tt.args.list); got != tt.want {
				t.Errorf("sum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_average(t *testing.T) {
	type args struct {
		list []int
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
			if got := average(tt.args.list); got != tt.want {
				t.Errorf("average() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCheapes(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"2", args{str: "16,1,2,0,4,2,7,1,2,14"}, 37},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCheapes(tt.args.str); got != tt.want {
				t.Errorf("GetCheapes() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetFuel(t *testing.T) {
	type args struct {
		crab []int
		pos  int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 2}, 37},
		{"2", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 1}, 41},
		{"2", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 3}, 39},
		{"2", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 10}, 71},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetFuel(tt.args.crab, tt.args.pos); got != tt.want {
				t.Errorf("GetFuel() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_abs(t *testing.T) {
	type args struct {
		x int
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
			if got := abs(tt.args.x); got != tt.want {
				t.Errorf("abs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetFuelCrabs(t *testing.T) {
	type args struct {
		crab []int
		pos  int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 5}, 168},
		{"2", args{crab: []int{16, 1, 2, 0, 4, 2, 7, 1, 2, 14}, pos: 2}, 206},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetFuelCrabs(tt.args.crab, tt.args.pos); got != tt.want {
				t.Errorf("GetFuelCrabs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCheapestCrabsway(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: "16,1,2,0,4,2,7,1,2,14"}, 168},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCheapestCrabsway(tt.args.str); got != tt.want {
				t.Errorf("GetCheapestCrabsway() = %v, want %v", got, tt.want)
			}
		})
	}
}
