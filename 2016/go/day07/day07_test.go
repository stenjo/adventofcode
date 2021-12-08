package day07

import (
	"reflect"
	"testing"
)

func TestCountIPsSupportingTLS(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{[]string{
			"abba[mnop]qrst",
			"abcd[bddb]xyyx",
			"aaaa[qwer]tyui",
			"ioxxoj[asdfgh]zxcvbn",
			}}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CountIPsSupportingTLS(tt.args.str); got != tt.want {
				t.Errorf("CountIPsSupportingTLS() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseLines(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want []Ip
	}{
		{"1", args{[]string{"abba[mnop]qrst"}}, []Ip{{"abba|qrst", "mnop"}}},
		{"2", args{[]string{"abcd[bddb]xyyx"}}, []Ip{{"abcd|xyyx", "bddb"}}},
		{"3", args{[]string{"aaaa[qwer]tyui"}}, []Ip{{"aaaa|tyui", "qwer"}}},
		{"4", args{[]string{"ioxxoj[asdfgh]zxcvbn"}}, []Ip{{"ioxxoj|zxcvbn", "asdfgh"}}},
		{"4", args{[]string{"ioxxoj[asdfgh]zxcvbn", "aaaa[qwer]tyui"}}, []Ip{{"ioxxoj|zxcvbn", "asdfgh"}, {"aaaa|tyui", "qwer"}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseLines(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseLines() = %v, want %v", got, tt.want)
			}
		})
	}
}
