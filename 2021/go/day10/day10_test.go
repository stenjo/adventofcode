package day10

import (
	"reflect"
	"testing"
)

func TestGetSyntaxErrorPoints(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{
			"[({(<(())[]>[[{[]{<()<>>",
			"[(()[<>])]({[<{<<[]>>(",
			"{([(<{}[<>[]}>{[]{[(<()>",
			"(((({<>}<{<{<>}{[]{[]{}",
			"[[<[([]))<([[{}[[()]]]",
			"[{[{({}]{}}([{[{{{}}([]",
			"{<[[]]>}<{[{[{[]{()[[[]",
			"[<(<(<(<{}))><([]([]()",
			"<{([([[(<>()){}]>(<<{{",
			"<{([{{}}[<[[[<>{}]]]>[]]",
		}}, 26397},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetSyntaxErrorPoints(tt.args.str); got != tt.want {
				t.Errorf("GetSyntaxErrorPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_sum(t *testing.T) {
	type args struct {
		i []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{i: []int{2, 3, 4, 1}}, 10},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := sum(tt.args.i); got != tt.want {
				t.Errorf("sum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_errorPoints(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
		{"1", args{str:[]string{
			"{([(<{}[<>[]}>{[]{[(<()>",
			"[[<[([]))<([[{}[[()]]]",
			"[{[{({}]{}}([{[{{{}}([]",
			"[<(<(<(<{}))><([]([]()",
			"<{([([[(<>()){}]>(<<{{",
		}}, []int{1197, 3, 57, 3, 25137}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := errorPoints(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("errorPoints() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetSyntaxError(t *testing.T) {
	type args struct {
		line string
	}
	tests := []struct {
		name string
		args args
		want rune
	}{
		// TODO: Add test cases.
		{"1", args{line: "{([(<{}[<>[]}>{[]{[(<()>"}, '}'},
		{"2", args{line: "[[<[([]))<([[{}[[()]]]"}, ')'},
		{"3", args{line: "[{[{({}]{}}([{[{{{}}([]"}, ']'},
		{"4", args{line: "[<(<(<(<{}))><([]([]()"}, ')'},
		{"5", args{line: "<{([([[(<>()){}]>(<<{{"}, '>'},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetSyntaxError(tt.args.line); got != tt.want {
				t.Errorf("GetSyntaxError() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestStack_IsEmpty(t *testing.T) {
	tests := []struct {
		name string
		s    *Stack
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.IsEmpty(); got != tt.want {
				t.Errorf("Stack.IsEmpty() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestStack_Push(t *testing.T) {
	type args struct {
		r rune
	}
	tests := []struct {
		name string
		s    *Stack
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.s.Push(tt.args.r)
		})
	}
}

func TestStack_Pop(t *testing.T) {
	tests := []struct {
		name  string
		s     *Stack
		want  rune
		want1 bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := tt.s.Pop()
			if got != tt.want {
				t.Errorf("Stack.Pop() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("Stack.Pop() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestGetCompletionScore(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str:[]string{
			"[({(<(())[]>[[{[]{<()<>>",
			"[(()[<>])]({[<{<<[]>>(",
			"{([(<{}[<>[]}>{[]{[(<()>",
			"(((({<>}<{<{<>}{[]{[]{}",
			"[[<[([]))<([[{}[[()]]]",
			"[{[{({}]{}}([{[{{{}}([]",
			"{<[[]]>}<{[{[{[]{()[[[]",
			"[<(<(<(<{}))><([]([]()",
			"<{([([[(<>()){}]>(<<{{",
			"<{([{{}}[<[[[<>{}]]]>[]]",
		}}, 288957},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCompletionScore(tt.args.str); got != tt.want {
				t.Errorf("GetCompletionScore() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_middle(t *testing.T) {
	type args struct {
		i []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{i:[]int{1, 2, 3}}, 2},
		{"2", args{i:[]int{100, 20, 3}}, 20},
		{"3", args{i:[]int{288957, 5566, 1480781, 995444, 294}}, 288957},
		
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := middle(tt.args.i); got != tt.want {
				t.Errorf("middle() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCompletionScores(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{"1", args{str:[]string{
			"[({(<(())[]>[[{[]{<()<>>",
			"[(()[<>])]({[<{<<[]>>(",
			"{([(<{}[<>[]}>{[]{[(<()>",
			"(((({<>}<{<{<>}{[]{[]{}",
			"[[<[([]))<([[{}[[()]]]",
			"[{[{({}]{}}([{[{{{}}([]",
			"{<[[]]>}<{[{[{[]{()[[[]",
			"[<(<(<(<{}))><([]([]()",
			"<{([([[(<>()){}]>(<<{{",
			"<{([{{}}[<[[[<>{}]]]>[]]",
		}}, []int{288957, 5566, 1480781, 995444, 294}},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CompletionScores(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("CompletionScores() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetScore(t *testing.T) {
	type args struct {
		compl string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{compl:"}}]])})]"}, 288957},
		{"2", args{compl:")}>]})"}, 5566},
		{"3", args{compl:"}}>}>))))"}, 1480781},
		{"4", args{compl:"]]}}]}]}>"}, 995444},
		{"5", args{compl:"])}>"}, 294},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetScore(tt.args.compl); got != tt.want {
				t.Errorf("GetScore() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCompletionString(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{"1", args{s:"[({(<(())[]>[[{[]{<()<>>"}, "}}]])})]"},
		{"2", args{s:"[(()[<>])]({[<{<<[]>>("}, ")}>]})"},
		{"3", args{s:"(((({<>}<{<{<>}{[]{[]{}"}, "}}>}>))))"},
		{"4", args{s:"{<[[]]>}<{[{[{[]{()[[[]"}, "]]}}]}]}>"},
		{"5", args{s:"<{([{{}}[<[[[<>{}]]]>[]]"}, "])}>"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCompletionString(tt.args.s); got != tt.want {
				t.Errorf("GetCompletionString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_matching(t *testing.T) {
	type args struct {
		d rune
	}
	tests := []struct {
		name string
		args args
		want rune
	}{
		{"1", args{d:'['}, ']'},
		{"1", args{d:'('}, ')'},
		{"1", args{d:'{'}, '}'},
		{"1", args{d:'<'}, '>'},
		{"5", args{d:'H'}, '_'},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := matching(tt.args.d); got != tt.want {
				t.Errorf("matching() = %v, want %v", got, tt.want)
			}
		})
	}
}
