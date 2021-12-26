package day24

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

type Inst struct {
	op, v, n string
}
type Alu struct {
	input []int64
	vars map[string]int64
}

func (a *Alu) getInput() int64 {
	if len((*a).input) != 0 {
		val := (*a).input[0]
		(*a).input = (*a).input[1:]

		return val
	}
	return int64(math.NaN())
}

func (a *Alu) addInput(val int64) int {
	(*a).input = append((*a).input, val)
	return len((*a).input)
}

func (a *Alu) run(args []string) int64 {
	var res int64
	for _, v := range args {
		parts := strings.Split(v, " ")
		if len(parts) < 3 {
			res = (*a).compute(Inst{parts[0], parts[1], ""})
		} else {
			res = (*a).compute(Inst{parts[0], parts[1], parts[2]})
		}
	}

	return res
}

func verifyMONAD(monad int64, args []string) bool { 
	alu := Alu{}
	alu.input = make([]int64,0)
	alu.vars = make(map[string]int64, 0)
	for _, v := range intoToArr(monad) {
		alu.addInput(v)
	}

	alu.run(args)
	//13579246899999
	return alu.vars["z"] == 0
}

func intoToArr(i int64) []int64 {
	intArr := make([]int64,0)
	intStr := fmt.Sprintf("%d", i)
	for _, v := range intStr {
		val,_ := strconv.Atoi(string(v))
		intArr = append(intArr,int64(val))
	}
	return intArr
}

func RunOnNum(num []int64, ins []string) int64 {
	alu := Alu{}
	alu.input = make([]int64,0)
	alu.vars = make(map[string]int64, 0)
	for _, v := range num {
		alu.addInput(v)
	}
	return alu.run(ins)
}

func (alu * Alu) compute(i Inst) int64 {

	switch i.op {
	case "inp":
		(*alu).vars[i.v] = (*alu).getInput()
	case "add":
		(*alu).vars[i.v] = (*alu).vars[i.v] + (*alu).valOrVar(i.n)
	case "mul":
		(*alu).vars[i.v] = (*alu).vars[i.v] * (*alu).valOrVar(i.n)
	case "div":
		(*alu).vars[i.v] = (*alu).vars[i.v] / (*alu).valOrVar(i.n)
	case "mod":
		(*alu).vars[i.v] = (*alu).vars[i.v] % (*alu).valOrVar(i.n)
	case "eql":
		if (*alu).vars[i.v] == (*alu).valOrVar(i.n) {
			(*alu).vars[i.v] = 1
		} else {
			(*alu).vars[i.v] = 0
		}
	}
	return (*alu).vars[i.v]
}

func (alu * Alu) valOrVar(v string) int64 {
	if isNum(v) {
		return atoi(v)
	} else {
		return (*alu).vars[v]
	}
}

func atoi(a string) int64 {
	i, err := strconv.ParseInt(string(a), 10, 64)
	if err != nil {
		panic(err)
	}
	return int64(i)
}

func isNum(v string) bool {
	if _, err := strconv.Atoi(v); err == nil {
		return true
	}
	return false
}