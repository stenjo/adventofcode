use assert_cmd::Command;
use day18::*;
use memory::Memory;
use rstest::rstest;

const TEST: &str = "5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0";

#[rstest]
#[case::first(TEST, 12, 22)]
fn test_drop(#[case] input: &str, #[case] bytes: usize, #[case] result: u64) {
    use loc::Loc;

    let mut m = Memory::new(input, (6, 6));

    m.drop(bytes);
    let path = m.least_cost_distance();

    m.print(path.clone());

    let cost = path.get(&m.memory[&Loc { x: 6, y: 6 }]).unwrap();
    assert_eq!(result, *cost);
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day18")
        .unwrap()
        .arg("../../data/day18.txt")
        .assert()
        .success()
        .stdout("322\n60,21\n");
}
