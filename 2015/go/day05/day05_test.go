package day05

import (
	"testing"
)

var niceOrNaughtyStrings = []string{
	"ugknbfddgicrmopn",
	"aaa",
	"jchzalrnumimnmhp",
	"haegwjzuvuyypxyu",
	"dvszwmarrgswjxmb",
}

func TestGetNiceStrings(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: niceOrNaughtyStrings}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetNiceStrings(tt.args.strList); got != tt.want {
				t.Errorf("GetNiceStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_containsDisallowed(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{str: "ugknbfddgicrmopn"}, false},
		{"2", args{str: "aaa"}, false},
		{"3", args{str: "jchzalrnumimnmhp"}, false},
		{"4", args{str: "haegwjzuvuyypxyu"}, true},
		{"5", args{str: "dvszwmarrgswjxmb"}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := containsDisallowed(tt.args.str); got != tt.want {
				t.Errorf("containsDisallowed() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_containsDouble(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{str: "ugknbfddgicrmopn"}, true},
		{"2", args{str: "aaa"}, true},
		{"3", args{str: "jchzalrnumimnmhp"}, false},
		{"4", args{str: "haegwjzuvuyypxyu"}, true},
		{"5", args{str: "dvszwmarrgswjxmb"}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := containsDouble(tt.args.str); got != tt.want {
				t.Errorf("containsDouble() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_containsWovels(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{str: "ugknbfddgicrmopn"}, true},
		{"2", args{str: "aaa"}, true},
		{"3", args{str: "jchzalrnumimnmhp"}, true},
		{"4", args{str: "haegwjzuvuyypxyu"}, true},
		{"5", args{str: "dvszwmarrgswjxmb"}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := containsWovels(tt.args.str); got != tt.want {
				t.Errorf("containsWovels() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_hasPairTwice(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"0", args{str: "kkkk"}, true},
		{"1", args{str: "qjhvhtzxzqqjkmpb"}, true},
		{"2", args{str: "xxyxx"}, true},
		{"3", args{str: "uurcxstgmygtbstg"}, true},
		{"4", args{str: "aabcdefgaa"}, true},
		{"5", args{str: "ieodomkazucvgmuy"}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasPairTwice(tt.args.str); got != tt.want {
				t.Errorf("hasPairTwice() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_hasRepeatChar(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{str: "qjhvhtzxzqqjkmpb"}, true},
		{"2", args{str: "xxyxx"}, true},
		{"3", args{str: "uurcxstgmygtbstg"}, false},
		{"4", args{str: "oyo"}, true},
		{"5", args{str: "ieodomkazucvgmuy"}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasRepeatChar(tt.args.str); got != tt.want {
				t.Errorf("hasRepeatChar() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetRealNiceStrings(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{"qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"}}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetRealNiceStrings(tt.args.strList); got != tt.want {
				t.Errorf("GetRealNiceStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}
