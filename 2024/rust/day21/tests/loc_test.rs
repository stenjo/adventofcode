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
#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5))]
fn test_grid(#[case] test: &str, #[case] min: Loc, #[case] max: Loc) {
    let mut lm = LocMap::new(test);
    assert_eq!(min, lm.min);
    assert_eq!(max, lm.max);
}

#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5), 11)]
#[case(TEST2, Loc::new(0, 0), Loc::new(4, 5), 18)]
#[case(TEST2, Loc::new(3, 4), Loc::new(0, 2), 8)]
#[case(KEYPAD1, Loc::new(2, 3), Loc::new(0, 0), 8)]
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
    let mut lm = LocMap::new(test);
    let begin = lm.get_char_loc(start);
    let end = lm.get_char_loc(stop);
    let directions = lm.get_directions(&begin, &end);

    assert_eq!(
        dirs,
        directions
            .into_iter()
            .map(|s| s.to_string())
            .collect::<String>()
    );
}
