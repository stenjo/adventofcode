use assert_cmd::Command;
use day16::*;
use rstest::rstest;

const LARGE: &str = "#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################";

const SMALL: &str = "###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############";

#[rstest]
#[case(SMALL, 7036)]
#[case(LARGE, 11048)]
fn test1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()));
}
// #[rstest]
// #[case(SMALL, 45)]
// #[case(LARGE, 64)]
// fn test2(#[case] input: &str, #[case] result: i64) {
//     assert_eq!(result, part2(input.to_string()));
// }

// #[test]
// fn test_part1_success() {
//     Command::cargo_bin("day16")
//         .unwrap()
//         .arg("../../data/day16.txt")
//         .assert()
//         .success()
//         .stdout("122492\n386\n");
// }
