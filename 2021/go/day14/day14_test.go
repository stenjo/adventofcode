package day14

import (
	"reflect"
	"testing"
)

func TestGetElementDiff(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{
			"NNCB", " ", "CH -> B", "HH -> N", "CB -> H", "NH -> C", "HB -> C", "HC -> B", "HN -> C", "NN -> C", "BH -> H", "NC -> B", "NB -> B", "BN -> B", "BB -> N", "BC -> B", "CC -> N", "CN -> C"}}, 1588},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetElementDiff(tt.args.str); got != tt.want {
				t.Errorf("GetElementDiff() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPolymer_RunStep(t *testing.T) {
	type args struct {
		rules map[string]string
	}
	tests := []struct {
		name string
		e    *Polymer
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.e.RunStep(tt.args.rules)
		})
	}
}

func TestParseRules(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want map[string]string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := ParseRules(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ParseRules() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPolymer_max(t *testing.T) {
	tests := []struct {
		name string
		e    Polymer
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.e.max(); got != tt.want {
				t.Errorf("Polymer.max() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestPolymer_min(t *testing.T) {
	tests := []struct {
		name string
		e    Polymer
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.e.min(); got != tt.want {
				t.Errorf("Polymer.min() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetElementDiff40(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{
			"NNCB", " ", "CH -> B", "HH -> N", "CB -> H", "NH -> C", "HB -> C", "HC -> B", "HN -> C", "NN -> C", "BH -> H", "NC -> B", "NB -> B", "BN -> B", "BB -> N", "BC -> B", "CC -> N", "CN -> C"}}, 2188189693529},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetElementDiff40(tt.args.str); got != tt.want {
				t.Errorf("GetElementDiff40() = %v, want %v", got, tt.want)
			}
		})
	}
}
