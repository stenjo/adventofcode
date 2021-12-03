package day03

import "testing"

var bits = []string{"00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"}

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
		{"Test1", args{str:[]string{"00100", "11110"}, bit:2}, 2},
		{"Test2", args{str:[]string{"00100", "11110"}, bit:0}, 1},
		{"Test3", args{str:[]string{"00100", "11110"}, bit:4}, 0},
		{"Test4", args{str:bits, bit:0}, 7},
		{"Test5", args{str:bits, bit:1}, 5},
		{"Test6", args{str:bits, bit:2}, 8},
		{"Test7", args{str:bits, bit:3}, 7},
		{"Test8", args{str:bits, bit:4}, 5},

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