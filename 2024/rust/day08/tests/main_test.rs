use std::collections::HashSet;

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

#[rstest]
#[case(INPUT.to_string(), (0,0),(0,11), 12, (0,11))]
#[case(INPUT.to_string(), (0,0),(0,11), 12, (0,11))]
#[case(INPUT.to_string(), (1,0),(11,0), 12, (11,0))]
#[case(INPUT.to_string(), (5,6),(8,8), 4, (11, 10))]
#[case(INPUT.to_string(), (0,0),(2,1), 6, (10,5))]
#[case(INPUT.to_string(), (11,0),(1,0), 12, (11,0))]
#[case(INPUT.to_string(), (0,0),(1,0), 12, (11,0))]
#[case(INPUT.to_string(), (2,5),(3,7), 6, (5,11))]
// #[case(INPUT.to_string(), (3,4),(2,7), '0', (4,1))]
// #[case(INPUT.to_string(), (2,7),(3,4), '0', (1,10))]
fn test_diagonal(
    #[case] input: String,
    #[case] pos: (isize, isize),
    #[case] other: (isize, isize),
    #[case] count: usize,
    #[case] result: (isize, isize),
) {
    let area = Area::new(input);
    let curr = Pos::new(pos.0, pos.1, '@');
    let other = Pos::new(other.0, other.1, '@');
    let positions: Vec<(isize, isize)> = area
        .get_diagonal(curr, other)
        .iter()
        .map(|&p| p.loc.as_tuple())
        .collect();
    let res: (isize, isize) = area.get_diagonal(curr, other).pop().unwrap().loc.as_tuple();
    let mut pos_set: HashSet<Loc> = HashSet::new();
    for t in positions.clone() {
        pos_set.insert(Loc::new(t.0, t.1));
    }
    println!("{:?}", positions.clone());
    area.display(pos_set);
    assert_eq!(count, positions.len());
    assert_eq!(result, res)
}
#[rstest]
#[case(INPUT.to_string(), (8,8),(5,6), 'A', (11,10))]
#[case(INPUT.to_string(), (5,7),(9,9), '0', (1,5))]
#[case(INPUT.to_string(), (1,8),(2,5), '0', (0, 11))]
#[case(INPUT.to_string(), (3,4),(2,7), '0', (4,1))]
#[case(INPUT.to_string(), (2,7),(3,4), '0', (1,10))]
fn test_antinodes(
    #[case] input: String,
    #[case] pos: (isize, isize),
    #[case] other: (isize, isize),
    #[case] freq: char,
    #[case] result: (isize, isize),
) {
    let area = Area::new(input);
    let curr = Pos::new(pos.0, pos.1, freq);
    let other = Pos::new(other.0, other.1, freq);
    let res: (isize, isize) = area.antinodes(&curr, &other).unwrap().as_tuple();
    assert_eq!(result, res)
}

const INPUT_SQ: &str = "...1...1....
............
............
1...........
............
............
............
1...........
............
............
.1..........
1.....1.....";

#[rstest]
#[case(INPUT_SQ, 55)]
#[case(
    "1......1....
.............",
    12
)]
fn test_part2(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part2(input.to_string()));
}

#[test]
fn test1() {
    assert_eq!(14, part1(INPUT.to_string()));
}
#[test]
fn test2() {
    assert_eq!(34, part2(INPUT.to_string()));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day08")
        .unwrap()
        .arg("../../data/day08.txt")
        .assert()
        .success()
        .stdout("265\n962\n");
}
