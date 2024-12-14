use day14::*;
use restroom::Restroom;
use rstest::rstest;

const FULL: &str = "p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3";

const SINGLE: &str = "p=2,4 v=2,-3";

#[rstest]
#[case(FULL, 1, 12)]
#[case(FULL, 100, 12)]
fn safety_factor_test(#[case] input: &str, #[case] steps: u64, #[case] result: i64) {
    let mut restroom = Restroom::new(input, 11, 7);
    restroom.move_robots(steps);

    assert_eq!(result, restroom.safety_factor() as i64);
}

#[rstest]
#[case(SINGLE, 0, 2)] // 0: 0-4, 4-6
#[case(SINGLE, 1, 0)] // 0: 0-4, 0-2
#[case(SINGLE, 2, 3)] // none - in between
#[case(SINGLE, 3, 1)] // 1: 6-10, 0-2
#[case(SINGLE, 4, 3)] // 3: 6-10, 4-6
fn quadrant_test(#[case] input: &str, #[case] steps: u64, #[case] result: i64) {
    let mut restroom = Restroom::new(input, 11, 7);
    restroom.move_robots(steps);
    restroom.print();
    // assert_eq!(1, restroom.get_robots().len(), "testing number of Robots");
    for (idx, robots) in restroom.quadrants().into_iter().enumerate() {
        if robots.len() > 0 {
            assert_eq!(idx as i64, result);
        }
    }
}

#[rstest]
#[case(SINGLE, 0, (2,4))]
#[case(SINGLE, 1, (4,1))]
#[case(SINGLE, 2, (6,5))]
#[case(SINGLE, 3, (8,2))]
#[case(SINGLE, 4, (10,6))]
#[case(SINGLE, 5, (1,3))]
fn move_test(#[case] input: &str, #[case] steps: u64, #[case] result: (i64, i64)) {
    let mut restroom = Restroom::new(input, 11, 7);
    restroom.move_robots(steps);

    assert_eq!(result, restroom.get_robots()[0].p.as_tuple());
}
