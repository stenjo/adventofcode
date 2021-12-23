package day16

import (
	"fmt"
	"math"
)

type Package struct {
	ver   int
	typ   int
	val   int
	pckgs []Package
	// pld string
}

var LITERAL = 4

func (p Package) sumVer() int {
	sum := p.ver
	for _, sp := range p.pckgs {
		sum += sp.sumVer()
	}
	return sum
}

func (p *Package) parseOperator(b Bits) Bits {
	lenTypeId := b.getBits(0, 1)
	var tail Bits
	switch lenTypeId {
	case 0: // length is a 15-bit number representing the number of bits in the sub-packets
		pkgLen := b.getBits(1, 15)
		_, tail = b.splitAt(16)
		tail = (*p).parseOperatorBits(pkgLen, tail)

	case 1: // length is a 11-bit number representing the number of sub-packets
		pkgCount := b.getBits(1, 11)
		_, tail = b.splitAt(12)
		tail = (*p).parseOperatorCount(pkgCount, tail)
	}

	return tail
}

func (p *Package) parseOperatorBits(len int, b Bits) Bits {

	var newPckg Package
	pkgBits, tail := b.splitAt(len)
	for !pkgBits.isAllZeros() {
		newPckg, pkgBits = decode(pkgBits)
		(*p).pckgs = append((*p).pckgs, newPckg)
	}
	return tail
}

func (p *Package) parseOperatorCount(count int, b Bits) Bits {

	var newPckg Package
	tail := b
	for i := 0; i < count && !tail.isAllZeros(); i++ {
		newPckg, tail = decode(tail)
		(*p).pckgs = append((*p).pckgs, newPckg)
	}
	return tail
}

func (p *Package) parseLiteral(b Bits) Bits {
	var val string
	var literal int
	for len(b) > 0 {
		var end int
		var bits string
		fmt.Sscanf(string(b)[:5], "%1b%s", &end, &bits)
		val = val + bits
		if end == 0 {
			fmt.Sscanf(val, "%b", &literal)
			(*p).val = literal
			return Bits(string(b)[5:])
		}
		b = Bits(string(b)[5:])
	}
	panic("Mismatch on literal decode")
}

func (p Package) sumVal() int { 
	var val int
	for _, sp := range p.pckgs {
		val += sp.val
	}
	return val
}

func (p Package) productVal() int { 
	val := 1
	for _, sp := range p.pckgs {
		val *= sp.val
	}
	return val
}

func (p Package) minVal() int { 
	val := math.MaxInt
	for _, sp := range p.pckgs {
		if sp.val < val {
			val = sp.val
		}
	}
	return val
}

func (p Package) maxVal() int { 
	val := 0
	for _, sp := range p.pckgs {
		if sp.val > val {
			val = sp.val
		}
	}
	return val
}

func (p Package) gtVal() int { 
	if p.pckgs[0].val > p.pckgs[1].val {
		return 1
	}
	return 0
}

func (p Package) ltVal() int { 
	if p.pckgs[0].val < p.pckgs[1].val {
		return 1
	}
	return 0
}

func (p Package) eqVal() int { 
	if p.pckgs[0].val == p.pckgs[1].val {
		return 1
	}
	return 0
}
