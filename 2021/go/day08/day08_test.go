package day08

import (
	"reflect"
	"testing"
)

func Test_parseNotes(t *testing.T) {
	type args struct {
		strlns []string
	}
	tests := []struct {
		name string
		args args
		want []Note
	}{
		// TODO: Add test cases.
		// {"1", args{strlns: []string{"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"}},
		// []Note{signals: []string{"acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"}, digits: []string{"cdfeb", "fcadb", "cdfeb", "cdbaf"}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseNotes(tt.args.strlns); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseNotes() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetUniqueSegmentsDigitCount(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"}}, 2},
		{"2", args{str: []string{"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb"}}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetUniqueSegmentsDigitCount(tt.args.str); got != tt.want {
				t.Errorf("GetUniqueSegmentsDigitCount() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_intInList(t *testing.T) {
	type args struct {
		i    int
		list []int
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
			if got := intInList(tt.args.i, tt.args.list); got != tt.want {
				t.Errorf("intInList() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNote_decode(t *testing.T) {
	tests := []struct {
		name string
		n    Note
		want int
	}{
		// TODO: Add test cases.
		{"1", Note{signals: []string{"acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"}, digits: []string{"cdfeb", "fcadb", "cdfeb", "cdbaf"}}, 5353},
		{"2", Note{signals: []string{"aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge", "gcbea", "fcaegb", "dgceab", "fcbdga"}, digits: []string{"gecf", "egdcabf", "bgf", "bfgea"}}, 4873},
		{"3", Note{signals: []string{"gcafb", "gcf", "dcaebfg", "ecagb", "gf", "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"}, digits: []string{"fgae", "cfgab", "fg", "bagce"}}, 4315},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.n.decode(); got != tt.want {
				t.Errorf("Note.decode() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_remove(t *testing.T) {
	type args struct {
		s   []string
		str string
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
			if got := remove(tt.args.s, tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("remove() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sortStrElements(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want []string
	}{
		{"1", args{str:[]string{"abcd", "efgh"}}, []string{"abcd", "efgh"}},
		{"2", args{str:[]string{"acbd", "fghe"}}, []string{"abcd", "efgh"}},
		{"3", args{str:[]string{"dabc", "fegh"}}, []string{"abcd", "efgh"}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sortStrElements(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("sortStrElements() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_hasCommonWith(t *testing.T) {
	type args struct {
		s1 string
		s2 string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{s1: "bcdef", s2: ""}, 0},
		{"2", args{s1: "bcdef", s2: "cd"}, 2},
		{"3", args{s1: "bcdef", s2: "f"}, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := hasCommonWith(tt.args.s1, tt.args.s2); got != tt.want {
				t.Errorf("hasCommonWith() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_getSegsForVal(t *testing.T) {
	type args struct {
		val int
		m   map[string]int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", args{val: 1, m: map[string]int{"a": 0, "ab": 1, "ac": 2}}, "ab"},
		{"2", args{val: 9, m: map[string]int{"abcdefg": 8}}, ""},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getSegsForVal(tt.args.val, tt.args.m); got != tt.want {
				t.Errorf("getSegsForVal() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sortRunes_Less(t *testing.T) {
	type args struct {
		i int
		j int
	}
	tests := []struct {
		name string
		s    sortRunes
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.Less(tt.args.i, tt.args.j); got != tt.want {
				t.Errorf("sortRunes.Less() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sortRunes_Swap(t *testing.T) {
	type args struct {
		i int
		j int
	}
	tests := []struct {
		name string
		s    sortRunes
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.s.Swap(tt.args.i, tt.args.j)
		})
	}
}

func Test_sortRunes_Len(t *testing.T) {
	tests := []struct {
		name string
		s    sortRunes
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.Len(); got != tt.want {
				t.Errorf("sortRunes.Len() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestSortString(t *testing.T) {
	type args struct {
		s string
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
			if got := SortString(tt.args.s); got != tt.want {
				t.Errorf("SortString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetOutputValueSum(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		// TODO: Add test cases.
		{"1", args{[]string{"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"}}, 8394},
		{"2", args{[]string{
			"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
			"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
		}}, 8394 + 9781},
		{"3", args{[]string{
			"be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
			"edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
			"fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
			"fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
			"aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
			"fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
			"gf dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf | cefg dcbef fcge gbcadfe",
			"gebcd bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg | ed bcgafe cdgba cbgef",
			"egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
			"gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
		}}, 61229},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetOutputValueSum(tt.args.str); got != tt.want {
				t.Errorf("GetOutputValueSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sortByLen(t *testing.T) {
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
			if got := sortByLen(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("sortByLen() = %v, want %v", got, tt.want)
			}
		})
	}
}
