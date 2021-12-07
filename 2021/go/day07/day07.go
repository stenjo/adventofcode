package day07

import (
	"strconv"
	"strings"
)

func ParseCrabs(s string) []int {
	var crabs []int

	// crabsS := strings.Split(s, ",")
	for _, f := range strings.Split(s, ",") {
		crab, _ := strconv.Atoi(f)
		crabs = append(crabs, crab)
	}
	return crabs
}

func GetFuel(crab []int, pos int) int {

	fuel := make([]int, len(crab))
	for i, c := range crab {
		fuel[i] = int(abs(c-pos))
	}
	return sum(fuel)
}

func GetFuelCrabs(crab []int, pos int) int {

	fuel := make([]int, len(crab))
	for i, c := range crab {
		fuel[i] = cost(int(abs(c-pos)))
	}
	return sum(fuel)
}

func cost(c int) int {
	var res int
	for i:= c; i > 0; i-- {
		res += i
	}
	return res
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func sum(list []int) int {

	var sum int
	for _, i := range list {
		sum += i
	}
	return sum
}

func average(list []int) int {

	return sum(list) / len(list)
}

func GetCheapes(str string) int {
	crabs := ParseCrabs(str)
	pos := average(crabs)
	fuel := GetFuel(crabs, pos)
	// cheapest := pos
	for i := 1; pos-i > 0; i++ {
		fu := GetFuel(crabs, pos+i)
		fl := GetFuel(crabs, pos-i)
		if fu < fuel || fl < fuel {
			if fu < fuel {
				fuel = fu
				// cheapest = i+pos
			} else {
				fuel = fl
				// cheapest = pos-i
			}
		} else {
			return fuel
		}
	}
	return fuel
}

func GetCheapestCrabsway(str string) int {
	crabs := ParseCrabs(str)
	pos := average(crabs)
	fuel := GetFuelCrabs(crabs, pos)
	// cheapest := pos
	for i := 1; pos-i > 0; i++ {
		fu := GetFuelCrabs(crabs, pos+i)
		fl := GetFuelCrabs(crabs, pos-i)
		if fu < fuel || fl < fuel {
			if fu < fuel {
				fuel = fu
				// cheapest = i+pos
			} else {
				fuel = fl
				// cheapest = pos-i
			}
		} else {
			return fuel
		}
	}
	return fuel
}
