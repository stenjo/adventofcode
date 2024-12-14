use farm::Farm;

pub mod farm;
pub mod loc;
pub mod plant;
pub mod plot;

pub fn part1(input: String) -> i64 {
    let mut farm = Farm::new(&input);
    let mut order: i64 = 0;
    for plot in farm.get_plots() {
        order += plot.perimeter() as i64 * plot.area() as i64;
    }

    return farm.price() as i64;
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
