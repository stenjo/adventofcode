use assert_cmd::Command;
use day22::*;
use rstest::rstest;

#[rstest]
#[case(123, 1, 15887950)]
#[case(1, 2000, 8685429)]
#[case(10, 2000, 4700978)]
#[case(100, 2000, 15273692)]
#[case(2024, 2000, 8667524)]
fn test_secret(#[case] input: u64, #[case] iterations: usize, #[case] result: i64) {
    assert_eq!(result, calculate_price(input, iterations) as i64);
}

const TEST: &str = "1
10
100
2024";

#[rstest]
#[case(123, 6, vec![-1,-1,0,2])]
fn test_sequences(#[case] secret: u64, #[case] key: u64, #[case] result: Vec<i32>) {
    let seq = sequences(secret);
    assert_eq!(10, seq.len());
    assert_eq!(result, seq[&key]);
}

#[rstest]
#[case(123, vec![-1,-1,0,2], 6)]
#[case(1, vec![-2,1,-1,3], 7)]
#[case(2, vec![-2,1,-1,3], 7)]
#[case(3, vec![-2,1,-1,3], 0)]
#[case(2024, vec![-2,1,-1,3], 9)]
fn test_match_pattern(#[case] secret: u64, #[case] pattern: Vec<i32>, #[case] result: u64) {
    let seq = match_pattern(secret, pattern);
    assert_eq!(result, seq);
}

const TEST2: &str = "1
2
3
2024";

#[rstest]
#[case(2024, vec![1,2,3,2024], 23)]
fn test_check_for(#[case] secret: u64, #[case] buyers: Vec<u64>, #[case] result: i64) {
    assert_eq!(result, check_for(secret, buyers).unwrap() as i64);
}

#[rstest]
#[case(TEST2, 23)]
fn test_part2(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part2(input.to_string()) as i64);
}

#[rstest]
#[case(TEST, 37327623)]
fn test_part1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()) as i64);
}

// #[test]
// fn test_part1_success() {
//     Command::cargo_bin("day22")
//         .unwrap()
//         .arg("../../data/day22.txt")
//         .assert()
//         .success()
//         .stdout("14869099597\n14869099597\n");
// }
