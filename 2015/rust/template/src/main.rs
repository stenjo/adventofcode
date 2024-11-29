use std::fs;

pub fn part1(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first("data", 4)]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }
}

pub fn main() {
    let path = "../".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
