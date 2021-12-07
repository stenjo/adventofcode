package day05

import (
	"reflect"
	"testing"
)

func TestGetHashCount(t *testing.T) {
	type args struct {
		key   string
		depth int
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
			if got := GetHashCount(tt.args.key, tt.args.depth); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("GetHashCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetPassword(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{str: "abc"}, "18f47a30"},
		{"1", args{str: "ojvtpuvg"}, "4543c154"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPassword(tt.args.str); got != tt.want {
				t.Errorf("GetPassword() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetHash(t *testing.T) {
	type args struct {
		key  string
		seed string
	}
	tests := []struct {
		name  string
		args  args
		want  string
		want1 bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := GetHash(tt.args.key, tt.args.seed)
			if got != tt.want {
				t.Errorf("GetHash() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("GetHash() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestGetBetterSolution(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"1", args{str: "abc"}, "\r05ace8e3"},
		// {"1", args{str: "ojvtpuvg"}, "1050cbbd"},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetBetterSolution(tt.args.str); got != tt.want {
				t.Errorf("GetBetterSolution() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestUpdatePassword(t *testing.T) {
	type args struct {
		password []string
		key      string
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
			if got := UpdatePassword(tt.args.password, tt.args.key); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("UpdatePassword() = %v, want %v", got, tt.want)
			}
		})
	}
}
