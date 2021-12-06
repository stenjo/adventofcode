package day06

import (
	"fmt"
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
	length := len(fish)
	var m int
	for i := 0; i < gens; i++ {
		m,fish = RunCycle(fish, gens)
		length += m * len(fish)
		i += m
		fmt.Println(length, fish)
	}
	return length + len(fish)
}

func RunCycle(f []int, max int) (int, []int) {
	length := len(f)
	hash := hashFunc(f)
	// multiplier := 1
	// fmt.Println(length)
	for i := 1; i <= max; i++ {
		f = RunLanternFishDay(f)
		if hash == hashFunc(f[:length]) {
			// fmt.Println(i)
			// multiplier *= i
			f = f[length:]
			return i,f
		}
	}
	return 1, f
}

func hashFunc(v []int) int {
    var hash int
    var i uint
    for _, x := range v {
        hash |= int(x) << (i * 8)
        i++
    }
    return hash
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