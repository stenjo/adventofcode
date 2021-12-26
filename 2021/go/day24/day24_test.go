package day24

import (
	"reflect"
	"testing"

	"example.com/aoc2021/tools"
)

func TestAlu_compute(t *testing.T) {
	type args struct {
		i Inst
	}
	tests := []struct {
		name string
		alu  *Alu
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.alu.compute(tt.args.i); got != tt.want {
				t.Errorf("Alu.compute() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_atoi(t *testing.T) {
	type args struct {
		a string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := atoi(tt.args.a); got != tt.want {
				t.Errorf("atoi() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlu_getInput(t *testing.T) {
	tests := []struct {
		name string
		a    *Alu
		want int64
	}{
		// {"1", &Alu{args: []string{"inp x", "mul x -1"}}, -2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.a.getInput(); got != tt.want {
				t.Errorf("Alu.getInput() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlu_addInput(t *testing.T) {
	type args struct {
		val int64
	}
	tests := []struct {
		name string
		a    *Alu
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.a.addInput(tt.args.val); got != tt.want {
				t.Errorf("Alu.addInput() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlu_valOrVar(t *testing.T) {
	type args struct {
		v string
	}
	tests := []struct {
		name string
		alu  *Alu
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.alu.valOrVar(tt.args.v); got != tt.want {
				t.Errorf("Alu.valOrVar() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isNum(t *testing.T) {
	type args struct {
		v string
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
			if got := isNum(tt.args.v); got != tt.want {
				t.Errorf("isNum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestAlu_run(t *testing.T) {
	type args struct {
		args []string
	}
	tests := []struct {
		name string
		a    *Alu
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.a.run(tt.args.args); got != tt.want {
				t.Errorf("Alu.run() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRunOnNum(t *testing.T) {
	type args struct {
		num []int64
		ins []string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		{"1", args{num: []int64{2}, ins: []string{"inp x", "mul x -1"}}, -2},
		{"2", args{num: []int64{2, 6}, ins: []string{
			"inp z",
			"inp x",
			"mul z 3",
			"eql z x",
		}}, 1},
		{"3", args{num: []int64{8}, ins: []string{
			"inp w",
			"add z w",
			"mod z 2",
			"div w 2",
			"add y w",
			"mod y 2",
			"div w 2",
			"add x w",
			"mod x 2",
			"div w 2",
			"mod w 2",
		}}, 1},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := RunOnNum(tt.args.num, tt.args.ins); got != tt.want {
				t.Errorf("RunOnNum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_verifyMONAD(t *testing.T) {
	type args struct {
		monad int64
		args  []string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"1", args{monad:13579246899999, args:tools.GetData("../../day24.txt")}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := verifyMONAD(tt.args.monad, tt.args.args); got != tt.want {
				t.Errorf("verifyMONAD() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_intoToArr(t *testing.T) {
	type args struct {
		i int64
	}
	tests := []struct {
		name string
		args args
		want []int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := intoToArr(tt.args.i); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("intoToArr() = %v, want %v", got, tt.want)
			}
		})
	}
}
