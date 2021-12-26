package day23

import (
	"io"
	"reflect"
	"testing"
)

func TestMustAtoi(t *testing.T) {
	type args struct {
		a string
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
			if got := MustAtoi(tt.args.a); got != tt.want {
				t.Errorf("MustAtoi() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_newChallengeFromReader(t *testing.T) {
	type args struct {
		r io.Reader
		c io.Closer
	}
	tests := []struct {
		name string
		args args
		want *Challenge
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := newChallengeFromReader(tt.args.r, tt.args.c); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("newChallengeFromReader() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestReadChallengeForDay(t *testing.T) {
	type args struct {
		year string
		day  string
	}
	tests := []struct {
		name string
		args args
		want *Challenge
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReadChallengeForDay(tt.args.year, tt.args.day); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ReadChallengeForDay() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestReadChallengeFromFile(t *testing.T) {
	tests := []struct {
		name string
		want *Challenge
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReadChallengeFromFile(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ReadChallengeFromFile() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestReadChallengeFromLiteral(t *testing.T) {
	type args struct {
		input string
	}
	tests := []struct {
		name string
		args args
		want *Challenge
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ReadChallengeFromLiteral(tt.args.input); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ReadChallengeFromLiteral() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestChallenge_Lines(t *testing.T) {
	tests := []struct {
		name string
		c    *Challenge
		want <-chan string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.c.Lines(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Challenge.Lines() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestChallenge_LineSlice(t *testing.T) {
	tests := []struct {
		name       string
		c          *Challenge
		wantResult []string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := tt.c.LineSlice(); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Challenge.LineSlice() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}

func TestChallenge_String(t *testing.T) {
	tests := []struct {
		name       string
		c          *Challenge
		wantResult string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := tt.c.String(); gotResult != tt.wantResult {
				t.Errorf("Challenge.String() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}

func TestChallenge_Matrix(t *testing.T) {
	tests := []struct {
		name       string
		c          *Challenge
		wantResult [][]int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if gotResult := tt.c.Matrix(); !reflect.DeepEqual(gotResult, tt.wantResult) {
				t.Errorf("Challenge.Matrix() = %v, want %v", gotResult, tt.wantResult)
			}
		})
	}
}
