use assert_cmd::Command;
use day25::*;
use rstest::rstest;
const TEST: &str = "#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####";

const SMALL: &str = "#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####
";
#[rstest]
#[case("#####\n..#..\n\n.....\n##.##", 1, 1, 1)]
#[case("#####\n..#..\n\n.....\n....#", 1, 1, 1)]
#[case(SMALL, 2, 1, 6)]
fn test_new(#[case] input: &str, #[case] keys: i64, #[case] locks: i64, #[case] sum: i64) {
    let m = Matching::new(input);
    println!(
        "key: {:?}, lock: {:?}",
        m.keys.get(0).unwrap(),
        m.locks.get(0).unwrap()
    );
    assert_eq!(sum, m.keys[0][0] as i64 + m.locks[0][0] as i64, "sum");
    assert_eq!(keys, m.keys.len() as i64, "keys");
    assert_eq!(locks, m.locks.len() as i64, "locks");
}

#[rstest]
#[case::first(SMALL, 0)]
#[case::first(TEST, 3)]
fn test1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day25")
        .unwrap()
        .arg("../../data/day25.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
