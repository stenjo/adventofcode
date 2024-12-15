use warehouse::Warehouse;

pub mod loc;
pub mod warehouse;

pub fn part1(input: String) -> i64 {
    let mut w = Warehouse::new(&input);
    w.run_robot();

    return w.gps_sum();
}

pub fn part2(input: String) -> i64 {
    let mut w = Warehouse::new(&input);
    w.expand();
    w.run_robot();

    return w.gps_sum_2();
}
