use day01::part1;
use day01::part2;
use std::fs;

fn main() {
    match fs::read_to_string("../day01.txt") {
        Ok(s) => {
            println!("Day 01, Part 1: {}", part1(&s));
            println!("Day 01, Part 2: {}", part2(&s));
        }
        Err(e) => {
            println!("Error reading file. {}", e)
        }
    }
}
