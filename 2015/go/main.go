package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"example.com/adventofcode/day01"
	"example.com/adventofcode/day02"
	"example.com/adventofcode/day03"
	"example.com/adventofcode/day04"
	"example.com/adventofcode/day05"
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
	fmt.Println(" -- Day 01 -- ")
	var day01_data = getdata("../day01.txt")
	fmt.Println(day01.FindFloor(strings.Join(day01_data, " ")))
	fmt.Println(day01.FindFirstPos(strings.Join(day01_data, " ")))

	// day02
	fmt.Println(" -- Day 02 -- ")
	var day02_str = getdata("../day02.txt")
	fmt.Println(day02.TotalPaper(day02_str))
	fmt.Println(day02.TotalRibbon(day02_str))

	// day02
	fmt.Println(" -- Day 03 -- ")
	var day03_str = getdata("../day03.txt")
	fmt.Println(day03.PresentDelivery(strings.Join(day03_str, "")))
	fmt.Println(day03.RoboSanta(strings.Join(day03_str, "")))

	// day04
	fmt.Println(" -- Day 04 -- ")
	var day04_str = "bgvyzdsv"
	fmt.Println(day04.GetHashCount(day04_str))
	fmt.Println(day04.Day4sideB(day04_str))

	// day05
	fmt.Println(" -- Day 05 -- ")
	var day05_str = getdata("../day05.txt")
	fmt.Println(day05.GetNiceStrings(day05_str))
	fmt.Println(day05.GetRealNiceStrings(day05_str))

}
