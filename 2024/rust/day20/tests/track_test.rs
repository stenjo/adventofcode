use std::collections::{HashMap, HashSet};

use day20::loc::Loc;
use day20::track::Track;
use rstest::rstest;

const LARGE: &str = "###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############";

#[rstest]
#[case(LARGE, 85)]
#[case("#####\n#S.##\n#..E#\n#####", 5)]
fn test_map_track(#[case] input: &str, #[case] result: i64) {
    let mut t = Track::new(input);

    let track_map: HashMap<Loc, i64> = t.map_track();
    t.print_map(&track_map);
    assert_eq!(result, track_map.len() as i64, "Score should be {}", result);
}

#[rstest]
#[case(LARGE, 5)]
fn test1(#[case] input: &str, #[case] result: i64) {
    let mut t = Track::new(&input);

    let cheats = t.best_cheats(20).unwrap();
    assert_eq!(result, cheats, "Score should be {}", result);
}

#[rstest]
#[case(LARGE, 239)]
fn test2(#[case] input: &str, #[case] result: i64) {
    use day20::part2;

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
    assert_eq!(140, w.walls.len(), "Walls: ");
    assert_eq!((14, 14), w.size.as_tuple(), "Size: ");
}
