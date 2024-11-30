use core::fmt;
use std::fmt::LowerHex;

pub fn part1(input: String) -> i64 {
    let mut key: i64 = 0;
    let mut hash = md5::compute(input.clone() + &key.to_string());

    while !format!("{:x}", hash).chars().take(5).all(|f| f == '0') {
        hash = md5::compute(input.clone() + &key.to_string());
        key += 1;
    }
    return key;
}

pub fn part2(input: String) -> i64 {
    let mut key: i64 = 0;
    let mut hash = md5::compute(input.clone() + &key.to_string());

    while !format!("{:x}", hash).chars().take(6).all(|f| f == '0') {
        hash = md5::compute(input.clone() + &key.to_string());
        key += 1;
    }
    return key;
}

pub fn main() {
    let input = std::env::args().nth(1).expect("Expected input argument");
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first("bgvyzdsv", 254576)]
    fn first(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }

    #[rstest]
    #[case::second("bgvyzdsv", 1038737)]
    fn second(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}
