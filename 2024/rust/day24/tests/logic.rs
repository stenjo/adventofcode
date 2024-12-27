use day24::logic::Logic;
use rstest::rstest;

const TEST: &str = "x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02";

const LARGE: &str = "x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj";

const SWAPPED: &str = "x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00";

#[rstest]
#[case(LARGE, 3, 3)]
fn test_find_input(#[case] input: &str, #[case] bit: usize, #[case] result: i64) {
    let mut l = Logic::new(input);
    let z_0 = l.gates.get(format!("z{:02}", bit).as_str()).unwrap();

    l.find_input_x(bit, z_0);
    assert_eq!(result, l.number() as i64);
}

#[rstest]
#[case(LARGE, 2024)]
fn testrun_adder(#[case] input: &str, #[case] result: i64) {
    let mut l = Logic::new(input);
    l.run_adder(0);
    assert_eq!(result, l.number() as i64);
}

#[rstest]
#[case(TEST, 4)]
#[case(LARGE, 2024)]
fn test1(#[case] input: &str, #[case] result: i64) {
    let mut l = Logic::new(input);
    l.run();
    assert_eq!(result, l.number() as i64);
}

#[rstest]
#[case(TEST, 4)]
#[case(LARGE, 2024)]
fn test2(#[case] input: &str, #[case] result: i64) {
    let mut l = Logic::new(input);
    l.run();
    assert_eq!(result, l.swapped_gates() as i64);
}
