package day21

import (
	"fmt"
	"strings"
)

type Track [10]int64

type Dice struct {
	value  int
	rolls  int64
}

type Player struct {
	pos   int
	score int64
}

func (p *Player) play(d *Dice, t Track) int64 {

	moves := (*d).roll() + (*d).roll() + (*d).roll()
	(*p).score += t.move(p,moves)

	return (*p).score
}

func (t Track) move(p *Player,n int) int64 {
	pos := (((*p).pos-1) + n)%len(t)
	(*p).pos = int(t[pos])

	return t[pos]
}

func (d *Dice) roll() int {
	if (*d).value == 100 {
		(*d).value = 0
	}
	(*d).value++
	(*d).rolls++

	return (*d).value
}

func (t *Track) init() {
	for i := 0; i < len(t); i++ {
		(*t)[i] = int64(i+1)
	}
}

func Game1(str []string) int64 { 
	die := Dice{}
	board := Track{}
	board.init()
	p1,p2 := loadPlayers(str)

	var turn int
	for {
		turn ++
		p1.play(&die,board)
		if p1.score >= 1000 {
			return p2.score * die.rolls
		}

		p2.play(&die,board)
		if p2.score >= 1000 {
			return p1.score * die.rolls
		}

	}
}

func Game2(str []string) int64 { 
	p1,p2 := loadPlayers(str)

	wins,_ := GetWinsAndLosses(p1.score, p2.score, int64(p1.pos), int64(p2.pos))

	return wins
}

// Recursive algoritm stolen from https://www.reddit.com/r/adventofcode/comments/rl6p8y/comment/hpe6bgn/?utm_source=share&utm_medium=web2x&context=3
// Credits to mental-chaos for this one
func GetWinsAndLosses(s1,s2,p1,p2 int64) (int64, int64) {
	if s2 >= 21 {
		return 0,1
	}
	var wins, losses int64
	rolls := map[int64]int64{3:1,4:3,5:6,6:7,7:6,8:3,9:1}
	for roll,freq := range rolls {
		newPos := (p1 + roll -1) % 10 + 1
		newLosses, newWins := GetWinsAndLosses(s2, s1 + newPos, p2, newPos )
		wins += newWins * freq
		losses += newLosses * freq
	}
	return wins, losses
}

func loadPlayers(str []string) (Player, Player) {
	p1 := Player{}
	p2 := Player{}
	// Player 1 starting position: 4
	// Player 2 starting position: 5

	fmt.Sscanf(strings.Join(str, ","), "Player 1 starting position: %d,Player 2 starting position: %d", &p1.pos, &p2.pos)

	return p1, p2
}