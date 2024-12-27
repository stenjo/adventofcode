use aoc::Solver;
use day24::Solution;
use logic::Logic;

pub mod aoc;
pub mod day24;
pub mod logic;

pub fn part1(input: String) -> i64 {
    let mut l = Logic::new(&input);
    l.run();
    return l.number();
}

pub fn part2(input: String) -> String {
    let s = Solution::new(&input);
    let mut sol = s.unwrap();

    let result = sol.part2();
    return format!("{}", result.unwrap());
}
