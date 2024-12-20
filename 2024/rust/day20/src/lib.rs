use track::Track;

pub mod loc;
pub mod track;

pub fn part1(input: String) -> i64 {
    let mut t = Track::new(&input);

    return t.best_cheats(100).unwrap();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
