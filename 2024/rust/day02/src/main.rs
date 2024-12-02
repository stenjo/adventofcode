use std::fs;

fn safety(input: String) -> bool {
    let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("Invalid number"))
        .collect();
    let mut safe = true;

    let mut 
    for idx in 1..5 {
        let diff = (numbers[idx] - numbers[idx - 1]);
        let abs_diff = diff.abs();
        if diff/abs_diff != direction;
        let direction = diff/abs_diff;
        if abs_diff < 1 || abs_diff > 3 {
            safe = false;
        }
    }

    return safe;
}

pub fn part1(input: String) -> i64 {
    let mut safe_lines: i64 = 0;
    for line in input.lines() {
        if safety(line.to_owned()) {
            safe_lines += 1;
        }
    }
    return safe_lines;
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("7 6 4 2 1", true)]
    #[case("1 2 7 8 9", false)]
    #[case("9 7 6 2 1", false)]
    #[case("1 3 2 4 5", false)]
    #[case("8 6 4 4 1", false)]
    #[case("1 3 6 7 9", true)]
    fn test_safe(#[case] input: String, #[case] result: bool) {
        assert_eq!(result, safety(input))
    }

    #[rstest]
    #[case::first(
        "7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9",
        2
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
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
