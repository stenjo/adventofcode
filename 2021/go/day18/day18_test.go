package day18

import (
	"reflect"
	"testing"
)

func TestGetMagnitude(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		// {"1", args{str:[]string{"[[1,2],[[3,4],5]]"}},143},
		// {"2", args{str:[]string{"[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"}},1384},
		// {"3", args{str:[]string{"[[[[1,1],[2,2]],[3,3]],[4,4]]"}},445},
		// {"4", args{str:[]string{"[[[[3,0],[5,3]],[4,4]],[5,5]]"}},791},
		// {"5", args{str:[]string{"[[[[5,0],[7,4]],[5,5]],[6,6]]"}},1137},
		// {"6", args{str:[]string{"[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]"}},3488},
		// {"7", args{str:[]string{"[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"}},4140},
		{"8", args{str:[]string{
			"[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
			"[[[5,[2,8]],4],[5,[[9,9],0]]]",
			"[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
			"[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
			"[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
			"[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
			"[[[[5,4],[7,7]],8],[[8,3],8]]",
			"[[9,3],[[9,9],[6,[4,9]]]]",
			"[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
			"[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"}},4140},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetMagnitude(tt.args.str); got != tt.want {
				t.Errorf("GetMagnitude() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_parseFishPairs(t *testing.T) {
	type args struct {
		str string
	}
	tests := []struct {
		name string
		args args
		want []Fish
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := parseFishPairs(tt.args.str); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("parseFishPairs() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_finalSnailFish(t *testing.T) {
	type args struct {
		raw []string
	}
	tests := []struct {
		name string
		args args
		want []Fish
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := finalSnailFish(tt.args.raw); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("finalSnailFish() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_finalSum(t *testing.T) {
	type args struct {
		raw []string
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
			if got := finalSum(tt.args.raw); got != tt.want {
				t.Errorf("finalSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
