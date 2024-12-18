use std::collections::HashSet;

use loc::Loc;
use track::Track;

pub mod loc;
pub mod track;
pub fn part1(input: String) -> i64 {
    let mut t = Track::new(input.as_str());

    return t.run();
}

pub fn part2(input: String) -> i64 {
    let mut t = Track::new(input.as_str());

    t.run();
    let mut stands: HashSet<Loc> = HashSet::new();
    let directions: [[char; 4]; 4] = [
        ['>', 'v', '<', '^'],
        ['v', '<', '^', '>'],
        ['<', '^', '>', 'v'],
        ['^', '>', 'v', '<'],
    ];
    for dir in directions {
        for l in t.get_stands(dir) {
            stands.insert(l);
        }
    }

    return stands.len() as i64;
}
