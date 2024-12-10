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
const INPUT2: &str = "89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732";

#[rstest]
#[case(INPUT.to_string(), 9)]
fn island_trailheads(#[case] input: String, #[case] result: usize) {
    let mut visited: Vec<Coord> = Vec::new();
    let mut trails: Vec<Vec<Coord>> = Vec::new();
    let mut i = Island::new(input);
    i.walk(Coord::new(0, 2), &mut visited, &mut trails);

    for t in trails.iter() {
        t.iter().for_each(|c| print!("{:?} ", c.to_tuple()));
        println!();
        i.print(t);
    }
    // i.print(&visited);
    assert_eq!(result, visited.len());
}
