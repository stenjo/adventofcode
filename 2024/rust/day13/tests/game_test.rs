use rstest::rstest;

const FIRST_TEST: &str = "Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400";

const SECOND_TEST: &str = "Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176";

const THIRD_TEST: &str = "Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450";

const FULL_TEST: &str = "Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279";

const LAST_TEST: &str = "Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279";
#[rstest]
#[case::first(LAST_TEST, (69,23),(27,71),(18641,10279))]
fn test_new(
    #[case] input: &str,
    #[case] a: (i128, i128),
    #[case] b: (i128, i128),
    #[case] prize: (i128, i128),
) {
    use day13::game::Game;

    let game = Game::new(&input);

    assert_eq!(a, game.a);
    assert_eq!(b, game.b);
    assert_eq!(prize, game.prize);
}

#[rstest]
#[case(FIRST_TEST, 280)]
#[case(SECOND_TEST, 0)]
#[case(THIRD_TEST, 200)]
#[case(LAST_TEST, 0)]
fn test_tokens(#[case] input: &str, #[case] result: i128) {
    use day13::game::Game;

    let game = Game::new(&input);
    println!("A: {:?}", game.a_btn());
    println!("B: {:?}", game.b_btn());
    assert_eq!(result, game.tokens());
}

#[rstest]
#[case((69, 23), (69, 23), vec![1,1])]
#[case((69, 23), (18641, 10279), vec![])]
#[case((27, 71), (18641, 10279), vec![])]
fn test_presses(
    #[case] inc: (i128, i128),
    #[case] target: (i128, i128),
    #[case] result: Vec<i128>,
) {
    use day13::game::Game;

    let game = Game {
        a: (69, 23),
        b: (27, 71),
        prize: (18641, 10279),
    };

    assert_eq!(result, game.presses(inc, target));
}

#[test]
fn test_games() {
    let games = day13::game::games(FULL_TEST);

    assert_eq!(4, games.len());
    assert_eq!((94, 34), games[0].a);
    assert_eq!((22, 67), games[0].b);
    assert_eq!((8400, 5400), games[0].prize);

    assert_eq!((26, 66), games[1].a);
    assert_eq!((67, 21), games[1].b);
    assert_eq!((12748, 12176), games[1].prize);

    assert_eq!((17, 86), games[2].a);
    assert_eq!((84, 37), games[2].b);
    assert_eq!((7870, 6450), games[2].prize);

    assert_eq!((69, 23), games[3].a);
    assert_eq!((27, 71), games[3].b);
    assert_eq!((18641, 10279), games[3].prize);
}
