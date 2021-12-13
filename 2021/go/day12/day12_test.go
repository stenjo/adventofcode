package day12

import (
	"reflect"
	"testing"
)

func TestParseNodes(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name  string
		args  args
		want  []Node
		want1 *Node
	}{
		// TODO: Add test cases.
		// {"1", args{str: []string{"start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"}},
		// 	[]Node{{"start", []*Node{}}, {"A", []*Node{}}, {"b", []*Node{}}, {"c", []*Node{}}, {"d", []*Node{}}, {"end", []*Node{}}},
		// 	&Node{"start", []*Node{}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := ParseNodes(tt.args.str)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ParseNodes() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("ParseNodes() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestGetPaths(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{"start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"}}, 10},
		{"2", args{str: []string{"dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"}}, 19},
		{"3", args{str: []string{"fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he", "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"}}, 226},
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPaths(tt.args.str); got != tt.want {
				t.Errorf("GetPaths() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_AsString(t *testing.T) {
	tests := []struct {
		name string
		list *NodeList
		want string
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.list.AsString(); got != tt.want {
				t.Errorf("NodeList.AsString() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_Update(t *testing.T) {
	type args struct {
		node *Node
	}
	tests := []struct {
		name  string
		nodes *NodeList
		args  args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.nodes.Update(tt.args.node)
		})
	}
}

func TestNodeList_Add(t *testing.T) {
	type args struct {
		n Node
	}
	tests := []struct {
		name string
		list *NodeList
		args args
		want *Node
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.list.Add(tt.args.n); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("NodeList.Add() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_Find(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name  string
		list  *NodeList
		args  args
		want  *Node
		want1 bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := tt.list.Find(tt.args.s)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("NodeList.Find() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("NodeList.Find() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestNode_AddLink(t *testing.T) {
	type args struct {
		l *Node
	}
	tests := []struct {
		name string
		n    *Node
		args args
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.n.AddLink(tt.args.l)
		})
	}
}

func TestNode_HasLink(t *testing.T) {
	type args struct {
		l *Node
	}
	tests := []struct {
		name string
		n    *Node
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.n.HasLink(tt.args.l); got != tt.want {
				t.Errorf("Node.HasLink() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetPathsPart2(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{"1", args{str: []string{"start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end"}}, 36},
		// {"2", args{str: []string{"dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc"}}, 103},
		// {"3", args{str: []string{"fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he", "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"}}, 3509},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := GetPathsPart2(tt.args.str); got != tt.want {
				t.Errorf("GetPathsPart2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_Once(t *testing.T) {
	type args struct {
		node *Node
	}
	tests := []struct {
		name string
		list *NodeList
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.list.Once(tt.args.node); got != tt.want {
				t.Errorf("NodeList.Once() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_Has(t *testing.T) {
	type args struct {
		node *Node
	}
	tests := []struct {
		name string
		list *NodeList
		args args
		want bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.list.Has(tt.args.node); got != tt.want {
				t.Errorf("NodeList.Has() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestNodeList_Pop(t *testing.T) {
	tests := []struct {
		name string
		list *NodeList
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.list.Pop()
		})
	}
}
