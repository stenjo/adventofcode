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

static TEST: &str = "111021\n1120\n11  11\n120312\n1 0  2\n    221";
static TEST2: &str = ".....\n    .\n.....\n..  .\n.. . \n ....";

#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5))]
fn test_grid(#[case] test: &str, #[case] min: Loc, #[case] max: Loc) {
    let mut lm = LocMap::new(test);
    assert_eq!(min, lm.min);
    assert_eq!(max, lm.max);
}

#[rstest]
#[case(TEST, Loc::new(0, 0), Loc::new(5, 5), 10)]
#[case(TEST2, Loc::new(0, 0), Loc::new(4, 5), 15)]
#[case(TEST2, Loc::new(0, 2), Loc::new(3, 4), 10)]
fn test_path(#[case] test: &str, #[case] start: Loc, #[case] end: Loc, #[case] length: usize) {
    let mut lm = LocMap::new(test);

    let path = lm.get_path(&start, &end);

    lm.visualize_cost(&path, '+');
    assert_eq!(length, path.len());
}
