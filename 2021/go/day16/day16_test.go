package day16

import (
	"strings"
	"testing"

	"example.com/aoc2021/tools"
)

func TestGetVersionsSum(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{s: "D2FE28"}, 6},
		{"2", args{s: "38006F45291200"}, 9},
		{"3", args{s: "EE00D40C823060"}, 14},
		{"4", args{s: "8A004A801A8002F478"}, 16},
		{"5", args{s: "620080001611562C8802118E34"}, 12},
		{"6", args{s: "C0015000016115A2E0802F182340"}, 23},
		{"7", args{s: "A0016C880162017C3686B18A3D4780"}, 31},
		{"8", args{s: strings.Join(tools.GetData("../../day16.txt"), "")}, 963},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetVersionsSum(tt.args.s); got != tt.want {
				t.Errorf("GetVersionsSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetValue(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"C200B40A82", args{s: "C200B40A82"}, 3},
		{"04005AC33890", args{s: "04005AC33890"}, 54},
		{"880086C3E88112", args{s: "880086C3E88112"}, 7},
		{"CE00C43D881120", args{s: "CE00C43D881120"}, 9},
		{"D8005AC2A8F0", args{s: "D8005AC2A8F0"}, 1},
		{"F600BC2D8F", args{s: "F600BC2D8F"}, 0},
		{"9C005AC2F8F0", args{s: "9C005AC2F8F0"}, 0},
		{"9C0141080250320F1802104A08", args{s: "9C0141080250320F1802104A08"}, 1},
		{"9", args{s: strings.Join(tools.GetData("../../day16.txt"), "")}, 1549026292886},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetValue(tt.args.s); got != tt.want {
				t.Errorf("GetValue() = %v, want %v", got, tt.want)
			}
		})
	}
}
