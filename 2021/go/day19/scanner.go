package day19

import (
	"fmt"
	"strings"
)

type Scanner struct {
	id      int
	pos     xyz
	signals []*Signal
}

type ScannerList []Scanner

type Intersect struct {
	here * Signal
	there * Signal
	rel []RelativeItem
}

func (s *Scanner) addSignal(pos xyz) {
	signl := Signal{pos:pos, id: len((*s).signals), relatives:Relatives{}}
	for _,b := range (*s).signals {
		b.align(&signl)
	}
	(*s).signals = append(s.signals,&signl)
}

func (sl *ScannerList) loadScanners(str []string) int {
	var scanner Scanner
	for i, s := range str {
		if strings.HasPrefix(s, "--- scanner") {
			var id int
			fmt.Sscanf(s, "--- scanner %d ---", &id)
			scanner = Scanner{id: id, pos: xyz{}, signals: []*Signal{}}
		} else if s != "" {
			pos := xyz{}
			pos.parse(s)
			scanner.addSignal(pos)
		}

		if s == "" || len(str)-1 == i {
			(*sl) = append((*sl), scanner)
		}
	}
	return len(*sl)
}

func (s1 Scanner) compare(s2 Scanner) (Intersect, bool) {
	for _,b2 := range s2.signals {
		for _,b1 := range s1.signals {
			intersection := b2.compare(b1)
			if len(intersection) >= 11 {
				return Intersect{b2,b1,intersection}, true
			}
		}
	}
	return Intersect{}, false
}

func (s1 *Scanner) align(s2 *Scanner, data Intersect) {

	for _,line := range data.rel {
		if strings.Split(line.rel,",")[1] == "0" {
			continue
		}
		relativeHere := s1.signals[line.index]
		dx0 := data.here.pos.x - relativeHere.pos.x
		dy0 := data.here.pos.y - relativeHere.pos.y
		dz0 := data.here.pos.z - relativeHere.pos.z

		relativeThere := s2.signals[line.this]
		dx1 := data.there.pos.x - relativeThere.pos.x
		dy1 := data.there.pos.y - relativeThere.pos.y
		dz1 := data.there.pos.z - relativeThere.pos.z

		if abs(dx0) == abs(dy0) || abs(dz0) == abs(dy0) || abs(dx0) == abs(dz0) {
			continue
		}

		rotation := []int{0,0,0,0,0,0,0,0,0,}
		
		if dx0 == dx1 	{ rotation[0] = 1}
		if dx0 == -dx1 	{ rotation[0] = -1}
		if dx0 == dy1 	{ rotation[3] = 1}
		if dx0 == -dy1 	{ rotation[3] = -1}
		if dx0 == dz1 	{ rotation[6] = 1}
		if dx0 == -dz1 	{ rotation[6] = -1}
		if dy0 == dx1 	{ rotation[1] = 1}
		if dy0 == -dx1 	{ rotation[1] = -1}
		if dy0 == dy1 	{ rotation[4] = 1}
		if dy0 == -dy1 	{ rotation[4] = -1}
		if dy0 == dz1 	{ rotation[7] = 1}
		if dy0 == -dz1 	{ rotation[7] = -1}
		if dz0 == dx1 	{ rotation[2] = 1}
		if dz0 == -dx1 	{ rotation[2] = -1}
		if dz0 == dy1 	{ rotation[5] = 1}
		if dz0 == -dy1 	{ rotation[5] = -1}
		if dz0 == dz1 	{ rotation[8] = 1}
		if dz0 == -dz1 	{ rotation[8] = -1}

		for _,b := range s2.signals {
			old := b.pos
			b.pos.x = old.x*rotation[0] + old.y*rotation[3] + old.z*rotation[6]
			b.pos.x = old.x*rotation[1] + old.y*rotation[4] + old.z*rotation[7]
			b.pos.x = old.x*rotation[2] + old.y*rotation[5] + old.z*rotation[8]
		}

		s2.pos = xyz{data.here.pos.x, data.here.pos.y, data.here.pos.z}

		for _,b := range s2.signals {
			b.pos.x += s2.pos.x
			b.pos.y += s2.pos.y
			b.pos.z += s2.pos.z
		}
		break
	}
}

// func atoi(s string) int {
// 	i,_ := strconv.Atoi(s)
// 	return i
// }