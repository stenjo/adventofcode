use assert_cmd::Command;
use day11::*;
use rstest::rstest;

// #[rstest]
// #[case("125 17", 2)]
// #[case("0 1 10 99 999", 2)]
// #[case("0 1 10 99 999", 2)]
// fn blink_test(#[case] input: String, #[case] result: i64) {
//     let stones = Stones::new(input);
//     let stones = stones.blink();
//     assert_eq!(result, stones.sum() as i64);
// }

// #[rstest]
// #[case("125 17", 2)]
// #[case("0 1 10 99 999", 2)]
// #[case("0 1 10 99 999", 2)]
// fn blink_1(#[case] input: String, #[case] result: i64) {
//     let stones = Stones::new(input);
//     let stones = stones.blink();
//     assert_eq!(result, stones.sum() as i64);
// }
#[rstest]
#[case("125 17", 1, vec![253000, 1, 7])]
#[case("0 1", 1,vec![1, 2024])]
#[case("0 1 10 99 999",1, vec![1, 2024, 1, 0, 9, 9, 2021976])]
fn blink_2(#[case] input: String, #[case] count: usize, #[case] result: Vec<u128>) {
    let mut stones = Stones::new(input);
    stones.blink(count);
    assert_eq!(result, stones.values());
}

#[rstest]
#[case("125 17", 55312)]
fn part1_test(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}
#[rstest]
#[case("125 17", 4)]
fn part2_test(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day11")
        .unwrap()
        .arg("../../data/day11.txt")
        .assert()
        .success()
        .stdout("199946\n0\n");
}
