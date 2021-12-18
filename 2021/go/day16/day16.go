package day16

import (
	"fmt"
)

type Package struct {
	ver int
	typ int
	val int
	pckgs []Package
	// pld string
}
var LITERAL = 4


func GetVersionsSum(s string) int {
	pkgs,_ := pkgDecode(toBits(s))
	var sum int
	for _,p := range pkgs {
		sum += p.ver
	}
	return sum
}

func pkgDecode(bits Bits) ([]Package,Bits) {
	pkgs := make([]Package,0)
	pkg,tail := decode(bits)
	pkgs = append(pkgs, pkg)
	// return pkgs, payload
	return pkgs, tail
}

// Unwrap package and return remaining if all not used
// func unpack(bits Bits) (Package, Bits) {
// 	var payload Bits
// 	p := Package{}

// 	if len(bits) < 11 { return p, payload }

// 	p.ver = getBits(bits, 0,3)
// 	p.typ = getBits(bits, 3,3)
// 	payload = bits[6:]

// 	if p.typ == LITERAL {
// 		p.val,payload = literals(payload)
// 	}
// 	return p, payload
// }

func decode(bits Bits) (Package,Bits) {

	p := Package{ver:bits.getBits(0,3),typ:bits.getBits(3,3)}
	tail := Bits(string(bits)[6:])

	if p.typ == LITERAL {
		tail = p.parseLiteral(tail)
	} else {
		tail = p.parseOperator(tail)
	}

	return p, tail
}

func (p *Package)parseOperator(b Bits) Bits {
	lenTypeId := b.getBits(0, 1)
	// var subpkgs []Package
	var tail Bits
	switch lenTypeId {
	case 0:	// length is a 15-bit number representing the number of bits in the sub-packets
		pkgLen := b.getBits(1,15)
		_,tail = b.splitAt(16)
		tail = (*p).parseOperatorBits(pkgLen,tail)

	case 1: // length is a 11-bit number representing the number of sub-packets
		pkgCount := b.getBits(1, 11)
		_,tail = b.splitAt(12)
		tail = (*p).parseOperatorCount(pkgCount,tail)
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
	var tail Bits
	for i := 0; i < count && !tail.isAllZeros(); i++ {
		newPckg, tail = decode(tail)
		(*p).pckgs = append((*p).pckgs, newPckg)
	} 
	return tail
}

func (p *Package)parseLiteral(b Bits) Bits {
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
			return Bits(string(b)[:5])
		}
		b = Bits(string(b)[5:])
	}
	panic("Mismatch on literal decode")
}