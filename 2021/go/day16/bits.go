package day16

import (
	"fmt"
	"strconv"
	"strings"
)

type Bits string

func toBits(hex string) Bits {
	var bits Bits
	for _,c := range hex {
		ui,_ := strconv.ParseUint(string(c), 16, 64)
		b := fmt.Sprintf("%04b", ui)
		bits = Bits(string(bits) + b)
	}
	return bits
}

func (bits Bits) splitAt(pos int) (Bits, Bits) {
	return bits[:pos], bits[pos:]
}

func (bits Bits) isAllZeros() bool {
	return bits == Bits(strings.Repeat("0", len(bits)))
}
func (bits Bits) getBits(index, length int) int {

	out,_ := strconv.ParseInt(string(bits[index:index+length]),2,64)
	return int(out)
}
