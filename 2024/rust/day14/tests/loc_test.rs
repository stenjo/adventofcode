use day14::loc::Loc;
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
