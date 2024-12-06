use std::collections::HashSet;

pub fn part1(input: String) -> i64 {
    let labmap = get_map(&input);
    let guard = get_guard(input.clone());
    let dir = get_dir(input);

    let path = walk(guard, dir, labmap);
    let visited = path.iter().map(|p| (p.0, p.1)).collect::<HashSet<_>>();
    return visited.len() as i64;
}

pub fn get_dir(input: String) -> usize {
    let dir = match input
        .clone()
        .chars()
        .find(|&c| !['.', '#', '\n'].contains(&c))
        .unwrap()
    {
        '^' => 0,
        '>' => 1,
        'v' => 2,
        '<' => 3,
        _ => 0,
    };
    dir
}

pub fn get_map(input: &String) -> Vec<Vec<bool>> {
    let labmap: Vec<Vec<bool>> = {
        input
            .lines()
            .map(|line| line.chars().map(|c| c == '#').collect())
            .collect()
    };
    labmap
}

pub fn walk(
    guard: (usize, usize),
    mut dir: usize,
    labmap: Vec<Vec<bool>>,
) -> Vec<(i32, i32, usize)> {
    let mut pos: (i32, i32) = (guard.0 as i32, guard.1 as i32);
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    let mut path: Vec<(i32, i32, usize)> = Vec::new();
    visited.insert(pos);
    loop {
        if is_out_of_bounds(pos, dir, labmap.len(), labmap[0].len()) {
            break;
        }
        // let next_pos = (pos.0 + directions[dir].0, pos.1 + directions[dir].1);
        let next_pos = {
            let p = get_next_pos((pos.0, pos.1, dir), dir);
            (p.0, p.1)
        };
        if labmap[next_pos.0 as usize][next_pos.1 as usize] {
            dir = (dir + 1) % 4;
            continue;
        } else {
            pos = next_pos;
            visited.insert(pos);
            path.push((pos.0, pos.1, dir));
        }
    }
    path
}

fn is_out_of_bounds(pos: (i32, i32), dir: usize, rows: usize, cols: usize) -> bool {
    let next = get_next_pos((pos.0, pos.1, dir), dir);
    next.0 < 0 || next.0 >= rows as i32 || next.1 < 0 || next.1 >= cols as i32
}

pub fn find_obstacle_options(
    guard: (usize, usize),
    dir: usize,
    labmap: Vec<Vec<bool>>,
) -> Vec<(i32, i32, usize)> {
    let visited: Vec<(i32, i32, usize)> = walk(guard, dir, labmap);
    let mut options: Vec<(i32, i32, usize)> = Vec::new();

    for (row, col, dir) in visited.iter() {
        let next_pos = get_next_pos((*row, *col, (*dir + 1) % 4), *dir);
        if visited.contains(&next_pos) {
            options.push(get_next_pos(next_pos, *dir));
        }
    }
    return options;
}

fn get_next_pos(pos: (i32, i32, usize), dir: usize) -> (i32, i32, usize) {
    let directions: Vec<(i32, i32)> = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];
    let next_pos = (pos.0 + directions[dir].0, pos.1 + directions[dir].1, pos.2);
    next_pos
}

pub fn get_guard(input: String) -> (usize, usize) {
    let map = input
        .lines()
        .map(|line| line.chars().map(|c| c == '^').collect::<Vec<bool>>());
    for (i, row) in map.enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell {
                return (i, j);
            }
        }
    }
    return (0, 0);
}

pub fn part2(input: String) -> i64 {
    let labmap = get_map(&input);
    let guard = get_guard(input.clone());
    let dir = get_dir(input);

    let options = find_obstacle_options(guard, dir, labmap);
    return options.len() as i64;
}
