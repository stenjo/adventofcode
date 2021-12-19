package day19

import (
	"reflect"
	"testing"
)

func TestBeacon_align(t *testing.T) {
	type args struct {
		s *Signal
	}
	tests := []struct {
		name string
		b    *Signal
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.b.align(tt.args.s)
		})
	}
}

func TestBeacon_compare(t *testing.T) {
	type args struct {
		a *Signal
	}
	tests := []struct {
		name string
		b    *Signal
		args args
		want [][]string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.b.compare(tt.args.a); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Beacon.compare() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRelatives_indexOf(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		r    Relatives
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.r.indexOf(tt.args.s); got != tt.want {
				t.Errorf("Relatives.indexOf() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_abs(t *testing.T) {
	type args struct {
		val int
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
			if got := abs(tt.args.val); got != tt.want {
				t.Errorf("abs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_min(t *testing.T) {
	type args struct {
		x int
		y int
		z int
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
			if got := min(tt.args.x, tt.args.y, tt.args.z); got != tt.want {
				t.Errorf("min() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_max(t *testing.T) {
	type args struct {
		x int
		y int
		z int
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
			if got := max(tt.args.x, tt.args.y, tt.args.z); got != tt.want {
				t.Errorf("max() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_hypot(t *testing.T) {
	type args struct {
		x int
		y int
		z int
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
			if got := hypot(tt.args.x, tt.args.y, tt.args.z); got != tt.want {
				t.Errorf("hypot() = %v, want %v", got, tt.want)
			}
		})
	}
}
