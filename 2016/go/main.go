package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"example.com/aoc2016/day01"
	"example.com/aoc2016/day02"
	"example.com/aoc2016/day03"
	"example.com/aoc2016/day04"
	"example.com/aoc2016/day05"
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
	fmt.Println("\n -- Day 01 --")
	var day01_data = getdata("../day01.txt")
	fmt.Println(day01.RunString(strings.Join(day01_data, " ")))
	fmt.Println(day01.VisitedTwice(strings.Join(day01_data, " ")))
	
	// day02
	fmt.Println("\n -- Day 02 --")
	var day02_str = getdata("../day02.txt")
	fmt.Println(day02.KeypadDecode(day02_str))
	fmt.Println(day02.NightmareKeypadDecode(day02_str))
	
	// day03
	fmt.Println("\n -- Day 03 --")
	var day03_str = getdata("../day03.txt")
	fmt.Println(day03.FindValidTriangles(day03_str))
	fmt.Println(day03.FindValidVerticalTriangles(day03_str))
	
	// day04
	fmt.Println("\n -- Day 04 --")
	var day04_str = getdata("../day04.txt")
	fmt.Println(day04.RealRoomSectorIdSums(day04_str))
	fmt.Println(day04.NortPoleObjectsId(day04_str))

	// day05
	fmt.Println("\n -- Day 05 --")
	var day05_str = "ojvtpuvg"
	fmt.Println(day05.GetPassword(day05_str))
	fmt.Println(day05.GetBetterSolution(day05_str))
	
}