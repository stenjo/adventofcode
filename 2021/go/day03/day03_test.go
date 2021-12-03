package day03

import (
	"reflect"
	"testing"
)

var bits = []string{"00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"}

func TestBitPopularity(t *testing.T) {
	type args struct {
		str []string
		bit int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"Test1", args{str: []string{"00100", "11110"}, bit: 2}, 2},
		{"Test2", args{str: []string{"00100", "11110"}, bit: 0}, 1},
		{"Test3", args{str: []string{"00100", "11110"}, bit: 4}, 0},
		{"Test4", args{str: bits, bit: 0}, 7},
		{"Test5", args{str: bits, bit: 1}, 5},
		{"Test6", args{str: bits, bit: 2}, 8},
		{"Test7", args{str: bits, bit: 3}, 7},
		{"Test8", args{str: bits, bit: 4}, 5},

		// {"Final", args{str: "bgvyzdsv"}, 254575},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := BitPopularity(tt.args.str, tt.args.bit); got != tt.want {
				t.Errorf("BitPopularity() = %v, want %v", got, tt.want)
			}
		})
	}

}

func TestMostCommonBit(t *testing.T) {
	type args struct {
		str []string
		bit int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"Test1", args{str: bits, bit: 0}, 1},
		{"Test2", args{str: bits, bit: 1}, 0},
		{"Test3", args{str: bits, bit: 2}, 1},
		{"Test4", args{str: bits, bit: 3}, 1},
		{"Test5", args{str: bits, bit: 4}, 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := MostCommonBit(tt.args.str, tt.args.bit); got != tt.want {
				t.Errorf("MostCommonBit() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetGammaRate(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestGamma", args{str: bits}, 22},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetGammaRate(tt.args.str); got != tt.want {
				t.Errorf("GetGammaRate() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetEpsilonRate(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestEpsilon", args{str: bits}, 9},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetEpsilonRate(tt.args.str); got != tt.want {
				t.Errorf("GetEpsilonRate() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetPowerConsumption(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestPower", args{str: bits}, 198},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPowerConsumption(tt.args.str); got != tt.want {
				t.Errorf("GetPowerConsumption() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestFilterList(t *testing.T) {
	type args struct {
		str    []string
		filter string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		// TODO: Add test cases.
		{"TestFilterList", args{str: bits, filter: "1011"}, []string{"10110", "10111"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FilterList(tt.args.str, tt.args.filter); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("FilterList() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetOxygenRate(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestGetOxygenRate", args{str: bits}, 23},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetOxygenRate(tt.args.str); got != tt.want {
				t.Errorf("GetOxygenRate() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCo2Rate(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestGetCo2Rate", args{str: bits}, 10},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCo2Rate(tt.args.str); got != tt.want {
				t.Errorf("GetCo2Rate() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetLifeSupportRating(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"TestGetLifeSupportRate", args{str: bits}, 230},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetLifeSupportRating(tt.args.str); got != tt.want {
				t.Errorf("GetLifeSupportRating() = %v, want %v", got, tt.want)
			}
		})
	}
}
