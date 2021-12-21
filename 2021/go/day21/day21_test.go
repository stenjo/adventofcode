package day21

import (
	"reflect"
	"testing"

	"example.com/aoc2021/tools"
)

func Test_loadPlayers(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name  string
		args  args
		want  Player
		want1 Player
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"Player 1 starting position: 4", "Player 2 starting position: 5"}}, Player{4, 0}, Player{5, 0}},
		{"1", args{str: tools.GetData("../../day21.txt")}, Player{4, 0}, Player{5, 0}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := loadPlayers(tt.args.str)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("loadPlayers() got = %v, want %v", got, tt.want)
			}
			if !reflect.DeepEqual(got1, tt.want1) {
				t.Errorf("loadPlayers() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}

func TestPlayer_play(t *testing.T) {
	type args struct {
		d *Dice
		t Track
	}
	tests := []struct {
		name string
		p    *Player
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.p.play(tt.args.d, tt.args.t); got != tt.want {
				t.Errorf("Player.play() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrack_move(t *testing.T) {
	type args struct {
		p *Player
		n int
	}
	tests := []struct {
		name string
		tr   Track
		args args
		want int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.tr.move(tt.args.p, tt.args.n); got != tt.want {
				t.Errorf("Track.move() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestDice_roll(t *testing.T) {
	tests := []struct {
		name string
		d    *Dice
		want int
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.d.roll(); got != tt.want {
				t.Errorf("Dice.roll() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestTrack_init(t *testing.T) {
	tests := []struct {
		name string
		tr   *Track
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			tt.tr.init()
		})
	}
}

func TestGame1(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"Player 1 starting position: 4", "Player 2 starting position: 8"}}, 739785},
		{"2", args{str: []string{"Player 1 starting position: 4", "Player 2 starting position: 5"}}, 864900},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Game1(tt.args.str); got != tt.want {
				t.Errorf("Game1() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGame2(t *testing.T) {
	type args struct {
		str []string
	}
	tests := []struct {
		name string
		args args
		want int64
	}{
		// TODO: Add test cases.
		{"1", args{str: []string{"Player 1 starting position: 4", "Player 2 starting position: 8"}}, 444356092776315},
		{"2", args{str: []string{"Player 1 starting position: 4", "Player 2 starting position: 5"}}, 575111835924670},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := Game2(tt.args.str); got != tt.want {
				t.Errorf("Game2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestGetWinsAndLosses(t *testing.T) {
	type args struct {
		s1 int64
		s2 int64
		p1 int64
		p2 int64
	}
	tests := []struct {
		name  string
		args  args
		want  int64
		want1 int64
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, got1 := GetWinsAndLosses(tt.args.s1, tt.args.s2, tt.args.p1, tt.args.p2)
			if got != tt.want {
				t.Errorf("GetWinsAndLosses() got = %v, want %v", got, tt.want)
			}
			if got1 != tt.want1 {
				t.Errorf("GetWinsAndLosses() got1 = %v, want %v", got1, tt.want1)
			}
		})
	}
}
