package main

import (
	"bufio"
	"fmt"
	"log"
	"os"

	"example.com/aoc2018/day01"
	"example.com/aoc2018/day02"
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
	var day01_data = getdata("../data/input.txt")
	fmt.Println(day01.ResultingFrequency(day01_data))
	fmt.Println(day01.FrequencyReachedTwice(day01_data))

	// day02
	fmt.Println("\n-- Day 02 --")
	var day02_str = getdata("../data/input2.txt")
	fmt.Println(day02.ExactlyNum(day02_str, 2)*day02.ExactlyNum(day02_str, 3))
	fmt.Println(day02.CommonLetters(day02_str))

	// day02
	fmt.Println("\n-- Day 03 --")
	// var day03_str = getdata("../day03.txt")
	// fmt.Println(day03.GetPowerConsumption(day03_str))
	// fmt.Println(day03.GetLifeSupportRating(day03_str))
}