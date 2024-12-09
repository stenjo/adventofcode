use std::{fs, time::Instant};

use day09::{part1, part2};

pub fn main() {
    let path = "".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    let now = Instant::now();
    println!("{}", part1(input.clone()));
    println!("{:?}", now.elapsed());
    // println!("{}", part2(input));
    now.elapsed();
}