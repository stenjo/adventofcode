package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"example.com/aoc2021/day01"
	"example.com/aoc2021/day02"
	"example.com/aoc2021/day03"
	"example.com/aoc2021/day04"
	"example.com/aoc2021/day05"
	"example.com/aoc2021/day06"
	"example.com/aoc2021/day07"
	"example.com/aoc2021/day08"
	"example.com/aoc2021/day09"
	"example.com/aoc2021/day10"
)

func getdata(file string) []string {
	f, err := os.Open(file)

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	var str []string

	for scanner.Scan() {
		str = append(str, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return str
}

func main() {

	// day01
	fmt.Println("\n-- Day 01 --")
	var day01_data = getdata("../day01.txt")
	fmt.Println(day01.CountDepth(day01_data))
	fmt.Println(day01.SlidingDepth(day01_data))

	// day02
	fmt.Println("\n-- Day 02 --")
	var day02_str = getdata("../day02.txt")
	fmt.Println(day02.MoveTo(day02_str))
	fmt.Println(day02.AimTo(day02_str))

	// day03
	fmt.Println("\n-- Day 03 --")
	var day03_str = getdata("../day03.txt")
	fmt.Println(day03.GetPowerConsumption(day03_str))
	fmt.Println(day03.GetLifeSupportRating(day03_str))

	// day04
	fmt.Println("\n-- Day 04 --")
	var day04_str = getdata("../day04.txt")
	fmt.Println(day04.FinalScore(day04_str))
	fmt.Println(day04.LastWinnerScore(day04_str))

	// day05
	fmt.Println("\n-- Day 05 --")
	var day05_str = getdata("../day05.txt")
	fmt.Println(day05.GetOverlappingPoints(day05_str))
	fmt.Println(day05.GetDagonalOverlappingPoints(day05_str))

	// day06
	fmt.Println("\n-- Day 06 --")
	var day06_str = getdata("../day06.txt")
	fmt.Println(day06.RunLanternFishGens(strings.Join(day06_str, ","), 80))
	fmt.Println(day06.RunLanternFishCycles(strings.Join(day06_str, ","), 256))

	// day07
	fmt.Println("\n-- Day 07 --")
	var day07_str = getdata("../day07.txt")
	fmt.Println(day07.GetCheapes(strings.Join(day07_str, ",")))
	fmt.Println(day07.GetCheapestCrabsway(strings.Join(day07_str, ",")))

	// day08
	fmt.Println("\n-- Day 08 --")
	var day08_str = getdata("../day08.txt")
	fmt.Println(day08.GetUniqueSegmentsDigitCount(day08_str))
	fmt.Println(day08.GetOutputValueSum(day08_str))

	// day09
	fmt.Println("\n-- Day 09 --")
	var day09_str = getdata("../day09.txt")
	fmt.Println(day09.GetRiskLevelSum(day09_str))
	fmt.Println(day09.GetBasinProducst(day09_str))

	// day10
	fmt.Println("\n-- Day 10 --")
	var day10_str = getdata("../day10.txt")
	fmt.Println(day10.GetSyntaxErrorPoints(day10_str))
	fmt.Println(day10.GetCompletionScore(day10_str))

}
