use std::collections::HashSet;

use day16::track::Track;
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
#[case("#####\n#S.##\n#..E#\n#####", 2003)]
fn test_run(#[case] input: &str, #[case] result: i64) {
    use std::collections::HashSet;

    let mut t = Track::new(input);
    let score = t.run();
    t.print(&HashSet::new());
    assert_eq!(result, score, "Score should be {}", result);
}

#[rstest]
#[case(SMALL, 45)]
#[case(LARGE, 64)]
#[case("#####\n#S.##\n#..E#\n#####", 2003)]
fn test_stands(#[case] input: &str, #[case] result: i64) {
    let mut t = Track::new(input);
    t.run();
    let stands = t.get_stands();
    t.print(&stands);
    assert_eq!(result, stands.len() as i64, "Score should be {}", result);
}

#[rstest]
#[case(SMALL, 7036)]
#[case(LARGE, 11048)]
fn test1(#[case] input: &str, #[case] result: i64) {
    use day16::part1;

    assert_eq!(
        result,
        part1(input.to_string()),
        "Score should be {}",
        result
    );
}

#[rstest]
#[case(SMALL, 1751)]
#[case(LARGE, 9021)]
fn test2(#[case] input: &str, #[case] result: i64) {
    use day16::part2;

    assert_eq!(
        result,
        part2(input.to_string()),
        "Stands should be {}",
        result
    );
}

#[test]
fn test_new_track_large() {
    let w = Track::new(LARGE);
    w.print(&HashSet::new());
    assert_eq!(157, w.walls.len(), "Walls: ");
    assert_eq!((16, 16), w.size.as_tuple(), "Size: ");
    // assert_eq!(Track::node_index(1), w.start, "Start: ");
    // assert_eq!(Track::node_index(1), w.finish, "Finish: ");
}
