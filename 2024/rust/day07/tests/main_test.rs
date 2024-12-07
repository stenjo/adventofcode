use assert_cmd::Command;
use day07::*;
use rstest::rstest;

#[rstest]
#[case(1, vec![vec!['*'], vec!['+']])]
#[case(2, vec![
    vec!['*', '*'],
    vec!['+', '*'],
    vec!['*', '+'],
    vec!['+', '+'],
])]
#[case(3, vec![
    vec!['*', '*', '*'],
    vec!['+', '*', '*'],
    vec!['*', '+', '*'],
    vec!['+', '+', '*'],
    vec!['*', '*', '+'],
    vec!['+', '*', '+'],
    vec!['*', '+', '+'],
    vec!['+', '+', '+'],
])]
fn test_gen_operations(#[case] length: usize, #[case] expected: Vec<Vec<char>>) {
    let equation = Equation::new("3267: 81 40 27").unwrap();
    let result = equation.gen_operations(length);
    assert_eq!(result, expected);
}

#[rstest]
// #[case("190: 10 19", 190)]
#[case("3267: 81 40 27", 3267)]
// #[case("83: 17 5", 0)]
// #[case(
//     "156: 15 6
//                 ",
//     0
// )]
// #[case("7290: 6 8 6 15", 0)]
// #[case("161011: 16 10 13", 0)]
// #[case("192: 17 8 14", 0)]
// #[case("21037: 9 7 18 13", 0)]
// #[case("292: 11 6 16 20", 292)]
fn test_solver(#[case] input: &str, #[case] result: i64) {
    let eq = Equation::new(input).unwrap();
    assert_eq!(result, eq.solve());
}

#[rstest]
#[case("190: 10 19", 190, 2)]
#[case("3267: 81 40 27", 3267, 3)]
#[case("83: 17 5", 83, 2)]
#[case(
    "156: 15 6
                ",
    156,
    2
)]
#[case("7290: 6 8 6 15", 7290, 4)]
#[case("161011: 16 10 13", 161011, 3)]
#[case("192: 17 8 14", 192, 3)]
#[case("21037: 9 7 18 13", 21037, 4)]
#[case("292: 11 6 16 20", 292, 4)]
fn test_equation_new(#[case] input: &str, #[case] value: i64, #[case] result: i32) {
    let eq = Equation::new(input).unwrap();
    assert_eq!(value, eq.val);
    assert_eq!(result, eq.nums.len() as i32)
}

#[rstest]
#[case(
    "190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20",
    3749
)]
fn test1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day07")
        .unwrap()
        .arg("../../data/day07.txt")
        .assert()
        .success()
        .stdout("1611660863222\n386\n");
}
