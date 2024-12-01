use std::fs;

pub fn part1(input: String) -> i64 {
    let mut diff: i64 = 0;
    let mut left: Vec<i64> = Vec::<i64>::new();
    let mut right: Vec<i64> = Vec::<i64>::new();
    for line in input.lines() {
        let numbers: Vec<i64> = line
            .split_whitespace()
            .map(|s| s.parse::<i64>().expect("Invalid number"))
            .collect();

        if numbers.len() == 2 {
            let (num1, num2) = (numbers[0], numbers[1]);
            left.push(num1);
            right.push(num2);
        }
    }
    left.sort();
    right.sort();

    while let Some(num1) = left.pop() {
        if let Some(num2) = right.pop() {
            let abs_diff = (num1 - num2).abs();
            diff += abs_diff;
        }
        // Calculate the absolute difference
    }
    return diff;
}

pub fn part2(input: String) -> i64 {
    let mut similarity: i64 = 0;
    let mut left: Vec<i64> = Vec::<i64>::new();
    let mut right: Vec<i64> = Vec::<i64>::new();
    for line in input.lines() {
        let numbers: Vec<i64> = line
            .split_whitespace()
            .map(|s| s.parse::<i64>().expect("Invalid number"))
            .collect();

        if numbers.len() == 2 {
            let (num1, num2) = (numbers[0], numbers[1]);
            left.push(num1);
            right.push(num2);
        }
    }
    left.sort();
    right.sort();

    while let Some(num1) = left.pop() {
        let freq = right.iter().filter(|&&n| n == num1).count() as i64;
        similarity += num1 * freq;

        // Calculate the absolute difference
    }
    return similarity;
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first("1 3", 2)]
    #[case::second("7 3\n1 5", 4)]
    #[case::all(
        "3   4
    4   3
    2   5
    1   3
    3   9
    3   3",
        11
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }

    #[rstest]
    #[case::sim("7 3\n1 5", 0)]
    #[case::all(
        "3   4
    4   3
    2   5
    1   3
    3   9
    3   3",
        31
    )]
    fn test2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}

pub fn main() {
    let path =
        "../../data/".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
