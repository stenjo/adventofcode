use assert_cmd::Command;
use day14::*;
use rstest::rstest;

const FULL: &str = "p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3";

// #[rstest]
// #[case::first(FULL, 12)]
// fn test1(#[case] input: &str, #[case] result: i64) {
//     assert_eq!(result, part1(input.to_string()));
// }

// #[test]
// fn test_part1_success() {
//     Command::cargo_bin("day14")
//         .unwrap()
//         .arg("../../data/day14.txt")
//         .assert()
//         .success()
//         .stdout("321\n386\n");
// }
