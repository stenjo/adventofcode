package day02

import (
	"testing"
)

func TestKeypadDecode(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{"ULL"}}, 1},
		{"2", args{strList: []string{"ULL", "RRDDD", "LURDL", "UUUUD"}}, 1985},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := KeypadDecode(tt.args.strList); got != tt.want {
				t.Errorf("KeypadDecode() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNightmareKeypadDecode(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{"ULL"}}, "5"},
		{"2", args{strList: []string{"ULL", "RRDDD"}}, "5D"},
		{"3", args{strList: []string{"ULL", "RRDDD", "LURDL"}}, "5DB"},
		{"4", args{strList: []string{"ULL", "RRDDD", "LURDL", "UUUUD"}}, "5DB3"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := NightmareKeypadDecode(tt.args.strList); got != tt.want {
				t.Errorf("NightmareKeypadDecode() = %v, want %v", got, tt.want)
			}
		})
	}
}
