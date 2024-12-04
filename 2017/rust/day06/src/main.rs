use std::fs;

pub fn part1(input: String) -> i32 {
    let mut banks: Vec<i32> = input.split_whitespace().map(|x| x.into()).collect();
    let mut cycles: i32 = 0;

    return cycles;
}

pub fn part2(input: String) -> i32 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first("0 2 7 0", 5)]
    fn test1(#[case] input: String, #[case] result: i32) {
        assert_eq!(result, part1(input));
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
