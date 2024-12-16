use track::Track;

pub mod loc;
pub mod track;
pub fn part1(input: String) -> i64 {
    let mut t = Track::new(input.as_str());

    return t.run_reindeer();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
