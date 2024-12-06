use assert_cmd::Command;
use day06::*;
use rstest::rstest;

#[rstest]
#[case::first("data", 4)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[rstest]
#[case::second("data", 4)]
fn test2(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day06")
        .unwrap()
        .arg("../../data/day06.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
