use day10::island::Island;
use day10::*;
use island::Coord;
use rstest::rstest;

const INPUT: &str = "89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732";
const INPUT2: &str = ".....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9.... ";

#[rstest]
#[case(INPUT2.to_string(), (0,5), 3)]
#[case(INPUT.to_string(), (0,2), 20)]
#[case(INPUT.to_string(), (0,4), 24)]
#[case(INPUT.to_string(), (2,4), 10)]
#[case(INPUT.to_string(), (4,6), 4)]
#[case(INPUT.to_string(), (5,2), 1)]
#[case(INPUT.to_string(), (5,5), 4)]
#[case(INPUT.to_string(), (6,0), 5)]
#[case(INPUT.to_string(), (6,6), 8)]
#[case(INPUT.to_string(), (7,1), 5)]
fn island_rating(#[case] input: String, #[case] start: (usize, usize), #[case] result: usize) {
    let mut visited: Vec<Coord> = Vec::new();
    let mut trails: Vec<Vec<Coord>> = Vec::new();
    let mut i = Island::new(input);
    i.rating(Coord::new(start.0, start.1), &mut visited, &mut trails);

    for t in trails.iter() {
        t.iter().for_each(|c| print!("{:?} ", c.to_tuple()));
        println!();
        // i.print(t);
    }
    // i.print(&visited);
    assert_eq!(result, trails.len());
}

#[rstest]
#[case(INPUT.to_string(), (0,2), 5)]
#[case(INPUT.to_string(), (0,4), 6)]
#[case(INPUT.to_string(), (2,4), 5)]
#[case(INPUT.to_string(), (4,6), 3)]
#[case(INPUT.to_string(), (5,2), 1)]
#[case(INPUT.to_string(), (5,5), 3)]
#[case(INPUT.to_string(), (6,0), 5)]
#[case(INPUT.to_string(), (6,6), 3)]
#[case(INPUT.to_string(), (7,1), 5)]
fn island_trailheads(#[case] input: String, #[case] start: (usize, usize), #[case] result: usize) {
    let mut visited: Vec<Coord> = Vec::new();
    let mut trails: Vec<Vec<Coord>> = Vec::new();
    let mut i = Island::new(input);
    i.walk(Coord::new(start.0, start.1), &mut visited, &mut trails);

    for t in trails.iter() {
        // t.iter().for_each(|c| print!("{:?} ", c.to_tuple()));
        println!();
        // i.print(t);
    }
    // i.print(&visited);
    assert_eq!(result, trails.len());
}

#[test]
fn test_get_height() {
    let input = "123\n456\n789".to_string();
    let island = Island::new(input);
    assert_eq!(island.get_height(Coord::new(0, 0)), Some(1));
    assert_eq!(island.get_height(Coord::new(2, 2)), Some(9));
    assert_eq!(island.get_height(Coord::new(3, 3)), None);
}

#[test]
fn test_get_starting_points() {
    let input = "012\n345\n678".to_string();
    let island = Island::new(input);
    let starting_points = island.get_starting_points();
    assert_eq!(starting_points, vec![Coord::new(0, 0)]);
}

#[test]
fn test_print() {
    let input = "012\n345\n678".to_string();
    let island = Island::new(input);
    let trail = vec![Coord::new(0, 0), Coord::new(0, 1), Coord::new(0, 2)];
    island.print(&trail);
}
