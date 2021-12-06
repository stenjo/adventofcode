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
		{"1", args{str:"abc"}, "18f47a30"},
		{"1", args{str:"ojvtpuvg"}, "4543c154"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPassword(tt.args.str); got != tt.want {
				t.Errorf("GetPassword() = %v, want %v", got, tt.want)
			}
		})
	}
}
