package day01

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestNextPos(t *testing.T) {
	var p complex64 = complex(0, 0)
	var d complex64 = complex(0, 1)
	var next, nd = NextPos(d, p, "R2")
	assert.Equal(t, real(next), float32(2.0))
	next, _ = NextPos(nd, next, "L3")
	assert.Equal(t, real(next), float32(2.0))
	assert.Equal(t, imag(next), float32(3.0))

}

func TestRunString(t *testing.T) {
	var result, _ = RunString("R2, L3")
	assert.Equal(t, result, complex64(complex(2, 3)))
	result, _ = RunString("R2, R2, R2")
	assert.Equal(t, result, complex64(complex(0, -2)))
	var _, blocks = RunString("R5, L5, R5, R3")
	assert.Equal(t, blocks, 12.0)
}

var input = "R8, R4, R4, R8"
func TestVisitedTwice(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name  string
		args  args
		want  complex64
		want1 int
	}{
		// TODO: Add test cases.
		{"1", args{str:input}, complex(1,1), 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := VisitedTwice(tt.args.str)
			if got != tt.want {
				t.Errorf("VisitedTwice() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("VisitedTwice() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func Test_posInList(t *testing.T) {
	type args struct {
		p complex64
		l []complex64
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
			if got := posInList(tt.args.p, tt.args.l); got != tt.want {
				t.Errorf("posInList() = %v, want %v", got, tt.want)
			}
		})
	}
}
