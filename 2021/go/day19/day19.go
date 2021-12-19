// Ripped off https://github.com/seihoukei/aoc_bp/blob/seihoukei_2021/data/2021/19/solver.js
// - but sadly does not work yet

package day19

import (
	"fmt"
)

type xyz struct {
	x int
	y int
	z int
}

func (p *xyz) parse(s string) {
	fmt.Sscanf(s, "%d,%d,%d", &(*p).x, &(*p).y, &(*p).z)
}

func CountBeacons(s []string) int {
	scanners := ScannerList{}
	scanners.loadScanners(s)
	scanners.align()
	beacons := map[string]int{}
	for _, scnr := range scanners {
		for _,sig := range scnr.signals {
			beacons[sig.toString()] += 1
		}
	}

	return len(beacons)
}

type locked map[int]bool
func (l locked) has(x int) bool {
	_,found := l[x]
	return found
}

func (sl *ScannerList) align() {
	locked := locked{0:true}
	for len(locked) < len(*sl) {
		for i := 0; i < len(*sl); i++ {
			for j := 0; j < len(*sl); j++ {
				if i == j || !locked.has(i) || locked.has(j) {
					continue
				}
				intersection, ok := (*sl)[i].compare((*sl)[j])
				if !ok {
					continue
				}
				(*sl)[i].align(&((*sl)[j]), intersection)
				locked[j] = true
			}
		}
	}
}