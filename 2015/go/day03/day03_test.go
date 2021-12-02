package day03

import (
	"testing"
)

func TestPresentDelivery(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test1", args{str: ">"}, 2},
		{"test2", args{str: "^>v<"}, 4},
		{"test3", args{str: "^v^v^v^v^v"}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := PresentDelivery(tt.args.str); got != tt.want {
				t.Errorf("PresentDelivery() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRoboSanta(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"test1", args{str: ">v"}, 3},
		{"test2", args{str: "^>v<"}, 3},
		{"test3", args{str: "^v^v^v^v^v"}, 11},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RoboSanta(tt.args.str); got != tt.want {
				t.Errorf("RoboSanta() = %v, want %v", got, tt.want)
			}
		})
	}
}
