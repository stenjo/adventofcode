use computer::Computer;

pub mod computer;

pub fn part1(input: String) -> String {
    let mut c = Computer::new(input.as_str());
    c.run();
    let result = c.output();
    let s = result
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(",");
    return s;
}

pub fn part2(input: String) -> u128 {
    let c = Computer::new(input.as_str());
    let result = c.run_to_copy();
    return result;
}
