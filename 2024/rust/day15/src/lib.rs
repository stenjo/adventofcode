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
    let walls = w.walls.len();
    w.expand();
    assert_eq!(walls * 2, w.walls.len(), "Walls should be doubled");
    w.run_robot_2();

    assert_eq!(walls * 2, w.walls.len(), "Walls should still be doubled");
    assert!(w.validate_2(), "Boxes should be paired");
    // w.print();
    return w.gps_sum_2();
}
