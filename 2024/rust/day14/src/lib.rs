use restroom::Restroom;

pub mod loc;
pub mod restroom;

pub fn part1(input: String) -> i64 {
    let mut restroom = Restroom::new(&input, 101, 103);
    restroom.move_robots(100);
    return restroom.safety_factor();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
