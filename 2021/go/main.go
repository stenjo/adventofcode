package main

import (
	"bufio"
	"fmt"
	"log"
	"os"

	"example.com/aoc2021/day01"
	"example.com/aoc2021/day02"
	"example.com/aoc2021/day03"
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

	// day02
	fmt.Println("\n-- Day 03 --")
	var day03_str = getdata("../day03.txt")
	fmt.Println(day03.GetPowerConsumption(day03_str))
	fmt.Println(day03.GetLifeSupportRating(day03_str))
}
