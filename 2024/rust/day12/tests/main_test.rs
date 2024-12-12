// use assert_cmd::Command;
use day12::*;
use rstest::rstest;

const LARGE: &str = "RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE";

const SPECIAL: &str = "OOOOO
OXOXO
OOOOO
OXOXO
OOOOO";

const SIMPLE: &str = "AAAA
BBCD
BBCC
EEEC";

// #[rstest]
// #[case(SIMPLE.to_string(), 140)]
// #[case(SPECIAL.to_string(), 772)]
// #[case(LARGE.to_string(), 1930)]
// fn test1(#[case] input: String, #[case] result: i64) {
// assert_eq!(result, part1(input));
// }

#[rstest]
#[case(SIMPLE.to_string(), 16)]
#[case(SPECIAL.to_string(), 25)]
#[case(LARGE.to_string(), 100)]
fn farm_plants_test(#[case] input: String, #[case] result: i64) {
    use farm::Farm;
    let farm = Farm::new(&input);
    assert_eq!(result, farm.get_plants().len() as i64);
}

#[rstest]
#[case("A", 4)]
#[case("AA", 12)]
#[case(
    "AA
BB", 24
)]
#[case("AABB", 24)]
fn farm_price_test(#[case] input: String, #[case] result: i64) {
    use farm::Farm;
    let farm = Farm::new(&input);
    assert_eq!(result, farm.price() as i64);
}

#[rstest]
#[case("A", 4)]
#[case("AA", 6)]
#[case("AABB", 6)]
#[case(
    "A
A", 6
)]
fn farm_perimeter_test(#[case] input: String, #[case] result: i64) {
    use farm::Farm;
    let farm = Farm::new(&input);
    let plots = farm.get_plots();
    let plot = plots.first().unwrap();
    println!("{:?}", plot);
    assert_eq!(result, plot.perimeter() as i64);
}

#[rstest]
#[case("A", 1)]
#[case("AA", 1)]
#[case("ABA", 3)]
#[case("ABA\nCCC", 4)]
#[case("AABB", 2)]
#[case("A\nA", 1)]
#[case("RCCCJF\nVVCJJC\nVVCCJJ\nCCCCCC", 4)]
#[case(SIMPLE.to_string(), 5)]
#[case(SPECIAL.to_string(), 5)]
#[case(LARGE.to_string(), 11)]
fn farm_plots_test(#[case] input: String, #[case] result: i64) {
    use farm::Farm;
    let farm = Farm::new(&input);
    let plots = farm.get_plots();
    print!(
        "{:?}",
        plots
            .iter()
            .map(|plot| plot.plant_type())
            .collect::<Vec<char>>()
    );
    for plot in plots.iter() {
        plot.print(plot.connecting_positions());
    }
    assert_eq!(result, plots.len() as i64);
}

// #[test]
// fn test_part1_success() {
//     Command::cargo_bin("day12")
//         .unwrap()
//         .arg("../../data/day12.txt")
//         .assert()
//         .success()
//         .stdout("321\n386\n");
// }
