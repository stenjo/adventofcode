use assert_cmd::Command;
use day22::*;
use rstest::rstest;

#[rstest]
#[case::first("data", 4)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}


#[test]
fn test_part1_success() {
    Command::cargo_bin("day22")
        .unwrap()
        .arg("../../data/day22.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
