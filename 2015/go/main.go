package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"

	"example.com/adventofcode/day02"
)

func main() {
	content, err := ioutil.ReadFile("../day02.txt")
	if err != nil {
		 log.Fatal(err)
	}
   fmt.Println(day02.TotalPaper(strings.Split(string(content), "\n")))
}

