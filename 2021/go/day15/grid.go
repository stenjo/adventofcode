package day15

type Grid map[xy]uint64

func (a Grid) has(n xy) bool {
	_, found := a[n]
	return found
}

func (a Grid) expand(maxX, maxY uint64) Grid {

	newGrid := Grid{}
	for y:=uint64(0); y < maxY; y++ {
		for x:=uint64(0); x < maxX; x++ {
			for i:=uint64(0); i < 5; i++ {
				for j:=uint64(0); j < 5; j++ {
					newGrid[xy{int((i*maxX) + x), int((j*maxY) + y)}] 	= wrap(a[xy{int(x),int(y)}]+i+j)
				}
			}
		}
	}
	return newGrid
}

// func (a Grid) print(width, height int) {
// 	for y := 0; y < height; y++ {
// 		s:=""
// 		for x := 0; x < width; x++ {
// 			s = s + strconv.FormatUint(a[xy{x,y}],10)
// 		}
// 		fmt.Println(s)
// 	}
// }

func wrap(i uint64) uint64 {
	return (i - 1) % 9 + 1
}
