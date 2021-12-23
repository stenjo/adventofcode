package day16

func GetVersionsSum(s string) int {

	pkg, _ := decode(toBits(s))

	return pkg.sumVer()
}

func GetValue(s string) int {

	pkg, _ := decode(toBits(s))

	return pkg.val
}

func decode(bits Bits) (Package, Bits) {

	p := Package{ver: bits.getBits(0, 3), typ: bits.getBits(3, 3)}
	tail := Bits(string(bits)[6:])

	if p.typ == LITERAL {
		tail = p.parseLiteral(tail)
	} else {
		tail = p.parseOperator(tail)
	}

	switch p.typ {
	case 0: // sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
		p.val = p.sumVal()
	case 1: // product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
		p.val = p.productVal()
	case 2: // minimum packets - their value is the minimum of the values of their sub-packets.
		p.val = p.minVal()
	case 3: // maximum packets - their value is the maximum of the values of their sub-packets.
		p.val = p.maxVal()
	case 5: // greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
		p.val = p.gtVal()
	case 6: // less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
		p.val = p.ltVal()
	case 7: // equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
		p.val = p.eqVal()
	}

	return p, tail
}
