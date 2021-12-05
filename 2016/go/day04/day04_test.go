package day04

import (
	"reflect"
	"testing"
)

func TestRealRoomSectorIdSums(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{
			"aaaaa-bbb-z-y-x-123[abxyz]",
			"a-b-c-d-e-f-g-h-987[abcde]",
			"not-a-real-room-404[oarel]",
			"totally-real-room-200[decoy]",
		}}, 1514},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RealRoomSectorIdSums(tt.args.strList); got != tt.want {
				t.Errorf("RealRoomSectorIdSums() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_valid(t *testing.T) {
	type args struct {
		n Ename
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{n: Ename{encrypted: "aaaaa-bbb-z-y-x", sectorId: 123, checksum: "abxyz"}}, true},
		{"2", args{n: Ename{encrypted: "totally-real-room", sectorId: 200, checksum: "decoy"}}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := valid(tt.args.n); got != tt.want {
				t.Errorf("valid() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseEnames(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want []Ename
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseEnames(tt.args.strList); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseEnames() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseName(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want Ename
	}{
		// TODO: Add test cases.
		{"1", args{str: "aaaaa-bbb-z-y-x-123[abxyz]"}, Ename{encrypted: "aaaaa-bbb-z-y-x", sectorId: 123, checksum: "abxyz"}},
		{"2", args{str: "a-b-c-d-e-f-g-h-987[abcde]"}, Ename{encrypted: "a-b-c-d-e-f-g-h", sectorId: 987, checksum: "abcde"}},
		{"3", args{str: "not-a-real-room-404[oarel]"}, Ename{encrypted: "not-a-real-room", sectorId: 404, checksum: "oarel"}},
		{"4", args{str: "totally-real-room-200[decoy]"}, Ename{encrypted: "totally-real-room", sectorId: 200, checksum: "decoy"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseName(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseName() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getCheckSum(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{s: "aaaaa-bbb-z-y-x"}, "abxyz"},
		{"2", args{s: "a-b-c-d-e-f-g-h"}, "abcde"},
		{"3", args{s: "not-a-real-room"}, "oarel"},
		{"4", args{s: "totally-real-room"}, "loart"},
		{"5", args{s: "Mnqsg-Onkd-naidbsr"}, "ndsMO"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getCheckSum(tt.args.s); got != tt.want {
				t.Errorf("getCheckSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_reverse(t *testing.T) {
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
			if got := reverse(tt.args.s); got != tt.want {
				t.Errorf("reverse() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_singles(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{s: "aaaaabbbzyx"}, "abzyx"},
		{"2", args{s: "abcdefgh"}, "abcdefgh"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singles(tt.args.s); got != tt.want {
				t.Errorf("singles() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestStringToRuneSlice(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want []rune
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := StringToRuneSlice(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("StringToRuneSlice() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSortStringByCharacter(t *testing.T) {
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
			if got := SortStringByCharacter(tt.args.s); got != tt.want {
				t.Errorf("SortStringByCharacter() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNortPoleObjectsId(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{strList: []string{
			"aaaaa-bbb-z-y-x-123[abxyz]",
			"a-b-c-d-e-f-g-h-987[abcde]",
			"zadft-baxq-anvqofe-404[oarel]",
			"totally-real-room-200[decoy]",
		}}, 404},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := NortPoleObjectsId(tt.args.strList); got != tt.want {
				t.Errorf("NortPoleObjectsId() = %v, want %v", got, tt.want)
			}
		})
	}
}


func TestRotate(t *testing.T) {
	type args struct {
		r    rune
		n    int
		left bool
	}
	tests := []struct {
		name string
		args args
		want rune
	}{
		// TODO: Add test cases.
		{"1", args{r: 'a', n: 1, left: false}, 'b'},
		{"2", args{r: 'a', n: 1, left: true}, 'z'},
		{"3", args{r: 'a', n: 27, left: true}, 'z'},
		{"4", args{r: 'a', n: 27, left: false}, 'b'},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Rotate(tt.args.r, tt.args.n, tt.args.left); got != tt.want {
				t.Errorf("Rotate() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestReverseEncrypt(t *testing.T) {
	type args struct {
		s string
		n int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{s: "North Pole objects", n:404}, "zadft-baxq-anvqofe"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReverseEncrypt(tt.args.s, tt.args.n); got != tt.want {
				t.Errorf("ReverseEncrypt() = %v, want %v", got, tt.want)
			}
		})
	}
}
