package day19

import (
	"testing"

	"example.com/aoc2021/tools"
)

func loadtest(file string) []string {
	return tools.GetData(file)
}

func Test_xyz_parse(t *testing.T) {
	p := xyz{}
	type args struct {
		s string
	}
	tests := []struct {
		name string
		p    *xyz
		args args
		want xyz
	}{
		// TODO: Add test cases.
		{"1", &p, args{s: "390,-675,-793"}, xyz{390, -675, -793}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.p.parse(tt.args.s)
			if got := p; got != tt.want {
				t.Errorf("xyz.parse() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCountBeacons(t *testing.T) {
	type args struct {
		s []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{s:loadtest("test2.txt")},79},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CountBeacons(tt.args.s); got != tt.want {
				t.Errorf("CountBeacons() = %v, want %v", got, tt.want)
			}
		})
	}
}
