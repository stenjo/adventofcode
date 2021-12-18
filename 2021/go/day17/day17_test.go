package day17

import (
	"reflect"
	"testing"
)

func TestGetHighestY(t *testing.T) {
	type args struct {
		trgt string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{trgt: "target area: x=20..30, y=-10..-5"}, 45},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetHighestY(tt.args.trgt); got != tt.want {
				t.Errorf("GetHighestY() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_loadTarget(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want Target
	}{
		{"1", args{str: "target area: x=20..30, y=-10..-5"}, Target{min: xy{20, -10}, max: xy{30, -5}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := loadTarget(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("loadTarget() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_calculate(t *testing.T) {
	type args struct {
		p xy
		v xy
	}
	tests := []struct {
		name  string
		args  args
		want  xy
		want1 xy
	}{
		// TODO: Add test cases.
		{"1", args{p: xy{10, -5}, v: xy{20, -10}}, xy{30, -15}, xy{19, -11}},
		{"2", args{p: xy{10, -5}, v: xy{0, -10}}, xy{10, -15}, xy{0, -11}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := calculate(tt.args.p, tt.args.v)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("calculate() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("calculate() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

// {"1", args{p: xy{20, -5}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, true},
// {"2", args{p: xy{20, -4}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, false},
// {"3", args{p: xy{19, -5}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, false},
// {"4", args{p: xy{30, -5}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, true},
// {"5", args{p: xy{20, -10}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, true},

// {"1", args{p: xy{20, -5}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, false},
// {"2", args{p: xy{20, -4}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, false},
// {"3", args{p: xy{19, -5}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, false},
// {"4", args{p: xy{30, -11}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, true},
// {"5", args{p: xy{31, -10}, target: Target{min: xy{20, -10}, max: xy{30, -5}}}, true},

func TestTarget_isAbove(t *testing.T) {
	type args struct {
		p xy
	}
	tests := []struct {
		name string
		tr   *Target
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.isAbove(tt.args.p); got != tt.want {
				t.Errorf("Target.isAbove() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTarget_isShortOf(t *testing.T) {
	type args struct {
		p xy
	}
	tests := []struct {
		name string
		tr   *Target
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.isShortOf(tt.args.p); got != tt.want {
				t.Errorf("Target.isShortOf() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTarget_isWithin(t *testing.T) {
	type args struct {
		p xy
	}
	tests := []struct {
		name string
		tr   *Target
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.isWithin(tt.args.p); got != tt.want {
				t.Errorf("Target.isWithin() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTarget_isBeyond(t *testing.T) {
	type args struct {
		p xy
	}
	tests := []struct {
		name string
		tr   *Target
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.isBeyond(tt.args.p); got != tt.want {
				t.Errorf("Target.isBeyond() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_shoot(t *testing.T) {
	type args struct {
		p Probe
		t Target
	}
	tests := []struct {
		name  string
		args  args
		want  int
		want1 xy
	}{
		// TODO: Add test cases.
		{"1", args{p: Probe{pos: xy{0, 0}, vel: xy{7, 2}}, t: Target{min: xy{20, -10}, max: xy{30, -5}}}, 3, xy{28, -7}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := shoot(tt.args.p, tt.args.t)
			if got != tt.want {
				t.Errorf("shoot() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("shoot() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestTarget_isPassedThroug(t *testing.T) {
	type args struct {
		p xy
	}
	tests := []struct {
		name string
		tr   *Target
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.isPassedThroug(tt.args.p); got != tt.want {
				t.Errorf("Target.isPassedThroug() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetNumOfDistinctV(t *testing.T) {
	type args struct {
		trgt string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{trgt: "target area: x=20..30, y=-10..-5"}, 112},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetNumOfDistinctV(tt.args.trgt); got != tt.want {
				t.Errorf("GetNumOfDistinctV() = %v, want %v", got, tt.want)
			}
		})
	}
}
