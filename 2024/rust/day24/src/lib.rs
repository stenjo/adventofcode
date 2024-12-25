use logic::Logic;

pub mod logic;

pub fn part1(input: String) -> i64 {
    let mut l = Logic::new(&input);
    l.run();
    return l.number();
}

pub fn part2(input: String) -> i64 {
    let mut l = Logic::new(&input);
    l.run();
    return l.swapped_gates();
}
