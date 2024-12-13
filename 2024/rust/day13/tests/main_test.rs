use assert_cmd::Command;
use day13::*;
use rstest::rstest;

const FULL_TEST: &str = "Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279";

#[rstest]
#[case(FULL_TEST, 480)]
fn test1(#[case] input: &str, #[case] result: i128) {
    assert_eq!(result, part1(input.to_string()));
}
#[rstest]
#[case(FULL_TEST, 480)]
fn test2(#[case] input: &str, #[case] result: i128) {
    assert_eq!(result, part2(input.to_string()));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day13")
        .unwrap()
        .arg("../../data/day13.txt")
        .assert()
        .success()
        .stdout("34393\n83551068361379\n");
}
