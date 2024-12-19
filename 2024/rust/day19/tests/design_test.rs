use day19::design::Design;

const TEST: &str = "r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb";

#[test]
fn test_design() {
    let d = Design::new(TEST);
    assert_eq!(d.inventory.len(), 8);
    assert_eq!(d.designs.len(), 8);
}

#[test]
fn test_part1() {
    assert_eq!(day19::part1(TEST.to_string()), 6);
}
