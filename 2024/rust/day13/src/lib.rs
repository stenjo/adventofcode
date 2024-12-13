pub mod game;
pub fn part1(input: String) -> i128 {
    let games = game::games(&input);
    let mut tokens = 0;
    for game in games {
        tokens += game.tokens()
    }
    return tokens;
}

pub fn part2(input: String) -> i128 {
    let games = game::games(&input);
    let mut tokens = 0;
    for mut game in games {
        game.seed(10000000000000);
        tokens += game.tokens()
    }
    return tokens;
}
