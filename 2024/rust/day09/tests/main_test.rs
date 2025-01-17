use assert_cmd::Command;
use day09::*;
use rstest::rstest;

#[rstest]
#[case(1, 6, 6, 6)]
#[case(0, 6, 0, 6)]
#[case(2, 2, 0, 2)]
#[case(4, 1, 0, 1)]
fn test_block(#[case] id: i32, #[case] size: usize, #[case] free: i64, #[case] check: i64) {
    let dm = Block::new(id, size);
    assert_eq!(free, dm.free_space());
    assert_eq!(check, dm.blocks().len() as i64);
}

#[rstest]
#[case::_00201("00201", 0, 5)]
#[case::_12345("12345", 6, 60)]
#[case::_2333133121414131402("2333133121414131402", 14, 1928)]
fn test_optimize1(#[case] input: String, #[case] free: i64, #[case] check: i64) {
    let mut dm = DiskMap::new(input);
    dm.print().unwrap();
    println!("00...111...2...333.44.5555.6666.777.888899");
    dm.optimize();
    dm.print().unwrap();
    println!("0099811188827773336446555566..............");
    assert_eq!(free, dm.free_space());
    assert_eq!(check, dm.checksum());
}
#[rstest]
#[case::_00201("00201", 0, 5)]
#[case::_12345("12345", 6, 132)]
#[case::_2333133121414131402("2333133121414131402", 14, 2858)]
fn test_optimize2(#[case] input: String, #[case] free: i64, #[case] check: i64) {
    let mut dm = DiskMap::new(input);
    dm.print().unwrap();
    println!("00...111...2...333.44.5555.6666.777.888899");
    dm.optimize2();
    dm.print().unwrap();
    println!("00992111777.44.333....5555.6666.....8888..");
    assert_eq!(free, dm.free_space());
    assert_eq!(check, dm.checksum());
}

#[rstest]
#[case("2333133121414131402", 1928)]
fn test_part1(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part1(input));
}

#[rstest]
#[case("2333133121414131402", 2858)]
fn test_part2(#[case] input: String, #[case] result: i64) {
    assert_eq!(result, part2(input));
}

#[test]
fn test_day09_success() {
    Command::cargo_bin("day09")
        .unwrap()
        .arg("../../data/day09.txt")
        .assert()
        .success()
        .stdout("6461289671426\n6488291456470\n");
}
