use assert_cmd::assert;
use day15::*;
use rstest::rstest;
use warehouse::Warehouse;

const LARGE: &str = "##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^";

const SMALL: &str = "########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<";

#[rstest]
#[case(SMALL, 2028)]
#[case(LARGE, 10092)]
fn test1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()), "GPS should be {}", result);
}

#[rstest]
#[case(SMALL, 1751)]
#[case(LARGE, 9021)]
fn test2(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part2(input.to_string()), "GPS should be {}", result);
}

// ########
// #..O.O.#
// ##@.O..#
// #...O..#
// #.#.O..#
// #...O..#
// #......#
// ########

#[rstest]
#[case(vec!['<'], false, (2,2))]
#[case(vec!['^'], true, (2,1))]
#[case(vec!['>'], true, (3,2))]
#[case(vec!['v'], true, (2,3))]
#[case(vec!['v','<'], true, (1,3))]
#[case(vec!['>','>'], true, (4,2))]
#[case(vec!['>','>','>','>'], false, (5,2))]
fn test_move_robot(#[case] input: Vec<char>, #[case] moved: bool, #[case] result: (i64, i64)) {
    let mut w = Warehouse::new(SMALL);
    let mut success = false;
    for &c in &input {
        success = w.move_robot(c)
    }
    assert_eq!(success, moved, "Moved should be {} for {:?}", moved, input);
    assert_eq!(result, w.robot.as_tuple(), "GPS should be {:?}", result);
}

const DOUBLE: &str = "#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^";

#[rstest]
#[case(vec!['<'], true, (9,3))]
#[case(vec!['^'], true, (10,2))]
#[case(vec!['>'], true, (11,3))]
#[case(vec!['v'], true, (10,4))]
#[case(vec!['>','>'], false, (11,3))]
#[case(vec!['<','v'], true,(9,4))]
#[case(vec!['<','v','v','<','<','^'], true, (7,4))]
#[case(vec!['<','v','v','<','<','^','^'], false, (7,4))]
fn test_move_robot_2(#[case] input: Vec<char>, #[case] moved: bool, #[case] result: (i64, i64)) {
    let mut w = Warehouse::new(DOUBLE);
    let mut success = false;
    w.expand();
    w.print();
    for &c in &input {
        success = w.move_robot_2(c);
    }
    w.print();
    assert_eq!(success, moved, "Moved should be {} for {:?}", moved, input);
    assert_eq!(
        result,
        w.robot.as_tuple(),
        "Position of robot should be {:?}",
        result
    );
}

#[rstest]
#[case("#####\n#O@.#\n#####\n\n<", 102)]
#[case("#####\n#.@.#\n#.O.#\n#####\n\n<", 204)]
#[case("#####\n#.@.#\n#...#\n#..O#\n#####\n\n<", 306)]
#[case(LARGE, 9021)]
fn test_gps_2(#[case] input: &str, #[case] result: i64) {
    let mut w = Warehouse::new(&input);
    let walls = w.walls.len();
    w.expand();
    assert_eq!(walls * 2, w.walls.len(), "Walls should be doubled");
    w.run_robot_2();
    assert_eq!(walls * 2, w.walls.len(), "Walls should still be doubled");
    w.print();
    assert!(w.validate_2(), "Boxes should be paired");
    assert_eq!(result, w.gps_sum_2());
}

#[rstest]
#[case(DOUBLE, 618)]
#[case(LARGE, 9021)]
fn test_part2(#[case] input: &str, #[case] result: i64) {
    let mut w = Warehouse::new(&input);
    w.expand();
    w.run_robot_2();

    w.print();
    assert_eq!(result, w.gps_sum_2());
}

#[test]
fn test_new_warehouse_large() {
    let w = Warehouse::new(LARGE);
    assert_eq!(37, w.walls.len(), "Walls: ");
    assert_eq!(21, w.boxes.len(), "Boxes: ");
    assert_eq!((4, 4), w.robot.as_tuple(), "Robot: ");
    assert_eq!(700, w.moves.len(), "Moves: ");
}

#[test]
fn test_new_warehouse_small() {
    let w = Warehouse::new(SMALL);
    assert_eq!(30, w.walls.len(), "Walls: ");
    assert_eq!(6, w.boxes.len(), "Boxes: ");
    assert_eq!((2, 2), w.robot.as_tuple(), "Robot: ");
    assert_eq!(15, w.moves.len(), "Moves: ");
}
