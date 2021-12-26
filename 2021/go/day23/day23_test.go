// from https://github.com/1e9y/adventofcode/blob/main/2021/day23/day23.go

package day23

import (
	"reflect"
	"testing"
)

func Test_loc(t *testing.T) {
	type args struct {
		xy [2]int
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
			if got := loc(tt.args.xy); got != tt.want {
				t.Errorf("loc() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBurrow_moveToHallway(t *testing.T) {
	type args struct {
		a [2]int
	}
	tests := []struct {
		name   string
		burrow Burrow
		args   args
		want   []Step
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.burrow.moveToHallway(tt.args.a); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Burrow.moveToHallway() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBurrow_folded(t *testing.T) {
	tests := []struct {
		name   string
		burrow Burrow
		want   bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.burrow.folded(); got != tt.want {
				t.Errorf("Burrow.folded() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBurrow_moveToRoom(t *testing.T) {
	type args struct {
		a [2]int
	}
	tests := []struct {
		name   string
		burrow Burrow
		args   args
		want   []Step
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.burrow.moveToRoom(tt.args.a); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Burrow.moveToRoom() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBurrow_empty(t *testing.T) {
	type args struct {
		pos [2]int
	}
	tests := []struct {
		name   string
		burrow Burrow
		args   args
		want   bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.burrow.empty(tt.args.pos); got != tt.want {
				t.Errorf("Burrow.empty() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestBurrow_move(t *testing.T) {
	tests := []struct {
		name   string
		burrow Burrow
		want   []Step
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.burrow.move(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Burrow.move() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_organize(t *testing.T) {
	type args struct {
		input  []string
		target Burrow
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
			if got := organize(tt.args.input, tt.args.target); got != tt.want {
				t.Errorf("organize() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestA(t *testing.T) {
	type args struct {
		input *Challenge
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
			if got := A(tt.args.input); got != tt.want {
				t.Errorf("A() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestB(t *testing.T) {
	type args struct {
		input *Challenge
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
			if got := B(tt.args.input); got != tt.want {
				t.Errorf("B() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPart1(t *testing.T) {
	tests := []struct {
		name string
	}{
		// TODO: Add test cases.
		{"1"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			Part1()
		})
	}
}
