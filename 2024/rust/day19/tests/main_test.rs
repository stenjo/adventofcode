use assert_cmd::Command;
use day19::*;
use rstest::rstest;

const TEST: &str = "r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb";
#[rstest]
#[case::first(TEST, 6)]
fn test1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day19")
        .unwrap()
        .arg("../../data/day19.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
