package day19

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

type Signal struct {
	id        int
	pos       xyz
	relatives Relatives
}

type Relatives map[int]string

type RelativeItem struct {
	rel string
	this int
	index int
}
func (sig Signal) toString() string {
	s := []string{
		strconv.Itoa(sig.pos.x),
		strconv.Itoa(sig.pos.y),
		strconv.Itoa(sig.pos.z),
	}
	return strings.Join(s, ",")
}

func (this *Signal) align(other *Signal) {
	// b.relatives = make(Relatives, 0)
	dx := abs(this.pos.x - other.pos.x)
	dy := abs(this.pos.y - other.pos.y)
	dz := abs(this.pos.z - other.pos.z)

	relative := strings.Join([]string{
		hypot(dx, dy, dz),
		fmt.Sprint(min(dx,dy,dz)),
		fmt.Sprint(max(dx,dy,dz))}, ",")

	this.addRelative(relative, other.id)
	other.addRelative(relative, this.id)
	// b.relatives[s.id] = relative
	// s.relatives[b.id] = relative
}

func (b *Signal) addRelative(re string, ind int) {
	(*b).relatives[ind] = re
}

func (b *Signal) compare(a *Signal) []RelativeItem {
	result := make([]RelativeItem,0)

	for _,relative := range (*b).relatives {
		i := (*a).relatives.indexOf(relative)
		if i > -1 {
			result = append(result,RelativeItem{
				a.relatives[i],
				b.relatives.indexOf(relative),
				i})
		}
	}

	return result
}

func (r Relatives) indexOf(s string) int {
	for i,n := range r {
		if s == n {
			return i
		}
	}
	return -1
}

func abs(val int) int {
	if val < 0 {
		return -val
	}
	return val
}

func min(x,y,z int) int {
	if x < y  && x < z { return x }
	if y < z && y < x { return y }
	return z
}

func max(x,y,z int) int {
	if x > y && x > z { return x }
	if y > z && y > x { return y }
	return z
}

func hypot(x,y,z int) string {
	a := math.Hypot(float64(x),float64(y))
	b := math.Hypot(a,float64(z))
	return fmt.Sprintf("%.5f",b)
}