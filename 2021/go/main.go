package main

import (
	"fmt"
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
	"example.com/aoc2021/day11"
	"example.com/aoc2021/day12"
	"example.com/aoc2021/day13"
	"example.com/aoc2021/day14"
	"example.com/aoc2021/day15"
	"example.com/aoc2021/day17"
	"example.com/aoc2021/day18"
	"example.com/aoc2021/day20"
	"example.com/aoc2021/tools"
)


func main() {

	// day01
	fmt.Println("\n-- Day 01 --")
	var day01_data = tools.GetData("../day01.txt")
	fmt.Println(day01.CountDepth(day01_data))
	fmt.Println(day01.SlidingDepth(day01_data))

	// day02
	fmt.Println("\n-- Day 02 --")
	var day02_str = tools.GetData("../day02.txt")
	fmt.Println(day02.MoveTo(day02_str))
	fmt.Println(day02.AimTo(day02_str))

	// day03
	fmt.Println("\n-- Day 03 --")
	var day03_str = tools.GetData("../day03.txt")
	fmt.Println(day03.GetPowerConsumption(day03_str))
	fmt.Println(day03.GetLifeSupportRating(day03_str))

	// day04
	fmt.Println("\n-- Day 04 --")
	var day04_str = tools.GetData("../day04.txt")
	fmt.Println(day04.FinalScore(day04_str))
	fmt.Println(day04.LastWinnerScore(day04_str))

	// day05
	fmt.Println("\n-- Day 05 --")
	var day05_str = tools.GetData("../day05.txt")
	fmt.Println(day05.GetOverlappingPoints(day05_str))
	fmt.Println(day05.GetDagonalOverlappingPoints(day05_str))

	// day06
	fmt.Println("\n-- Day 06 --")
	var day06_str = tools.GetData("../day06.txt")
	fmt.Println(day06.RunLanternFishGens(strings.Join(day06_str, ","), 80))
	fmt.Println(day06.RunLanternFishCycles(strings.Join(day06_str, ","), 256))

	// day07
	fmt.Println("\n-- Day 07 --")
	var day07_str = tools.GetData("../day07.txt")
	fmt.Println(day07.GetCheapes(strings.Join(day07_str, ",")))
	fmt.Println(day07.GetCheapestCrabsway(strings.Join(day07_str, ",")))

	// day08
	fmt.Println("\n-- Day 08 --")
	var day08_str = tools.GetData("../day08.txt")
	fmt.Println(day08.GetUniqueSegmentsDigitCount(day08_str))
	fmt.Println(day08.GetOutputValueSum(day08_str))

	// day09
	fmt.Println("\n-- Day 09 --")
	var day09_str = tools.GetData("../day09.txt")
	fmt.Println(day09.GetRiskLevelSum(day09_str))
	fmt.Println(day09.GetBasinProducst(day09_str))

	// day10
	fmt.Println("\n-- Day 10 --")
	var day10_str = tools.GetData("../day10.txt")
	fmt.Println(day10.GetSyntaxErrorPoints(day10_str))
	fmt.Println(day10.GetCompletionScore(day10_str))

	// day11
	fmt.Println("\n-- Day 11 --")
	var day11_str = tools.GetData("../day11.txt")
	fmt.Println(day11.GetFlashes(day11_str, 100))
	fmt.Println(day11.SimultanFlash(day11_str))

	// day12
	fmt.Println("\n-- Day 12 --")
	var day12_str = tools.GetData("../day12.txt")
	fmt.Println(day12.GetPaths(day12_str))
	fmt.Println(day12.GetPathsPart2(day12_str))
	
	// day13
	fmt.Println("\n-- Day 13 --")
	var day13_str = tools.GetData("../day13.txt")
	fmt.Println(day13.DotsWhenFoldedOnce(day13_str))
	fmt.Println(day13.DotsWhenFoldedAll(day13_str))
	
	// day14
	fmt.Println("\n-- Day 14 --")
	var day14_str = tools.GetData("../day14.txt")
	fmt.Println(day14.GetElementDiff(day14_str))
	fmt.Println(day14.GetElementDiff40(day14_str))
	
	// day15
	fmt.Println("\n-- Day 15 --")
	var day15_str = tools.GetData("../day15.txt")
	fmt.Println(day15.GetLowestRiskPath(day15_str))
	// fmt.Println(day15.GetLowestRiskPathExtended(day15_str))
	
	// day16
	fmt.Println("\n-- Day 16 --")
	// var day16_str = tools.GetData("../day16.txt")
	// fmt.Println(day16.GetLowestRiskPath(day16_str))
	// fmt.Println(day16.GetLowestRiskPathExtended(day16_str))
	
	// day17
	fmt.Println("\n-- Day 17 --")
	var day17_str = tools.GetData("../day17.txt")
	fmt.Println(day17.GetHighestY(strings.Join(day17_str, "")))
	fmt.Println(day17.GetNumOfDistinctV(strings.Join(day17_str, "")))

	// day18
	fmt.Println("\n-- Day 18 --")
	var day18_str = tools.GetData("../day18.txt")
	fmt.Println(day18.GetMagnitude(day18_str))
	// fmt.Println(days.Day18(day18_str))
	
	// day19
	fmt.Println("\n-- Day 19 --")
	// var day19_str = tools.GetData("../day19.txt")
	// fmt.Println(day19.GetLowestRiskPath(day19_str))
	// fmt.Println(day19.GetLowestRiskPathExtended(day19_str))

	// day20
	fmt.Println("\n-- Day 20 --")
	var day20_str = tools.GetData("../day20.txt")
	fmt.Println(day20.GetCountBy2Enhancements(day20_str))
	// fmt.Println(day20.GetLowestRiskPathExtended(day20_str))
}
