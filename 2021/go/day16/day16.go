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

func GetVersionsSum(s string) int {
	pkgs,_ := pkgDecode(toBits(s))
	var sum int
	for _,p := range pkgs {
		sum += p.ver
	}
	return sum
}

func pkgDecode(bits string) ([]Package,string) {
	pkgs := make([]Package,0)
	pkg,rem := unpack(bits)
	if pkg.typ != 0 {
		pkgs = append(pkgs, pkg)
	}
	if pkg.typ == LITERAL {
		return pkgs, rem
	} else {
		ltId := getBits(rem, 0, 1)
		var subpkgs []Package
		switch ltId {
		case 0:	// length is a 15-bit number representing the number of bits in the sub-packets
			pkgLen := getBits(rem,1,15)
			pld := (rem[15+1:])[:pkgLen]
			for len(pld) > 0 {
				subpkgs, pld = pkgDecode(pld)
				pkgs = append(pkgs, subpkgs...)
			}
			return pkgs, (rem[15+1:])[pkgLen:]

		case 1: // length is a 11-bit number representing the number of sub-packets
			pkgCount := getBits(rem, 1, 11)
			pld := rem[11+1:]
			for i := 0; i < pkgCount; i++ {
				subpkgs, pld = pkgDecode(pld)
				pkgs = append(pkgs, subpkgs...)
			}
			return pkgs, pld
		}
	}
	// return pkgs, payload
	return pkgs, ""
}

// Unwrap package and return remaining if all not used
func unpack(pkg string) (Package, string) {
	var payload string
	p := Package{}

	bits := pkg

	if len(bits) < 11 { return p, payload }

	p.ver = getBits(bits, 0,3)
	p.typ = getBits(bits, 3,3)
	payload = bits[6:]

	if p.typ == LITERAL {
		p.val,payload = literals(payload)
	}
	return p, payload
}

func toHex(bits string) string {
	var val int
	var hex string

	pad := (4 - (len(bits) % 4)) % 4
	bits = bits + "00000"[:pad]

	for len(bits) > 0 {
		chunk := ""
		if len(bits) < 4 {
			chunk = bits
			bits = ""
		} else {
			chunk = bits[:4]
			bits = bits[4:]
		}
		fmt.Sscanf(chunk, "%b", &val)
		hex = hex + fmt.Sprintf("%X", val)
	}
	return hex
}

func toBits(hex string) string {
	var value int
	var first int
	var bits string

	for len(hex) > 0 {
		chunk := ""
		if len(hex) < 8 {
			chunk = hex
			hex = ""
		} else {
			chunk = hex[:8]
			hex = hex[8:]
		}
		fmt.Sscanf(chunk, "%X", &value)
		r := fmt.Sprintf("%b", value)
		// Pad the bitstring
		fmt.Sscanf(chunk[:1], "%X", &first)
		if first < 8 { r = "0"+r}
		if first < 4 { r = "0"+r}
		if first < 2 { r = "0"+r}

		bits = bits + r
	
	}

	return bits
}

func literals(hex string) (int,string) {

	remainder := hex
	var value string
	var literal int
	
	for done := false; !done; {
		var end int
		var bits string
		remainder = hex[5:]
		fmt.Sscanf(hex[:5], "%1b%s", &end, &bits)
		value = value + bits
		if end == 0 {
			fmt.Sscanf(value, "%b", &literal)
			return literal, remainder
		}
		if len(hex) < 5 {
			done = true
		} else {
			hex = hex[5:]
		}
	}
	return literal, hex
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

func parseLiteral(hex string) int {
	var val string
	var literal int
	for len(hex) > 0 {
		var end int
		var bits string
		fmt.Sscanf(hex[:5], "%1b%s", &end, &bits)
		val = val + bits
		if end == 0 {
			fmt.Sscanf(val, "%b", &literal)
			return literal
		}
		hex = hex[5:]
	}
	return literal
}