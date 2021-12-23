package day22

import (
	"fmt"
	"sort"
	"strings"
)

type xyz struct {
	x int
	y int
	z int
}
type Cube struct {
	pos   xyz
	state bool
}

type Range struct {
	from int
	to int
}

type RangeList []Range

type CubeList map[xyz]Cube

type Cuboid struct {
	x     []Range
	y     []Range
	z     []Range
	state bool
}
func (a RangeList) Len() int 			{ return len(a) }
func (a RangeList) Swap(i, j int) 		{ a[i], a[j] = a[j], a[i] }
func (a RangeList) Less(i, j int) bool 	{ return a[i].from < a[j].from } 

func merge(rlis1,rlist2 RangeList) RangeList {
	result := RangeList{rlis1[0]}
	rlis1 = append(rlis1,rlist2...)
	sort.Sort(RangeList(rlis1))
	for _,r1 := range rlis1 {
		result = mergeRange(result[len(result)-1],r1)
	}
	return result
}

func remove(keep, remove RangeList) RangeList {
	updated := RangeList{}
	sort.Sort(keep)
	for _,r1 := range keep {
		updated = append(updated,removeRange(r1, remove[0])...)
	}
	return updated
}

func mergeRange(r1, r2 Range) RangeList {
	if r1 == r2 { return RangeList{r1} }
	if (r1.from - r2.to) > 1 || (r2.from - r1.to) > 1 {	// Disjoint ranges
		if r1.from < r2.from {
			return RangeList{r1,r2}
		} else {
			return RangeList{r2,r1}
		}
	} else if r1.from >= r2.from && r1.to <= r2.to {	
		return RangeList{r2}
	} else if r2.from >= r1.from && r2.to <= r1.to {	
		return RangeList{r1}
	} else {
		return RangeList{{from:min(r1.from, r2.from), to:max(r1.to, r2.to)}}
	}
}

func removeRange(keep,remove Range) RangeList {
	if keep == remove { return RangeList{} }
	if keep.from > remove.to || keep.to < remove.from { return RangeList{keep} }
	if remove.from <= keep.from && keep.to <= remove.to { return RangeList{}}
	if remove.from <= keep.from { return RangeList{{remove.to+1, keep.to}}}
	if keep.to <= remove.to { return RangeList{{keep.from, remove.from-1}} }
	return RangeList{{from:keep.from, to:remove.from-1}, {from:remove.to+1, to:keep.to}}
}

func CountOn(str []string) int64 {
	steps := loadSteps(str, xyz{-50,-50,-50}, xyz{50,50,50})
	// cubes := CubeList{}
	var lit int64

	result := steps[0]

	for _, step := range steps {
		result = resolve(result, step)
		// changed = cubes.apply(step)
		// lit = result.on(xyz{-50,-50,-50}, xyz{50,50,50})
		lit = result.on()
	}
	_ = steps
	_ = lit
	return result.on()
}

func resolve(cb, step Cuboid) Cuboid {
	if step.state {
		cb.x = merge(cb.x, step.x)
		cb.y = merge(cb.y, step.y)
		cb.z = merge(cb.z, step.z)
	} else {
		cb.x = remove(cb.x, step.x)
		cb.y = remove(cb.y, step.y)
		cb.z = remove(cb.z, step.z)

	}
	return cb
}

func toRange(tl []Range) []int {
	list := []int{}
	for _, r := range tl {
		list = append(list,makeRange(fmt.Sprintf("%d..%d",r.from,r.to), r.from, r.to)...)

	}
	return list
}

func (cbs *CubeList) apply(step Cuboid) int {
	var changed int
	for _,x := range toRange(step.x) {
		for _,y := range toRange(step.y) {
			for _,z := range toRange(step.z) {
				cb,found := (*cbs)[xyz{x,y,z}]
				if !found {
					(*cbs)[xyz{x,y,z}] = Cube{pos:xyz{x,y,z}, state:step.state}
					changed ++
				} else if cb.state != step.state {
					cb.state = step.state
					(*cbs)[xyz{x,y,z}] = cb
					changed ++
				}
			}
		}
	}
	return changed
}

func (cb Cuboid) on() int64 { 
	var countx, county, countz int
	for _,i := range cb.x { 
		countx = i.to-i.from+1
	}
	for _,i := range cb.y { 
		county += i.to-i.from+1
	}
	for _,i := range cb.x { 
		countz += i.to-i.from+1
	}
	return int64(countx)*int64(county)*int64(countz)
}

func loadSteps(str []string, min, max xyz) []Cuboid {

	cubeoids := make([]Cuboid, 0)
	for _, s := range str {
		var state, xrange, yrange, zrange string
		// "on x=10..12,y=10..12,z=10..12"
		parts := strings.Split(strings.ReplaceAll(s,",", " "), " ")
		state = parts[0]
		fmt.Sscanf(parts[1], "x=%s", &xrange)
		fmt.Sscanf(parts[2], "y=%s", &yrange)
		fmt.Sscanf(parts[3], "z=%s", &zrange)
		cubeoids = append(cubeoids, Cuboid{
			x:     parseRange(xrange),
			y:     parseRange(yrange),
			z:     parseRange(zrange),
			state: state == "on",
		})
	}
	return cubeoids
}

func parseRange(s string) []Range {
	var from,to int
	fmt.Sscanf(s, "%d..%d", &from, &to)
	return []Range{Range{from: from, to: to}}
}

func makeRange(minmax string, from, to int) []int {
	var min, max int
	_,err := fmt.Sscanf(minmax, "%d..%d", &min, &max)
	if err != nil {
		panic(err)
	}
	if min > to { return []int{}}
	if max < from { return []int{}}
	if min < from {min = from}
	if max > to {max = to}
	a := make([]int, max-min+1)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func abs(val int) int {
	if val < 0 {
		return -val
	}
	return val
}

func min(x,y int) int {
	if x < y  { return x }
	return y
}

func max(x,y int) int {
	if x > y { return x }
	return y
}
