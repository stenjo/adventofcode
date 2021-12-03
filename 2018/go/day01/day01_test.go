package day01

import (
	"testing"
)

func TestResultingFrequency(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"1", "-2", "3", "1"}}, 3},
		{"2", args{str: []string{"1", "1", "1"}}, 3},
		{"3", args{str: []string{"1", "1", "-2"}}, 0},
		{"4", args{str: []string{"-1", "-2", "-3"}}, -6},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ResultingFrequency(tt.args.str); got != tt.want {
				t.Errorf("ResultingFrequency() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestFrequencyReachedTwice(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"1", "-1"}}, 0},
		{"2", args{str: []string{"3", "3", "4", "-2", "-4"}}, 10},
		{"3", args{str: []string{"-6", "3", "8", "5", "-6"}}, 5},
		{"4", args{str: []string{"7", "7", "-2", "-7", "-4"}}, 14},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := FrequencyReachedTwice(tt.args.str); got != tt.want {
				t.Errorf("FrequencyReachedTwice() = %v, want %v", got, tt.want)
			}
		})
	}
}
