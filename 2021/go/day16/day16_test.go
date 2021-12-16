package day16

import (
	"reflect"
	"testing"
)

func Test_parseLiteral(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{s: "101111111000101000"}, 2021},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseLiteral(tt.args.s); got != tt.want {
				t.Errorf("parseLiteral() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getBits(t *testing.T) {
	type args struct {
		bits   string
		index  int
		length int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{bits: "101111111000101000", index: 12, length: 1}, 1},
		{"2", args{bits: "101111111000101000", index: 12, length: 3}, 5},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getBits(tt.args.bits, tt.args.index, tt.args.length); got != tt.want {
				t.Errorf("getBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_decode(t *testing.T) {
	type args struct {
		pkg string
	}
	tests := []struct {
		name  string
		args  args
		want  Package
		want1 string
	}{
		{"1", args{pkg: "D2FE28"}, Package{ver: 6, typ: 4, val: 2021}, ""},
		{"2", args{pkg: "38006F45291200"}, Package{ver: 1, typ: 6, val: 0}, "00000000000110111101000101001010010001001000000000"},
		{"3", args{pkg: "EE00D40C823060"}, Package{ver: 7, typ: 3, val: 0}, "10000000001101010000001100100000100011000001100000"},
		// 0101 0010 0010 0100
		{"4", args{pkg: "5224"}, Package{ver: 2, typ: 4, val: 20}, ""},
		// 1101 0001 010 0  - Had to add a bit
		{"5", args{pkg: "D14"}, Package{ver: 6, typ: 4, val: 10}, ""},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := decode(tt.args.pkg)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("decode() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("decode() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_toBits(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toBits(tt.args.s); got != tt.want {
				t.Errorf("toBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_pkgDecode(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want []Package
	}{
		{"1", args{s: "D2FE28"}, []Package{{ver: 6, typ: 4, val: 2021}}},
		// {"2", args{s: "38006F45291200"}, []Package{{ver: 1, typ: 6, val: 0}}},
		// {"3", args{s: "EE00D40C823060"}, []Package{{ver: 7, typ: 3, val: 0}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := pkgDecode(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("pkgDecode() = %v, want %v", got, tt.want)
			}
		})
	}
}
