package day16

import (
	"reflect"
	"testing"
)

func TestPackage_sumVer(t *testing.T) {
	tests := []struct {
		name string
		p    Package
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.p.sumVer(); got != tt.want {
				t.Errorf("Package.sumVer() = %v, want %v", got, tt.want)
			}
		})
	}
}



func TestPackage_parseLiteral(t *testing.T) {
	type args struct {
		b Bits
	}
	tests := []struct {
		name string
		p    *Package
		args args
		want Bits
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.p.parseLiteral(tt.args.b); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Package.parseLiteral() = %v, want %v", got, tt.want)
			}
		})
	}
}
