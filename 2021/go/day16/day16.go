package day16

import (
	"fmt"
	"strconv"
)

type Package struct {
	ver int
	typ int
	val int
	// pld string
}
var LITERAL = 4

func pkgDecode(s string) []Package {
	pkgs := make([]Package,0)
	pkg, pld := decode(s)
	pkgs = append(pkgs, pkg)
	for pkg.typ != LITERAL {
		ltId := getBits(pld, 0, 1)
		switch ltId {
		case 0:	// length is a 15-bit number representing the number of bits in the sub-packets
			pkgLen := getBits(pld,1,15)
			pld = pld[15+1:]
			for len(pld) > 0 {
				pkg, pld = decode(pld[:pkgLen])
				pkgs = append(pkgs, pkg)
			}

		case 1: // length is a 11-bit number representing the number of sub-packets
			pkgCount := getBits(pld, 1, 11)
			pld = pld[11+1:]
			for i := 0; i < pkgCount; i++ {
				pkg, pld = decode(pld)
				pkgs = append(pkgs, pkg)
			}
		}
	} 
	return pkgs
}

func decode(pkg string) (Package,string) {

	p := Package{}
	var payload string

	bits := toBits(pkg)
	p.ver = getBits(bits, 0,3)
	p.typ = getBits(bits, 3,3)
	payload = bits[6:]

	if p.typ == LITERAL {
		p.val = parseLiteral(payload)
		payload = ""
	}
	return p, payload
}

func toBits(s string) string {
	var value int
	var first int

	fmt.Sscanf(s, "%X", &value)
	r := fmt.Sprintf("%b", value)
	// Pad the bitstring
	fmt.Sscanf(s[:1], "%X", &first)
	if first < 8 { r = "0"+r}
	if first < 4 { r = "0"+r}
	if first < 2 { r = "0"+r}

	return r
}

func getBits(bits string, index,length int) int {

	var val int
	var trash string
	format := "%"+strconv.Itoa(length)+"b"
	if index > 0 {
		format = "%"+strconv.Itoa(index)+"s" + format
		fmt.Sscanf(bits, format, &trash, &val)
	} else {
		fmt.Sscanf(bits, format, &val)
	}
	return val
}

func parseLiteral(s string) int {
	var val string
	var literal int
	for len(s) > 0 {
		var end int
		var bits string
		fmt.Sscanf(s[:5], "%1b%s", &end, &bits)
		val = val + bits
		if end == 0 {
			fmt.Sscanf(val, "%b", &literal)
			return literal
		}
		s = s[5:]
	}
	return literal
}