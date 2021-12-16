package day15

import (
	"container/heap"
	"math"
	"strconv"
)

type xy struct {
	x int
	y int
}

type Node struct {
	pos xy
	priority int
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}
type Grid map[xy]int

func GetLowestRiskPath(str []string) int {
	area, maxX, maxY := parseInput(str)
	distance := make(Grid)
	visited := make(Grid)

	unvisited := make(PriorityQueue,0)
	heap.Init(&unvisited)
	
	n := xy{0,0}
	area[n] = 0	// Start with 0 risk
	heap.Push(&unvisited, &Node{pos:n, priority:0})
	distance[n] = 0
	for unvisited.Len() > 0 {
		node := heap.Pop(&unvisited).(*Node)
		n = node.pos
		neighbours := []xy{{n.x-1, n.y},{n.x, n.y-1}, {n.x+1, n.y}, {n.x, n.y+1}}
		for _,nb := range neighbours {
			if area.has(nb) {
				riskLevel := node.priority + area[nb]
				if !distance.has(nb) {
					distance[nb] = riskLevel
				} else if distance[nb] > riskLevel {
					distance[nb] = riskLevel
				}
				if !visited.has(nb) {
					heap.Push(&unvisited, &Node{pos:nb, priority:riskLevel})
				}
			}
		}
		visited[n] = 1
	}

	return distance[xy{maxX, maxY}]
}

func GetLowestRiskPathExtended(str []string) int {
	area, maxX, maxY := parseInput(str)
	distance := make(Grid)
	visited := make(Grid)

	unvisited := make(PriorityQueue,0)
	heap.Init(&unvisited)
	
	n := xy{0,0}
	e := xy{maxX,maxY}
	// area[n] = 0	// Start with 0 risk
	heap.Push(&unvisited, &Node{pos:n, priority:0})
	distance[n] = 0
	for unvisited.Len() > 0 {
		node := heap.Pop(&unvisited).(*Node)
		n = node.pos
		neighbours := []xy{{n.x-1, n.y},{n.x, n.y-1}, {n.x+1, n.y}, {n.x, n.y+1}}
		for _,nb := range neighbours {
			if risk, ok := area.hasExtended(nb, maxX, maxY); ok {
				riskLevel := node.priority + risk
				if !distance.has(nb) {	// if not yet visited
					distance[nb] = riskLevel
					if e.x < nb.x { e.x = nb.x }
					if e.y < nb.y { e.y = nb.y }
				} else if distance[nb] > riskLevel {
					distance[nb] = riskLevel
				}
				if !visited.has(nb) {	// if not yet visited
					heap.Push(&unvisited, &Node{pos:nb, priority:riskLevel})
				}
			}
		}
		visited[n] = 1
	}

	return distance[e]
}

func (a Grid) has(n xy) bool {
	_,found := a[n]
	return found
}

func (a Grid) hasExtended(n xy, maxX, maxY int) (int,bool) {
	dx,x := modRem(n.x, maxX+1)
	dy,y := modRem(n.y, maxY+1)
	if dx >= 5 || dy >= 5 { return math.MaxInt, false }
	v,found := a[xy{x,y}]
	v = limRisk(v + (dx + dy))
	return v,found
}

func limRisk(v int) int {
	return (v-1) % 9 + 1
}
func modRem(x,y int) (int, int) {
	return x / y, x % y
}

//67554889357866599146897761125791887223681299833479
func parseInput(str []string) (Grid, int, int) {
	area := make(Grid)
	maxX, maxY := 0, 0
	for y := 0; y < len(str); y++ {
		for x := 0; x < len(str[y]); x++ {
			area[xy{x,y}] = atoi(str[y][x])
			maxX = max(maxX, x)
			maxY = max(maxY, y)
		}
	}
	return area, maxX, maxY
}

func max(x,y int) int {
	if x > y { return x }
	return y
}

func atoi(a byte) int {
	i, err := strconv.Atoi(string(a))
	if err != nil {
		panic(err)
	}
	return i
}

// A PriorityQueue implements heap.Interface and holds Items.
type PriorityQueue []*Node

func (pq PriorityQueue) Len() int { return len(pq) }

func (pq PriorityQueue) Less(i, j int) bool {
	// We want Pop to give us the lowest, not highest, priority so we use less than here.
	return pq[i].priority < pq[j].priority
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Node)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

// update modifies the priority and value of an Item in the queue.
func (pq *PriorityQueue) update(item *Node, value xy, priority int) {
	item.pos = value
	item.priority = priority
	heap.Fix(pq, item.index)
}
