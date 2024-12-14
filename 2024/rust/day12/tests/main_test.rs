use assert_cmd::Command;

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

const MEDIUM: &str = "AAAAA
ABCCA
ABADD
ABCCC
AAACC";

#[rstest]
#[case(SIMPLE.to_string(), 140)]
#[case(SPECIAL.to_string(), 772)]
#[case(LARGE.to_string(), 1930)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

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
#[case("A", vec![4])]
#[case("AA", vec![6])]
#[case("AABB", vec![6,6])]
#[case("A\nA", vec![6])]
#[case(SIMPLE, vec![10,8,8,4,10])]
fn farm_perimeter_test(#[case] input: &str, #[case] result: Vec<i64>) {
    use farm::Farm;
    let mut farm = Farm::new(&input);
    let plots = farm.get_plots();

    print!(
        "{:?}",
        plots
            .iter()
            .map(|plot| plot.plant_type())
            .collect::<Vec<char>>()
    );
    for (key, plot) in plots.iter().enumerate() {
        plot.print(plot.edges());
        assert_eq!(result[key], plot.perimeter() as i64);
    }
}

#[rstest]
#[case("A", 1)]
#[case("AA", 1)]
#[case("ABA", 3)]
#[case("ABA\nCCC", 4)]
#[case("AABB", 2)]
#[case("A\nA", 1)]
#[case("VCCCJC\nVVCJJC\nVVCCJJ\nCCCCCC", 4)]
#[case(SIMPLE.to_string(), 5)]
#[case(SPECIAL.to_string(), 5)]
#[case(MEDIUM.to_string(), 6)]
#[case(LARGE.to_string(), 11)]
fn farm_plots_test(#[case] input: String, #[case] result: i64) {
    use farm::Farm;
    let mut farm = Farm::new(&input);
    let plots = farm.get_plots();
    print!(
        "{:?}",
        plots
            .iter()
            .map(|plot| plot.plant_type())
            .collect::<Vec<char>>()
    );
    for plot in plots.iter() {
        if plot.plant_type() == 'C' {
            plot.print(plot.edges());
        }
    }
    assert_eq!(result, plots.len() as i64);
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day12")
        .unwrap()
        .arg("../../data/day12.txt")
        .assert()
        .success()
        .stdout("1485656\n386\n");
}
