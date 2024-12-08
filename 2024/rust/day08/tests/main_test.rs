use assert_cmd::Command;
use day08::*;
use rstest::rstest;
const INPUT: &str = "............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............";

const K: &str = "......#.....
...#....0...
.....0....#.
.......0....
....0.......
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
............";
const L: &str = "......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#.";

#[rstest]
#[case(INPUT.to_string(), (8,8),(5,6), 'A', vec![(2,4),(11,10)])]
#[case(INPUT.to_string(), (5,7),(9,9), '0', vec![(1,5)])]
#[case(INPUT.to_string(), (1,8),(2,5), '0', vec![(3, 2), (0, 11)])]
#[case(INPUT.to_string(), (3,4),(2,7), '0', vec![(1,10),(4,1)])]
#[case(INPUT.to_string(), (2,7),(3,4), '0', vec![(4,1), (1,10)])]
fn test_antinodes(
    #[case] input: String,
    #[case] pos: (isize, isize),
    #[case] other: (isize, isize),
    #[case] freq: char,
    #[case] result: Vec<(isize, isize)>,
) {
    let area = Area::new(input);
    let curr = Pos::new(pos.0, pos.1, freq);
    let other = Pos::new(other.0, other.1, freq);
    let res: Vec<(isize, isize)> = area
        .antinodes(&curr, &other)
        .iter()
        .map(|n| n.as_tuple())
        .collect();
    assert_eq!(result, res)
}

#[rstest]
#[case(INPUT.to_string(), (5,6), 'A')]
fn test_display(#[case] input: String, #[case] pos: (isize, isize), #[case] result: char) {
    let area = Area::new(input);
    assert_eq!(result, area.get(pos.0, pos.1).unwrap().freq);
}

#[test]
fn test1() {
    assert_eq!(14, part1(INPUT.to_string()));
}
// #[test]
// fn test2() {
//     assert_eq!(14, part2(INPUT.to_string()));
// }

#[test]
fn test_part1_success() {
    Command::cargo_bin("day08")
        .unwrap()
        .arg("../../data/day08.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
