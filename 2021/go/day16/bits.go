package day16

import (
	"fmt"
	"strconv"
	"strings"
)

type Bits string

func toBits(hex string) Bits {
	var value int
	var first int
	var bits Bits

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
		if first < 8 {
			r = "0" + r
		}
		if first < 4 {
			r = "0" + r
		}
		if first < 2 {
			r = "0" + r
		}

		bits = Bits(string(bits) + string(r))

	}

	return bits
}

func (b Bits)toHex() string {
	var val int
	var hex string

	bits := string(b)
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

func (bits Bits) splitAt(pos int) (Bits, Bits) {
	return bits[:pos], bits[pos:]
}

func (bits Bits) isAllZeros() bool {
	return bits == Bits(strings.Repeat("0", len(bits)))
}
func (bits Bits) getBits(index, length int) int {

	var val int
	var trash string
	format := "%" + strconv.Itoa(length) + "b"
	if index > 0 {
		format = "%" + strconv.Itoa(index) + "s" + format
		fmt.Sscanf(string(bits), format, &trash, &val)
	} else {
		fmt.Sscanf(string(bits), format, &val)
	}
	return val
}
