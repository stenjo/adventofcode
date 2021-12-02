package day04

import (
	"testing"
)

func TestGetHashCount(t *testing.T) {
	type args struct {
		key string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"Test1", args{key: "abcdef"}, 609043},
		{"Test2", args{key: "pqrstuv"}, 1048970},
		{"Final", args{key: "bgvyzdsv"}, 254575},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetHashCount(tt.args.key); got != tt.want {
				t.Errorf("GetHashCoung() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		list []byte
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"Test10", args{list: []byte{}}, 609043},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sum(tt.args.list); got != tt.want {
				t.Errorf("sum() = %v, want %v", got, tt.want)
			}
		})
	}
}
