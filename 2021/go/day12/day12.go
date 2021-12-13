package day12

import (
	"fmt"
	"strings"
)

type Node struct {
	Name  string
	Links []*Node
}

type NodeList []Node

func GetPaths(str []string) int {
	var paths []string
	nodes, start := ParseNodes(str)
	for _,node := range start.Links {
		var nodePath NodeList
		nodePath.Add((*start))
		nodes.FindEnd(node, &nodePath, &paths, false)

	}
	return len(paths)
}

func GetPathsPart2(str []string) int {
	var paths []string
	nodes, start := ParseNodes(str)
	for _,node := range start.Links {
		var nodePath NodeList
		nodePath.Add((*start))
		nodes.FindEnd(node, &nodePath, &paths, true)

	}
	for _,s := range paths {
		fmt.Println(s)
	}
	return len(paths)
}

func (list *NodeList) AsString() string {

	var s string
	for i, n := range (*list) {
		if i == 0 {
			s = n.Name
		} else {
			s = s + "," + n.Name
		}
	}
	return s
}
func (list *NodeList) Once(node *Node) bool {
	var count int
	for _, n := range (*list) {
		if n.Name == node.Name {
			count++
		}
	}
	return count <= 1
}

func (list *NodeList) Has(node *Node) bool {
	for _, n := range (*list) {
		if n.Name == node.Name {
			return true
		}
	}
	return false
}
func (list *NodeList) FindEnd(n *Node, path *NodeList, str *[]string, extended bool) bool {
	node, _ := list.Find(n.Name)
	if node.Name == "start" {
		return false
	} else if node.Name == "end" {
		path.Add((*node))
		*str = append(*str, path.AsString())
		path.Pop()
		return true
	} else if path.AllowedVisit(node, extended){
		path.Add((*node))
		for _,p := range node.Links {
			list.FindEnd(p, path, str, extended)
		}
		path.Pop()
	}
	return false
}

func ParseNodes(str []string) (NodeList, *Node) {
	nodes := make(NodeList, 0)

	for _, l := range str {
		parts := strings.Split(l, "-")
		left, ok := nodes.Find(parts[0])
		if !ok {
			left = nodes.Add(Node{parts[0], nil})
		}
		right,ok := nodes.Find(parts[1])
		if !ok {
			right = nodes.Add(Node{parts[1], nil})
		}

		if !left.HasLink(right) {
			left.AddLink(right)
			nodes.Update(left)
		}
		if !right.HasLink(left) {
			right.AddLink(left)
			nodes.Update(right)
		}

	}
	start,_ := nodes.Find("start")
	return nodes, start
}

func (nodes *NodeList) AllowedVisit(node *Node, ext bool) bool {

	if !ext {
		if !node.IsLarge() && !nodes.Has(node) {
			return true
		} else if node.IsLarge() {
			return true
		}
	} else {
		// second := nodes.SecondLast()
		last := nodes.Last()
		if !node.IsLarge() {
			if last == nil { return true }
			if !last.IsLarge() && !nodes.Has(node) {
				return true
			} else if last.IsLarge() && nodes.Count(node) < 2 {
				return true
			}
			return false
		} else {
			return true
		}
	}
	return false
}

func (list *NodeList) SecondLast() *Node {
	if len(*list) > 1 {
		return &(*list)[len(*list)-2]
	}
	return nil
}
func (list *NodeList) Last() *Node {
	if len(*list) > 0 {
		return &(*list)[len(*list)-1]
	}
	return nil
}
func (list *NodeList) Count(node *Node) int {
	var count int
	for _, n := range (*list) {
		if n.Name == node.Name {
			count++
		}
	}
	return count
}

func (nodes *NodeList) Update(node *Node) {
	for i,n := range (*nodes) {
		if n.Name == node.Name {
			(*nodes)[i] = (*node)
			break
		}
	}
}

func (list *NodeList) Add(n Node) *Node {
	if n.Links == nil {
		n.Links = make([]*Node, 0)
	}
	*list = append(*list, n)
	node,_ := list.Find(n.Name)
	return node
}

func (list *NodeList) Pop() {
	if len(*list) > 0 {
		index := len(*list) - 1 // Get the index of the top most element.
		*list = (*list)[:index] // Remove it from the stack by slicing it off.
	}
}

func (list *NodeList) Find(s string) (*Node,bool) {
	for i := 0; i < len(*list); i++ {
		if  strings.HasPrefix((*list)[i].Name,s) {
			return &((*list)[i]), true
		}
	}
	return nil, false
}
func (n *Node) IsLarge() bool {
	if n == nil { return false}
	return n.Name != strings.ToLower(n.Name)
}

func (n *Node) AddLink(l *Node) *Node {
	
	(*n).Links = append((*n).Links, l)
	return n
}

func (n *Node) HasLink(l *Node) bool {

	if len(n.Links) == 0 {
		return false
	}
	for _, lnk := range n.Links {
		if lnk.Name == l.Name {
			return true
		}
	}
	return false
}