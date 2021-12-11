package day11

import (
	"strconv"
)

type Octo struct {
	charge int
	flashed bool
}

type OctoMap [][]Octo

func GetFlashes(str []string, steps int) int {

	var result int
	octos := parseOctos(str)
	for i := 0; i < steps; i++ {
		result += octos.RunStep()
	}

	return result
}

func SimultanFlash(str []string) int {

	octos := parseOctos(str)
	for i := 1; i < 1000000000; i++ {
		if octos.RunStep() == 100 {
			return i
		}
	}

	return 0
}

func (m *OctoMap) RunStep() int {
	var flashes int
	// Increase energy level by 1
	for y:= 0; y < len(*m); y++ {
		for x:= 0; x < len((*m)[y]); x++ {
			(*m).Increase(x,y)
		}
	}

	// Set all flased to 0 and count flashes
	for y:= 0; y < len(*m); y++ {
		for x:= 0; x < len((*m)[y]); x++ {
			if (*m)[y][x].flashed {
				(*m)[y][x].charge = 0
				(*m)[y][x].flashed = false
				flashes += 1
			}
		}
	}
	
	return flashes
}

func (m *OctoMap) Increase(x,y int) {
	(*m)[y][x].charge += 1
	if (*m)[y][x].charge > 9 && !(*m)[y][x].flashed {
		(*m)[y][x].flashed = true
		(*m).IncreaseNeighbours(x,y)
	}
}

func (m *OctoMap) IncreaseNeighbours(x,y int) {
	if x > 0 			  && y > 0 			 { (*m).Increase(x-1,y-1) }
	if 						 y > 0 			 { (*m).Increase(x,  y-1) }
	if x < len((*m)[y])-1 && y > 0 			 { (*m).Increase(x+1,y-1) }
	if x > 0					  			 { (*m).Increase(x-1,y)   }
	if x < len((*m)[y])-1 		  			 { (*m).Increase(x+1,y)   }
	if x > 0 		  	  && y < len(*m)-1   { (*m).Increase(x-1,y+1) }
	if 						 y < len(*m)-1   { (*m).Increase(x,  y+1) }
	if x < len((*m)[y])-1 && y < len(*m)-1   { (*m).Increase(x+1,y+1) }
}

func parseOctos(str []string) OctoMap {
	res := make(OctoMap,len(str))

	for i, s := range str {
		res[i] = make([]Octo, len(s))
		for j, c := range s {
			v, _ := strconv.Atoi(string(c))
			res[i][j].charge = v
		}
	}
	return res
}