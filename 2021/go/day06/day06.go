package day06

import (
	"strconv"
	"strings"
)

func RunLanternFishDay(fish []int) []int {

	for i, f := range fish {
		if f > 0 {
			fish[i] = f - 1
		} else {
			fish[i] = 6
			fish = append(fish, 8)
		}
	}
	return fish
}

func RunLanternFishGens(s string, gens int) int {

	fish := ParseFish(s)
	for i := 0; i < gens; i++ {
		fish = RunLanternFishDay(fish)
	}
	return len(fish)
}

func RunLanternFishCycles(s string, gens int) int {

	fish := ParseFish(s)
	var ages [9]int
	for _,f := range fish {
		ages[f] += 1
	}

	for i := 0; i < gens; i++ {
		mothers := ages[0]
		for a := 1; a < len(ages); a++ {
			ages[a-1] = ages[a]
		}
		ages[8] = mothers
		ages[6] += mothers
	}

	return sum(ages)
}

func sum(ages [9]int) int {

	var s int
	for _,i := range ages {
		s += i
	}
	return s
}


func ParseFish(s string) []int {
	var fishes []int

	fishS := strings.Split(s, ",")
	for _,f := range fishS {
		fish,_ := strconv.Atoi(f)
		fishes = append(fishes,fish)
	}
	return fishes
}