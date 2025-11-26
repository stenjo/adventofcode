use day21::loc::Loc;
use day21::loc::LocMap;
use rstest::rstest;

#[rstest]
#[case(Loc::new(1, 1), Loc::new(1, 0), Loc::new(2, 1))]
#[case(Loc::new(1, 1), Loc::new(2, 0), Loc::new(3, 1))]
#[case(Loc::new(1, 1), Loc::new(3, 0), Loc::new(1, 1))]
#[case(Loc::new(1, 1), Loc::new(0, 3), Loc::new(1, 1))]
#[case(Loc::new(1, -1), Loc::new(0, 3), Loc::new(1, 2))]
fn test1(#[case] mut loc: Loc, #[case] v: Loc, #[case] result: Loc) {
    let min = Loc::new(1, 1);
    let max = Loc::new(3, 3);
    loc.add_teleport(&v, &min, &max);
    assert_eq!(result, loc);
}

static TEST: &str = "111021\n1120\n11  11\n120312\n1 0  2\n    22";
static TEST2: &str = ".....\n    .\n.....\n..  .\n.  . \n.....";
const KEYPAD1: &str = "789\n456\n123\n 0A";
const KEYPAD2: &str = " ^A\n<v>";

#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5))]
fn test_grid(#[case] test: &str, #[case] min: Loc, #[case] max: Loc) {
    let lm = LocMap::new(test);
    assert_eq!(min, lm.min);
    assert_eq!(max, lm.max);
}

#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5), 11)]
#[case(TEST2, Loc::new(0, 0), Loc::new(4, 5), 18)]
#[case(TEST2, Loc::new(3, 4), Loc::new(0, 2), 8)]
#[case(KEYPAD1, Loc::new(2, 3), Loc::new(0, 0), 6)]
#[case(KEYPAD2, Loc::new(2, 1), Loc::new(2, 0), 2)]
fn test_path(#[case] test: &str, #[case] start: Loc, #[case] end: Loc, #[case] length: usize) {
    let mut lm = LocMap::new(test);

    let path = lm.get_path(&start, &end);

    lm.visualize_cost(&path, '+');
    println!();
    for l in &path {
        println!("{:?}", l.as_tuple());
    }
    println!();
    lm.visualize(&path, '+');
    assert_eq!(length, path.len());
}

#[rstest]
#[case(KEYPAD1, 'A', '0', "<")]
#[case(KEYPAD1, 'A', '7', "<^^<^")]
fn test_directions(
    #[case] test: &str,
    #[case] start: char,
    #[case] stop: char,
    #[case] dirs: &str,
) {
    use std::collections::HashMap;

    let mut lm = LocMap::new(test);
    lm.current = lm.get_loc(start);
    let (_, path) = lm.dijkstra_pri(stop);
    println!("{:?}", path.iter().collect::<String>());
    let mut d1: HashMap<char, i32> = HashMap::new();
    let mut d2: HashMap<char, i32> = HashMap::new();
    for &c in path.iter() {
        let count = d1.entry(c).or_insert(0);
        *count += 1;
    }
    for c in dirs.chars() {
        let count = d2.entry(c).or_insert(0);
        *count += 1;
    }
    assert_eq!(d2, d1);
}

#[rstest]
#[case(KEYPAD1, "029A", "<A^A^>^AvvvA")]
#[case(KEYPAD1, "179A", "<^<A^^A>>AvvvA")]
#[case(KEYPAD2, "^<<A^^A>>AvvvA", "<Av<AA>>^A<AA>AvAA^A<vAAA>^A")]
#[case(
    KEYPAD2,
    "v<<A>^Av<A>>^A<AA>AvAA^Av<AAA>^A",
    "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
)]
#[case(KEYPAD1, "980A", "^^^A<AvvvA>A")]
#[case(KEYPAD2, "^^^A<AvvvA>A", "<AAA>A<v<A>^>A<vAAA^>AvA^A")]
#[case(
    KEYPAD2,
    "<AAA>Av<<A>>^A<vAAA>^AvA^A",
    "<v<A>^>AAAvA^A<vA<AA>^>AvAA<^A>A<v<A>A^>AAAvA<^A>A<vA^>A<A>A"
)]
// #[case(KEYPAD2, "v<<A>^Av<A>>^A", "v<A<AA>>^AvA<^A>Av<A<A>>^AvAA<^A>A")]
// #[case(KEYPAD2, "v<<A", "v<A<AA>>^A")]
// #[case(KEYPAD2, "<vA<AA>>^A", "<v<A>>^A<vA<A>>^AAvAA<^A>A")]
fn test_directions_to(#[case] pad: &str, #[case] seq: &str, #[case] dirs: &str) {
    let mut lm = LocMap::new(pad);

    let mut path = Vec::new();
    lm.current = lm.get_loc('A');

    for c in seq.chars() {
        let (_, keys) = lm.dijkstra_pri(c);
        path.extend(keys);
        path.push('A');
    }
    lm.visualize_cost(&Vec::new(), '.');
    println!(
        "{:?}",
        lm.convert(&dirs.chars().collect())
            .iter()
            .collect::<String>()
    );
    println!("{:?}", lm.convert(&path).iter().collect::<String>());
    let back: Vec<char> = path.iter().cloned().collect();
    println!("{:?}", lm.convert(&back).iter().collect::<String>());
    assert_eq!(dirs, path.iter().collect::<String>());
}

#[rstest]
#[case(KEYPAD1, "<A^A>^^AvvvA", "029A")]
#[case(KEYPAD1, "<^<A^^A>>AvvvA", "179A")]
#[case(KEYPAD2, "v<<A>^Av<A>>^A<AA>AvAA^Av<AAA>^A", "<^<A^^A>>AvvvA")]
#[case(
    KEYPAD2,
    "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    "<Av<AA>>^A<AA>AvAA^A<vAAA>^A"
)]
#[case(KEYPAD1, "^<<A^^A>>AvvvA", "179A")]
fn test_convert(#[case] pad: &str, #[case] seq: &str, #[case] dirs: &str) {
    let lm = LocMap::new(pad);
    let sequence: Vec<char> = seq.chars().collect();
    let keys: Vec<char> = lm.convert(&sequence);
    assert_eq!(dirs, keys.iter().collect::<String>());
}

#[rstest]
#[case(KEYPAD1, "029A", 12)]
fn test_dijkstra(#[case] pad: &str, #[case] seq: &str, #[case] length: i32) {
    let mut lm = LocMap::new(pad);

    let mut len = 0;

    for c in seq.chars() {
        let (l, _) = lm.dijkstra_pri(c);
        len += l + 1;
    }
    assert_eq!(length, len);
}
