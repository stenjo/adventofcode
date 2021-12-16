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

		// {"1", args{pkg: "D2FE28"}, Package{ver: 6, typ: 4, val: 2021}, "000"},
		// {"2", args{pkg: "D2FE287"}, Package{ver: 6, typ: 4, val: 2021}, "0000111"},
		// {"3", args{pkg: "D2FE289"}, Package{ver: 6, typ: 4, val: 2021}, "0001001"},

func Test_literals(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name  string
		args  args
		want  int
		want1 string
	}{
		// TODO: Add test cases.
		{"1", args{s: "101111111000101000"}, 2021, "000"},
		{"2", args{s: "1011111110001010000111"}, 2021, "0000111"},
		{"3", args{s: "1011111110001010001001"}, 2021, "0001001"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := literals(tt.args.s)
			if got != tt.want {
				t.Errorf("literals() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("literals() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_toHex(t *testing.T) {
	type args struct {
		bits string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{bits: "110100101111111000101000"}, "D2FE28"},
		{"2", args{bits: "110100101111111000101"}, "D2FE28"},
		{"3", args{bits: "1101001011111110001010"}, "D2FE28"},
		{"4", args{bits: "11010010111111100010100"}, "D2FE28"},
		{"5", args{bits: "110100101111111000101000110100101111111000101000110100101111111000101"}, "D2FE28D2FE28D2FE28"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toHex(tt.args.bits); got != tt.want {
				t.Errorf("toHex() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetVersionsSum(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		// {"1", args{s: "D2FE28"}, 6},
		// {"2", args{s: "38006F45291200"}, 9},
		// {"3", args{s: "EE00D40C823060"}, 14},
		// {"4", args{s: "8A004A801A8002F478"}, 16},
		{"5", args{s: "620080001611562C8802118E34"}, 12},
		{"6", args{s: "C0015000016115A2E0802F182340"}, 23},
		{"7", args{s: "A0016C880162017C3686B18A3D4780"}, 31},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetVersionsSum(tt.args.s); got != tt.want {
				t.Errorf("GetVersionsSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_pkgDecode(t *testing.T) {
	type args struct {
		bits string
	}
	tests := []struct {
		name  string
		args  args
		want  []Package
		want1 string
	}{
		// {"1", args{bits: "110100101111111000101000"}, []Package{{ver: 6, typ: 4, val: 2021}}, "000"},
		{"2", args{bits: "00111000000000000110111101000101001010010001001000000000"}, []Package{{ver: 1, typ: 6, val: 0}, {ver: 6, typ: 4, val: 10}, {ver: 2, typ: 4, val: 20}}, "0000000"},
		{"3", args{bits: "11101110000000001101010000001100100000100011000001100000"}, []Package{{ver: 7, typ: 3, val: 0}, {ver: 2, typ: 4, val: 1}, {ver: 4, typ: 4, val: 2}, {ver: 1, typ: 4, val: 3}},"00000"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := pkgDecode(tt.args.bits)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("pkgDecode() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("pkgDecode() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
