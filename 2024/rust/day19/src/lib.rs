pub mod design;

use design::Design;

pub fn part1(input: String) -> i64 {
    let design = Design::new(input.as_str());
    let result = design.valid_designs();
    return result as i64;
}

pub fn part2(input: String) -> i64 {
    let design = Design::new(input.as_str());
    let result = design.max_combinations();
    return result as i64;
}
