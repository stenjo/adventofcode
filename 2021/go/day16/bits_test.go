package day16

import (
	"reflect"
	"testing"
)

func Test_toBits(t *testing.T) {
	type args struct {
		hex string
	}
	tests := []struct {
		name string
		args args
		want Bits
	}{
		{"1", args{hex: "D2FE28"}, Bits("110100101111111000101000")},
		{"2", args{hex: "38006F45291200"}, Bits("00111000000000000110111101000101001010010001001000000000")},
		{"3", args{hex: "EE00D40C823060"}, Bits("11101110000000001101010000001100100000100011000001100000")},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toBits(tt.args.hex); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("toBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBits_getBits(t *testing.T) {
	type args struct {
		index  int
		length int
	}
	tests := []struct {
		name string
		bits Bits
		args args
		want int
	}{
		{"1", Bits("11101110000000001101010000001100100000100011000001100000"), args{index: 1, length: 1}, 1},
		{"2", Bits("11101110000000001101010000001100100000100011000001100000"), args{index: 18, length: 4}, 5},
		{"3", Bits("11101110000000001101010000001100100000100011000001100000"), args{index: 55, length: 1}, 0},
		{"4", Bits("11101110000000001101010000001100100000100011000001100000"), args{index: 50, length: 0}, 0},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.bits.getBits(tt.args.index, tt.args.length); got != tt.want {
				t.Errorf("Bits.getBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

