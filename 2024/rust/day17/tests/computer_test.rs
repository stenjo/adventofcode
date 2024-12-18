use std::fs;

use day17::{computer::Computer, part1, part2};
use rstest::rstest;

const TEST: &str = "Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0";

#[rstest]
#[case(0, 0)]
#[case(1, 1)]
#[case(4, 729)]
fn test_combo(#[case] input: i64, #[case] result: i64) {
    let c = Computer::new(TEST);
    assert_eq!(result, c.combo(input));
}
#[rstest]
#[case(0, 729)]
#[case(1, 364)]
#[case(2, 182)]
#[case(5, 729)]
fn test_adv(#[case] input: i64, #[case] result: i64) {
    let mut c = Computer::new(TEST);
    let res = c.adv(input);
    assert_eq!(&result, c.reg.get(&'A').unwrap());
    assert_eq!(result, res);
}

#[rstest]
#[case(0, 0)]
#[case(4, 1)]
#[case(5, 0)]
fn test_bst(#[case] input: i64, #[case] result: i64) {
    let mut c = Computer::new(TEST);
    let res = c.bst(input);
    assert_eq!(&result, c.reg.get(&'B').unwrap());
    assert_eq!(result, res);
}

#[rstest]
#[case(0, 7, 7)]
#[case(3, 7, 4)]
#[case(2, 7, 5)]
#[case(7, 17, 22)]
#[case(7, 22, 17)]
fn test_bxl(#[case] input: i64, #[case] reg_b: i64, #[case] result: i64) {
    let mut c = Computer::new(TEST);
    c.reg.insert('B', reg_b);
    let res = c.bxl(input);
    assert_eq!(
        &result,
        c.reg.get(&'B').unwrap(),
        "B {:b} -> {:b}",
        reg_b,
        result
    );
    assert_eq!(result, res);
}
#[rstest]
#[case(0, 0, 0)]
#[case(3, 3, 3)]
fn test_jnz(#[case] input: i64, #[case] ip: i32, #[case] result: i64) {
    let mut c = Computer::new(TEST);
    c.program[0] = 3;
    c.program[1] = input;
    let res = c.step();
    assert_eq!(ip, c.ip, "ip should be {}", ip);
    assert_eq!(result, res);
}
#[rstest]
#[case("Register C: 9\n\nProgram: 2,6", 0, 1, 9, vec![])]
#[case("Register A: 10\n\nProgram: 5,0,5,1,5,4", 10, 0, 0, vec![0,1,2])]
#[case("Register A: 2024\n\nProgram: 0,1,5,4,3,0", 0, 0, 0, vec![4,2,5,6,7,7,7,7,3,1,0])]
#[case("Register B: 29\n\nProgram: 1,7", 0, 26, 0, vec![])]
#[case("Register B: 2024\nRegister C: 43690\n\nProgram: 4,0", 0, 44354, 43690, vec![])]
fn test_step(
    #[case] input: &str,
    #[case] reg_a: i64,
    #[case] reg_b: i64,
    #[case] reg_c: i64,
    #[case] result: Vec<i64>,
) {
    let mut c = Computer::new(input);

    println!(
        "\nA:{}, B:{}, C:{}\n",
        c.reg.get(&'A').unwrap(),
        c.reg.get(&'B').unwrap(),
        c.reg.get(&'C').unwrap()
    );
    c.run();
    assert_eq!(result, c.output, "Output should be {:?}", result);
    assert_eq!(reg_a, *c.reg.get(&'A').unwrap(), "A should be {}", reg_a);
    assert_eq!(reg_b, *c.reg.get(&'B').unwrap(), "B should be {}", reg_b);
    assert_eq!(reg_c, *c.reg.get(&'C').unwrap(), "C should be {}", reg_c);
}

#[test]
fn test_new() {
    let c = Computer::new(TEST);
    assert_eq!(c.ip, 0);
    assert_eq!(c.reg.get(&'A').unwrap(), &729);
    assert_eq!(c.reg.get(&'B').unwrap(), &0);
    assert_eq!(c.reg.get(&'C').unwrap(), &0);
    assert_eq!(c.program.len(), 6);
    assert_eq!(c.program[0], 0);
    assert_eq!(c.program[1], 1);
    assert_eq!(c.program[2], 5);
    assert_eq!(c.program[3], 4);
    assert_eq!(c.program[4], 3);
    assert_eq!(c.program[5], 0);
}

#[rstest]
#[case(TEST, vec![4,6,3,5,6,3,5,2,1,0])]
fn test1(#[case] input: &str, #[case] result: Vec<usize>) {
    use day17::part1;
    let s = result
        .iter()
        .map(|x| x.to_string())
        .collect::<Vec<_>>()
        .join(",");

    assert_eq!(s, part1(input.to_string()));
}

// #[test]
// pub fn test_main() {
//     let path = "".to_string() + "../../data/day17.txt";
//     let input = match fs::read_to_string(&path) {
//         Ok(input) => input,
//         Err(e) => panic!("Error reading file: {}", e),
//     };
//     println!("{}", part1(input.clone()));
//     assert!(false)
// }

// 2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0
// 2 bst(4) -> A % 8
// 7 cdv(5) -> A/ 32 -> C
// 4 bxc(6) -> B ^ C -> B
// 0 adv(3) -> A / 8 -> A

// A : 111 00 000
//
#[rstest]
#[case(7, vec![0])]
#[case(0b111, vec![0])]
#[case(0b11111001, vec![2,4])]
fn test_backtrack(#[case] input: i64, #[case] result: Vec<i64>) {
    let mut initial = input;
    let path = "".to_string() + "../../data/day17.txt";
    let config = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    let mut c = Computer::new(&config);
    c.reg.insert('A', initial);
    c.run();
    let out: u128 = c
        .output
        .iter()
        .map(|p| p.to_string())
        .collect::<Vec<String>>()
        .join("")
        .parse()
        .unwrap();
    println!("\nCode: {} -> Initial: {}", out, initial);
    assert_eq!(result, c.output);
}

// #[test]
// pub fn test_run_to_copy() {
//     let path = "".to_string() + "../../data/day17.txt";
//     let input = match fs::read_to_string(&path) {
//         Ok(input) => input,
//         Err(e) => panic!("Error reading file: {}", e),
//     };
//     part2(input.clone());
//     assert!(false)
// }
