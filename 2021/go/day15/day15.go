package day15

import (
	"container/heap"
	"strconv"
)

type xy struct {
	x int
	y int
}

type Node struct {
	pos xy
	priority uint64
	// The index is needed by update and is maintained by the heap.Interface methods.
	index int // The index of the item in the heap.
}

func GetLowestRiskPath(str []string) uint64 {
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
				riskLevel := node.priority + uint64(area[nb])
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

	return distance[xy{int(maxX), int(maxY)}]
}

func GetLowestRiskPathExtended(str []string) uint64 {
	area, maxX, maxY := parseInput(str)
	// area.print(maxX+1, maxY+1)
	area = area.expand(maxX+1, maxY+1)
	maxX = ((maxX + 1) * 5) - 1 
	maxY = ((maxY + 1) * 5) - 1
	// area.print(maxX+1, maxY+1)
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

	return distance[xy{int(maxX), int(maxY)}]

}


func limRisk(v int) int {
	return (v-1) % 9 + 1
}
func modRem(x,y int) (int, int) {
	return x / y, x % y
}

//67554889357866599146897761125791887223681299833479
func parseInput(str []string) (Grid, uint64, uint64) {
	area := make(Grid)
	maxX, maxY := 0, 0
	for y := 0; y < len(str); y++ {
		for x := 0; x < len(str[y]); x++ {
			area[xy{x,y}] = atoi(str[y][x])
			maxX = max(maxX, x)
			maxY = max(maxY, y)
		}
	}
	return area, uint64(maxX), uint64(maxY)
}

func max(x,y int) int {
	if x > y { return x }
	return y
}

func atoi(a byte) uint64 {
	i, err := strconv.ParseInt(string(a), 10, 64)
	if err != nil {
		panic(err)
	}
	return uint64(i)
}

