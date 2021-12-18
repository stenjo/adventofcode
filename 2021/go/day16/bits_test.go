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
		// TODO: Add test cases.
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
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.bits.getBits(tt.args.index, tt.args.length); got != tt.want {
				t.Errorf("Bits.getBits() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBits_toHex(t *testing.T) {
	tests := []struct {
		name string
		b    Bits
		want string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.b.toHex(); got != tt.want {
				t.Errorf("Bits.toHex() = %v, want %v", got, tt.want)
			}
		})
	}
}

