package day17

import "fmt"

type xy struct {
	x int
	y int
}

type Probe struct {
	pos xy
	vel xy
}

type Target struct {
	min xy
	max xy
}

func (t *Target) isAbove(p xy) bool {
	return p.y > t.min.y
}

func (t *Target) isShortOf(p xy) bool {
	return p.x < t.min.x
}

func (t *Target) isWithin(p xy) bool {
	return p.x >= t.min.x && p.x <= t.max.x && p.y >= t.min.y && p.y <= t.max.y
}

func (t *Target) isBeyond(p xy) bool {
	return p.x > t.max.x || p.y < t.min.y
}

func (t *Target) isPassedThroug(p xy) bool {
	return (p.x > t.max.x && p.y > t.min.y) || (p.y < t.min.y && p.x > t.min.x)
}

func GetHighestY(trgt string) int {
	var maxY int
	t := loadTarget(trgt)

	dy := t.min.y*-1 - 1
	maxY = dy * (dy+1) / 2

	return maxY
}

func GetNumOfDistinctV(trgt string) int {

	var valids int
	t := loadTarget(trgt)
	p := Probe{}
	for p.vel.x = 0; p.vel.x < 200; p.vel.x++ {
		for p.vel.y = -300; p.vel.y < 300; p.vel.y++ {
			if _,end := shoot(p,t); t.isWithin(end) {
				valids += 1
			}

		}
	}
	return valids
}

func shoot(p Probe, t Target) (int,xy) {
	maxY := p.pos.y

	for !t.isWithin(p.pos) {
		if t.isBeyond(p.pos) {
			return maxY, p.pos
		} else {
			p.pos, p.vel = calculate(p.pos, p.vel)
			if maxY < p.pos.y { 
				maxY = p.pos.y
			} 
		}
	}
	return maxY,p.pos
}

func loadTarget(str string) Target {
	t := Target{}
	fmt.Sscanf(str, "target area: x=%d..%d, y=%d..%d", &(t.min.x), &(t.max.x), &(t.min.y), &(t.max.y))
	return t
}


func calculate(p xy, v xy) (xy, xy) {
	p.x += v.x
	p.y += v.y
	if v.x > 0 {
		v.x -= 1
	}
	if v.x < 0 {
		v.x += 1
	}
	v.y -= 1

	return p, v
}
