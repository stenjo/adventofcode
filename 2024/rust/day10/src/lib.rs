use island::Island;

pub mod island;

pub fn part1(input: String) -> i64 {
    let mut island = Island::new(input);
    let starts = island.get_starting_points();
    let mut scores = 0;
    for s in starts {
        let mut visited = Vec::new();
        let mut trails = Vec::new();

        island.walk(s, &mut visited, &mut trails);

        scores += trails.len() as i64;
    }
    scores
}

pub fn part2(input: String) -> i64 {
    let mut island = Island::new(input);
    let starts = island.get_starting_points();
    let mut scores = 0;
    for s in starts {
        let mut visited = Vec::new();
        let mut trails = Vec::new();

        island.rating(s, &mut visited, &mut trails);

        scores += trails.len() as i64;
    }
    scores
}
