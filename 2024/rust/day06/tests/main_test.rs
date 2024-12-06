use std::{collections::HashSet, fs};

use assert_cmd::Command;
use day06::{find_obstacle_options, walk, *};
use rstest::rstest;

const TEST_INPUT: &str = "....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...";

#[rstest]
#[case::first(TEST_INPUT.to_string(), 41)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[test]
fn test2() {
    let path = "../../data/day06.txt".to_string();
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };

    assert_eq!(4515, part1(input));
}

#[test]
fn test_getguard() {
    assert_eq!((6, 4), get_guard(TEST_INPUT.to_string()));
}

#[test]
fn test_options() {
    let input = TEST_INPUT.to_string();
    let labmap = get_map(&input);
    let guard = get_guard(input.clone());
    let dir = get_dir(input);
    let options = find_obstacle_options(guard, dir, labmap.clone());
    print_map(guard, &labmap, &walk(guard, dir, &labmap), &options);
    assert_eq!(vec![(6, 4, 3), (7, 7, 2), (7, 8, 1)], options);
}

fn print_map(
    guard: (usize, usize),
    labmap: &Vec<Vec<bool>>,
    path: &Vec<(i32, i32, usize)>,
    options: &Vec<(i32, i32, usize)>,
) {
    println!();
    println!();
    let o: Vec<(i32, i32)> = options.iter().map(|p| (p.0, p.1)).collect();
    for (i, row) in labmap.iter().enumerate() {
        for (j, cell) in row.iter().enumerate() {
            if *cell {
                print!("  # ");
            } else if (i, j) == guard {
                print!("  @ ");
            } else if o.contains(&(i as i32, j as i32)) {
                print!(
                    " {:2} ",
                    o.iter()
                        .position(|&x| x == (i as i32, j as i32))
                        .unwrap_or(0)
                );
            } else if path.contains(&(i as i32, j as i32, 0)) {
                print!("  ^ ");
            } else if path.contains(&(i as i32, j as i32, 1)) {
                print!("  > ");
            } else if path.contains(&(i as i32, j as i32, 2)) {
                print!("  v ");
            } else if path.contains(&(i as i32, j as i32, 3)) {
                print!("  < ");
            } else {
                print!("  . ");
            }
        }
        println!();
    }
    println!()
}
#[rstest]
#[case::second(TEST_INPUT.to_string(), 6)]
fn test_2(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part2(input));
}

#[test]
fn day_success() {
    Command::cargo_bin("day06")
        .unwrap()
        .arg("../../data/day06.txt")
        .assert()
        .success()
        .stdout("4515\n386\n");
}
