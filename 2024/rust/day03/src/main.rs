use regex::Regex;
use std::fs;

pub fn part1(input: String) -> i64 {
    let re = Regex::new(r"mul\((\-?\d+),(\-?\d+)\)").unwrap();
    let mut results = Vec::new();

    // Find all matches in the input string
    for cap in re.captures_iter(&input) {
        // Extract x and y as integers
        let x: i64 = cap[1].parse().unwrap();
        let y: i64 = cap[2].parse().unwrap();
        results.push((x, y));
    }
    let mut sum = 0;
    for pair in results {
        sum += pair.0 * pair.1;
    }
    return sum;
}

pub fn part2(input: String) -> i64 {
    let does: Vec<&str> = input.split("do()").collect();
    let mut results: Vec<(i64, i64)> = Vec::new();
    for todo in does {
        let donts: Vec<&str> = todo.split("don\'t(").collect();
        let s = donts.get(0).unwrap_or(&"");
        let re = Regex::new(r"mul\((\-?\d+),(\-?\d+)\)").unwrap();

        for cap in re.captures_iter(&s) {
            let x: i64 = cap[1].parse().unwrap();
            let y: i64 = cap[2].parse().unwrap();
            results.push((x, y));
        }
    }
    let mut sum = 0;
    for pair in results {
        sum += pair.0 * pair.1;
    }
    return sum;
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first(
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
        161
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }
    #[rstest]
    #[case::second(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
        48
    )]
    fn test2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}

pub fn main() {
    let path = "../data/".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
