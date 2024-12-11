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

#[rstest]
#[case("125 17", vec![17,125])]
#[case("0 1 10 99 999", vec![0,1,10,99,999])]
#[case("1 0 1 10 99 999", vec![0,1,10,99,999])]
fn stone_1(#[case] input: String, #[case] result: Vec<u128>) {
    let stones = Stones::new(input);
    let mut stone_keys: Vec<u128> = stones.keys();
    stone_keys.sort();
    println!("  keys: {:?}", stones.keys());
    println!("values: {:?}", stones.values());
    assert_eq!(result, stone_keys);
}

#[rstest]
#[case("125 17", 1, vec![253000, 1, 7], 3)] // 1
#[case("125 17", 2, vec![253, 0, 2024, 14168], 4)] // 2
#[case("125 17", 3, vec![512072, 1, 20, 24, 28676032], 5)]
#[case("125 17", 4, vec![512, 72, 2024, 2, 0, 4, 2867, 6032], 9)]
#[case("0 1", 1,vec![1, 2024],2)] // 5
#[case("1 1",1, vec![2024], 2)]
#[case("0 1 10 99 999",1, vec![1, 2024, 0, 9, 2021976], 7)] // 7
#[case("1 ",1, vec![2024], 1)]
#[case("0 ",1, vec![1], 1)]
#[case("2024",1, vec![20,24], 2)]
fn blink_2(
    #[case] input: String,
    #[case] count: usize,
    #[case] mut result: Vec<u128>,
    #[case] amount: u128,
) {
    let mut stones = Stones::new(input);
    stones.blink(count);
    result.sort();
    let mut stone_values = stones.keys();
    stone_values.sort();
    println!("  keys: {:?}", stones.keys());
    println!("values: {:?}", stones.values());
    println!("tuples: {:?}", stones.tuples());
    assert_eq!(result, stone_values);
    assert_eq!(amount, stones.count());
}

#[test]
fn test_blink() {
    for m in [872027] {
        let mut stones = Stones::new(m.to_string());
        print!("{} -> ", m);
        for _n in 1..26 {
            stones.blink(1);
            print!("{:?} -  ", stones.count());
        }
        println!();
    }
}

#[rstest]
#[case(872027, 1, vec![872, 27])]
#[case(0, 1, vec![1])]
#[case(1, 2, vec![2024])]
#[case(10, 1, vec![1, 0])]
fn test_process(#[case] m: u128, #[case] count: usize, #[case] mut result: Vec<u128>) {
    let mut stones = Stones::new(m.to_string());
    print!("{} -> ", m);

    let mut v = stones.process_number(&m, count as u64);
    print!("{:?} -  ", v);
    println!();

    result.sort();
    v.sort();
    assert_eq!(result, v.iter().map(|(x, _)| *x).collect::<Vec<u128>>());
}

#[rstest]
#[case("125 17", 25, 55312)]
#[case("125 17", 6, 22)]
#[case("0", 1, 1)]
#[case("1", 1, 1)]
fn part1_test(#[case] input: String, #[case] blinks: usize, #[case] result: i64) {
    let mut stones = Stones::new(input);
    stones.blink(blinks);

    assert_eq!(result, stones.count().try_into().unwrap());
}
#[rstest]
#[case("125 17", 55312)]
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
        .stdout("199946\n237994815702032\n");
}
