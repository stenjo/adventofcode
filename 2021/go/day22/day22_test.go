package day22

import (
	"reflect"
	"testing"

	"example.com/aoc2021/tools"
)

func TestCountOn(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		// TODO: Add test cases.
		{"1", args{str: tools.GetData("test.txt")}, 39},
		// {"2", args{str: tools.GetData("test2.txt")}, 590784},
		// {"3", args{str:tools.GetData("../../day22.txt")}, 547648},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := CountOn(tt.args.str); got != tt.want {
				t.Errorf("CountOn() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestCubeList_apply(t *testing.T) {
	type args struct {
		step Cuboid
	}
	tests := []struct {
		name string
		cbs  *CubeList
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.cbs.apply(tt.args.step); got != tt.want {
				t.Errorf("CubeList.apply() = %v, want %v", got, tt.want)
			}
		})
	}
}
//		{"1", args{rlis1:RangeList{{1,2},{7,9}}, rlist2:RangeList{{3,4},{5,6}}}, RangeList{{1,9}}},

func Test_toRange(t *testing.T) {
	type args struct {
		tl []Range
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := toRange(tt.args.tl); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("toRange() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_loadSteps(t *testing.T) {
	type args struct {
		str []string
		min xyz
		max xyz
	}
	tests := []struct {
		name string
		args args
		want []Cuboid
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := loadSteps(tt.args.str, tt.args.min, tt.args.max); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("loadSteps() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseRange(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want []Range
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseRange(tt.args.s); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseRange() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_makeRange(t *testing.T) {
	type args struct {
		minmax string
		from   int
		to     int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := makeRange(tt.args.minmax, tt.args.from, tt.args.to); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("makeRange() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRangeList_Len(t *testing.T) {
	tests := []struct {
		name string
		a    RangeList
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.a.Len(); got != tt.want {
				t.Errorf("RangeList.Len() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestRangeList_Swap(t *testing.T) {
	type args struct {
		i int
		j int
	}
	tests := []struct {
		name string
		a    RangeList
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.a.Swap(tt.args.i, tt.args.j)
		})
	}
}

func TestRangeList_Less(t *testing.T) {
	type args struct {
		i int
		j int
	}
	tests := []struct {
		name string
		a    RangeList
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.a.Less(tt.args.i, tt.args.j); got != tt.want {
				t.Errorf("RangeList.Less() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_merge(t *testing.T) {
	type args struct {
		rlis1  RangeList
		rlist2 RangeList
	}
	tests := []struct {
		name string
		args args
		want RangeList
	}{
		{"1", args{rlis1: RangeList{{1, 2}, {7, 9}}, rlist2: RangeList{{3, 4}, {5, 6}}}, RangeList{{1, 9}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := merge(tt.args.rlis1, tt.args.rlist2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("merge() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_abs(t *testing.T) {
	type args struct {
		val int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := abs(tt.args.val); got != tt.want {
				t.Errorf("abs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_min(t *testing.T) {
	type args struct {
		x int
		y int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := min(tt.args.x, tt.args.y); got != tt.want {
				t.Errorf("min() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_max(t *testing.T) {
	type args struct {
		x int
		y int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := max(tt.args.x, tt.args.y); got != tt.want {
				t.Errorf("max() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_mergeRange(t *testing.T) {
	type args struct {
		r1 Range
		r2 Range
	}
	tests := []struct {
		name string
		args args
		want RangeList
	}{
		{"1", args{r1: Range{}, r2: Range{}}, RangeList{{}}},
		{"2", args{r1: Range{1, 2}, r2: Range{3, 4}}, RangeList{{1, 4}}},
		{"3", args{r1: Range{}, r2: Range{3, 4}}, RangeList{{0, 0}, {3, 4}}},
		{"4", args{r1: Range{1, 2}, r2: Range{}}, RangeList{{0, 2}}},
		{"5", args{r1: Range{-10, 2}, r2: Range{3, 10}}, RangeList{{-10, 10}}},
		{"6", args{r1: Range{1, 3}, r2: Range{2, 5}}, RangeList{{1, 5}}},
		{"7", args{r1: Range{2, 5}, r2: Range{1, 3}}, RangeList{{1, 5}}},
		{"8", args{r1: Range{3, 10}, r2: Range{-10, 2}}, RangeList{{-10, 10}}},
		{"9", args{r1: Range{4, 10}, r2: Range{-10, 2}}, RangeList{{-10, 2}, {4, 10}}},
		{"10", args{r1: Range{-3, 10}, r2: Range{0, 2}}, RangeList{{-3, 10}}},
		{"11", args{r1: Range{-3, 2}, r2: Range{-10, 2}}, RangeList{{-10, 2}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := mergeRange(tt.args.r1, tt.args.r2); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("mergeRange() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_removeRange(t *testing.T) {
	type args struct {
		keep   Range
		remove Range
	}
	tests := []struct {
		name string
		args args
		want RangeList
	}{
		{"1", args{keep: Range{}, remove: Range{}}, RangeList{}},
		{"2", args{keep: Range{1, 5}, remove: Range{3, 4}}, RangeList{{1, 2}, {5,5}}},
		{"3", args{keep: Range{3, 4}, remove: Range{}}, RangeList{{3, 4}}},
		{"4", args{keep: Range{-1, 2}, remove: Range{}}, RangeList{{-1, -1},{1, 2}}},
		{"5", args{keep: Range{-10, 2}, remove: Range{3, 10}}, RangeList{{-10, 2}}},
		{"6", args{keep: Range{1, 3}, remove: Range{3, 5}}, RangeList{{1, 2}}},
		{"7", args{keep: Range{2, 5}, remove: Range{1, 3}}, RangeList{{4, 5}}},
		{"8", args{keep: Range{3, 10}, remove: Range{-10, 3}}, RangeList{{4, 10}}},
		{"9", args{keep: Range{4, 10}, remove: Range{-10, 10}}, RangeList{}},
		{"10", args{keep: Range{-3, 10}, remove: Range{0, 2}}, RangeList{{-3, -1},{3,10}}},
		{"11", args{keep: Range{-3, 2}, remove: Range{-10, 2}}, RangeList{}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := removeRange(tt.args.keep, tt.args.remove); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("removeRange() = %v, want %v", got, tt.want)
			}
		})
	}
}
