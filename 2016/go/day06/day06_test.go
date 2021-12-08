package day06

import (
	"reflect"
	"testing"
)

func TestGetErrorCorrected(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"1", args{strList: []string{"eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"}}, "easter"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetErrorCorrected(tt.args.strList); got != tt.want {
				t.Errorf("GetErrorCorrected() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_transpose(t *testing.T) {
	type args struct {
		s []string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := transpose(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("transpose() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_findPopular(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name  string
		args  args
		want  rune
		want1 int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := findPopular(tt.args.s)
			if got != tt.want {
				t.Errorf("findPopular() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("findPopular() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestGetModifiedCorrected(t *testing.T) {
	type args struct {
		strList []string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"1", args{strList: []string{"eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa", "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"}}, "advent"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetModifiedCorrected(tt.args.strList); got != tt.want {
				t.Errorf("GetModifiedCorrected() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_findLeastPopular(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name  string
		args  args
		want  rune
		want1 int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := findLeastPopular(tt.args.s)
			if got != tt.want {
				t.Errorf("findLeastPopular() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("findLeastPopular() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
