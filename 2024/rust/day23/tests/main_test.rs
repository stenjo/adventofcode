use assert_cmd::Command;
use day23::*;
use rstest::rstest;

const EXAMPLE: &str = "kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn";

#[rstest]
#[case::first(EXAMPLE, 7)]
fn test1(#[case] input: &str, #[case] result: i64) {
    assert_eq!(result, part1(input.to_string()));
}

const EXAMPLE2: &str = "ka-co
ta-co
de-co
ta-ka
de-ta
ka-de";

#[rstest]
#[case(EXAMPLE, "aq,cg,co,de,vc")]
#[case(EXAMPLE2, "co,de,ka,ta")]
fn test2(#[case] input: &str, #[case] result: &str) {
    assert_eq!(result, part2(input.to_string()).as_str());
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day23")
        .unwrap()
        .arg("../../data/day23.txt")
        .assert()
        .success()
        .stdout("1062\nbz,cs,fx,ms,oz,po,sy,uh,uv,vw,xu,zj,zm\n");
}
