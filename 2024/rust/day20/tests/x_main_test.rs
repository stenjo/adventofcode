use assert_cmd::Command;
use day20::*;
use rstest::rstest;

#[rstest]
#[case::first("data", 4)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day20")
        .unwrap()
        .arg("../../data/day20.txt")
        .assert()
        .success()
        .stdout("1346\n386\n");
}
