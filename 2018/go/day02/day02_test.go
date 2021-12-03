package day02

import (
	"reflect"
	"testing"
)

var boxIds = []string{"abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"}
var boxId2 = []string{"abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"}

func TestCommonLetters(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{str: boxId2}, "fgij"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CommonLetters(tt.args.str); got != tt.want {
				t.Errorf("CommonLetters() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_addCount(t *testing.T) {
	type args struct {
		r       rune
		letters []CodeKey
	}
	tests := []struct {
		name string
		args args
		want []CodeKey
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := addCount(tt.args.r, tt.args.letters); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("addCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isInList(t *testing.T) {
	type args struct {
		c    rune
		list []CodeKey
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isInList(tt.args.c, tt.args.list); got != tt.want {
				t.Errorf("isInList() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestExactlyNum(t *testing.T) {
	type args struct {
		boxIds []string
		num    int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"2", args{boxIds: boxIds, num: 2}, 4},
		{"3", args{boxIds: boxIds, num: 3}, 3},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ExactlyNum(tt.args.boxIds, tt.args.num); got != tt.want {
				t.Errorf("ExactlyNum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCheckSum(t *testing.T) {
	type args struct {
		str []string
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
			if got := CheckSum(tt.args.str); got != tt.want {
				t.Errorf("CheckSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_compare(t *testing.T) {
	type args struct {
		a string
		b string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{a:"abcde", b:"axcye"},2},
		{"2", args{a:"fghij", b:"fguij"},1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := compare(tt.args.a, tt.args.b); got != tt.want {
				t.Errorf("compare() = %v, want %v", got, tt.want)
			}
		})
	}
}
