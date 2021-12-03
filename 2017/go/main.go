package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"

	"example.com/aoc2017/day01"
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
	var day01_data = getdata("../data/input1.txt")
	fmt.Println(day01.Day01(strings.Join(day01_data, " ")))
	// fmt.Println(day01.FindFirstPos(strings.Join(day01_data, " ")))

	// day02
	// var day02_str = getdata("../day02.txt")
	// fmt.Println(day02.TotalPaper(day02_str))
	// fmt.Println(day02.TotalRibbon(day02_str))

	// day02
	// var day03_str = getdata("../day03.txt")
	// fmt.Println(day03.PresentDelivery(strings.Join(day03_str, "")))
	// fmt.Println(day03.RoboSanta(strings.Join(day03_str, "")))

	// day04
	// var day04_str = "bgvyzdsv"
	// fmt.Println(day04.GetHashCount(day04_str))
	// fmt.Println(day04.Day4sideB(day04_str))

}
