use assert_cmd::Command;
use day10::*;
use rstest::rstest;

const INPUT: &str = "89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732";
#[rstest]
#[case::first(INPUT.to_string(), 36)]
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
        .stdout("841\n1875\n");
}
