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
fn test_run(#[case] input: &str, #[case] result: i64) {
    let mut t = Track::new(input);
    let score = t.run_reindeer();
    t.print();
    assert_eq!(result, score, "Score should be {}", result);
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

// #[rstest]
// #[case(SMALL, 1751)]
// #[case(LARGE, 9021)]
// fn test2(#[case] input: &str, #[case] result: i64) {
//     assert_eq!(result, part2(input.to_string()), "GPS should be {}", result);
// }

#[test]
fn test_new_warehouse_large() {
    let w = Track::new(LARGE);
    w.print();
    assert_eq!(157, w.walls.len(), "Walls: ");
    assert_eq!((16, 16), w.size.as_tuple(), "Size: ");
    // assert_eq!(Track::node_index(1), w.start, "Start: ");
    // assert_eq!(Track::node_index(1), w.finish, "Finish: ");
}
