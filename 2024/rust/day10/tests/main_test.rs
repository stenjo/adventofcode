use assert_cmd::Command;
use day10::*;
use rstest::rstest;

#[rstest]
#[case::first("data", 4)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}


#[test]
fn test_part1_success() {
    Command::cargo_bin("day10")
        .unwrap()
        .arg("../../data/day10.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
