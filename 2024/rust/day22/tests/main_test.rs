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
#[case(TEST, 37327623)]
fn test_part1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()) as i64);
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day22")
        .unwrap()
        .arg("../../data/day22.txt")
        .assert()
        .success()
        .stdout("14869099597\n386\n");
}
