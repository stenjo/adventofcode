package day20

import (
	"reflect"
	"testing"

	"example.com/aoc2021/tools"
)

func TestTrenchMap_calcIndex(t *testing.T) {
	tests := []struct {
		name   string
		pixels TrenchMap
		want   int
	}{
		{"1", TrenchMap{0: "...", 1: "#..", 2: ".#."}, 34},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.pixels.calcIndex(); got != tt.want {
				t.Errorf("TrenchMap.calcIndex() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestEnhancement_getChar(t *testing.T) {
	type args struct {
		index int
	}
	tests := []struct {
		name string
		e    Enhancement
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", Enhancement("..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"), args{index: 34}, "#"},
		{"2", Enhancement("..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"), args{index: 0}, "."},
		{"3", Enhancement("..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"), args{index: 73}, "#"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.e.getChar(tt.args.index); got != tt.want {
				t.Errorf("Enhancement.getChar() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_loadData(t *testing.T) {
	type args struct {
		data []string
	}
	tests := []struct {
		name  string
		args  args
		want  Enhancement
		want1 TrenchMap
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := loadData(tt.args.data)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("loadData() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("loadData() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestTrenchMap_getSubMap(t *testing.T) {
	type args struct {
		x int
		y int
	}
	tests := []struct {
		name string
		m    TrenchMap
		args args
		want TrenchMap
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.m.getSubMap(tt.args.x, tt.args.y); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("TrenchMap.getSubMap() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrenchMap_expand(t *testing.T) {
	tm := TrenchMap{0: "#"}
	tests := []struct {
		name string
		m    *TrenchMap
		want TrenchMap
	}{
		// TODO: Add test cases.
		// {"1", &tm, TrenchMap{0: ".....", 1: ".....", 2: "..#..", 3: ".....", 4: "....."}},
	}
	for _, tt := range tests {
		tm[0] = "#"
		t.Run(tt.name, func(t *testing.T) {
			tt.m.expand()
			for i := 0; i < len((*tt.m)); i++ {
				if got := tt.m; (*got)[i] != tt.want[i] {
					t.Errorf("TrenchMap.expand() = %v, want %v", got, tt.want)
				}
			}
		})
	}
}

func TestTrenchMap_colAsStr(t *testing.T) {
	type args struct {
		x int
	}
	tests := []struct {
		name string
		m    TrenchMap
		args args
		want string
	}{
		// TODO: Add test cases.
		{"1", TrenchMap{0: "#"}, args{x: 0}, "#"},
		{"2", TrenchMap{0: ".#.", 1: ".#.", 2: ".#."}, args{x: 0}, "..."},
		// {"3", TrenchMap{0: "#"}, args{x: -1}, "."},
		// {"4", TrenchMap{0: "#"}, args{x: 1}, "."},
		{"5", TrenchMap{0: ".#.", 1: ".#.", 2: ".#."}, args{x: 1}, "###"},
		// {"6", TrenchMap{0: ".#.", 1: ".#.", 2: ".#."}, args{x: 3}, "..."},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.m.colAsStr(tt.args.x); got != tt.want {
				t.Errorf("TrenchMap.colAsStr() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCountBy2Enhancements(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: tools.GetData("test.txt")}, 9},
		{"2", args{str: tools.GetData("test_day20.txt")}, 35},
		{"3", args{str: tools.GetData("../../day20.txt")}, 5306},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCountBy2Enhancements(tt.args.str); got != tt.want {
				t.Errorf("GetCountBy3Enhancements() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrenchMap_refine(t *testing.T) {
	type args struct {
		e Enhancement
	}
	tests := []struct {
		name string
		tm   *TrenchMap
		args args
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tm.refine(tt.args.e); got != tt.want {
				t.Errorf("TrenchMap.refine() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrenchMap_count(t *testing.T) {
	tests := []struct {
		name string
		tm   TrenchMap
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tm.count(); got != tt.want {
				t.Errorf("TrenchMap.count() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetCountBy50Enhancements(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"1", args{str: tools.GetData("test.txt")}, 3123},
		{"2", args{str: tools.GetData("test_day20.txt")}, 3351},
		{"3", args{str: tools.GetData("../../day20.txt")}, 17497},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetCountBy50Enhancements(tt.args.str); got != tt.want {
				t.Errorf("GetCountBy50Enhancements() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrenchMap_print(t *testing.T) {
	tests := []struct {
		name string
		m    TrenchMap
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.m.print()
		})
	}
}
