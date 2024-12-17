use assert_cmd::Command;
use day17::*;
use rstest::rstest;

const INPUT: &str = "Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0";

#[rstest]
#[case(INPUT, "4,6,3,5,6,3,5,2,1,0")]
fn test1(#[case] input: &str, #[case] result: &str) {
    assert_eq!(result, part1(input.to_string()));
}

#[rstest]
#[case(INPUT, 117440)]
fn test2(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part2(input.to_string()));
}

// #[test]
// fn test_part1_success() {
//     Command::cargo_bin("day17")
//         .unwrap()
//         .arg("../../data/day17.txt")
//         .assert()
//         .success()
//         .stdout("1,4,6,1,6,4,3,0,3\n386\n");
// }
