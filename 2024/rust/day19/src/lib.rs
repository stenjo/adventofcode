use design::Design;

pub mod design;

pub fn part1(input: String) -> i64 {
    let d = Design::new(&input);
    return d.valid_designs() as i64;
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
