use day04::*;
use grid::*;
use std::fs;

pub fn _part1(input: String) -> i64 {
    let mut x: Vec<Vec<char>> = Vec::new();
    for line in input.lines() {
        let mut range: Vec<char> = line.trim().chars().collect();
        range.insert(0, '.');
        range.push('.');
        x.push(range.clone());
    }
    let dots: Vec<char> = ".".repeat(x[0].len()).chars().collect();
    x.insert(0, dots.clone());
    x.push(dots.clone());

    let mut count: i64 = 0;
    count += search_lines(&x);
    count += search_lines(&transpose(x.clone()));
    count += search_lines(&transpose(diagonals(x.clone(), 'r')));
    count += search_lines(&transpose(diagonals(x.clone(), 'l')));

    return count;
}

fn transpose(xword: Vec<Vec<char>>) -> Vec<Vec<char>> {
    let mut xword_transposed: Vec<Vec<char>> = Vec::new();
    for i in 0..xword[0].len() {
        let mut row: Vec<char> = Vec::new();
        for j in 0..xword.len() {
            row.push(xword[j][i]);
        }
        xword_transposed.push(row);
    }
    return xword_transposed;
}

fn diagonals(xword: Vec<Vec<char>>, dir: char) -> Vec<Vec<char>> {
    let mut xword_diagonals: Vec<Vec<char>> = Vec::new();
    for i in 0..xword.len() {
        let mut row: Vec<char> = Vec::new();
        if dir == 'r' {
            for _n in i..(xword.len() - 1) {
                row.push('.');
            }
        }
        if dir == 'l' {
            for _n in 0..i {
                row.push('.');
            }
        }
        for j in 0..xword[i].len() {
            row.push(xword[i][j]);
        }
        if dir == 'r' {
            for _n in 0..i {
                row.push('.');
            }
        }
        if dir == 'l' {
            for _n in i..(xword.len() - 1) {
                row.push('.');
            }
        }
        xword_diagonals.push(row);
    }
    return xword_diagonals;
}

pub fn part1(input: String) -> i64 {
    let mut grid: Grid<char> = Grid::new(0, 0);
    let lines = input.lines();

    for line in lines {
        let mut range: Vec<char> = line.trim().chars().collect();
        range.insert(0, '.');
        range.push('.');
        grid.push_row(range.clone());
    }
    let dots: Vec<char> = ".".repeat(grid.cols()).chars().collect();
    grid.insert_row(0, dots.clone());
    grid.push_row(dots.clone());

    let mut count: i64 = 0;
    for x in 1..grid.rows() as i32 - 1 {
        for y in 1..grid.cols() as i32 - 1 {
            let c = grid.get(x, y).unwrap();
            if *c == 'A' {
                let surrounding: Vec<(i32, i32)> = vec![(1, 1), (1, 0), (0, 1), (-1, 1)];
                for p in surrounding {
                    let nx0 = p.0 * 2 + x as i32;
                    let ny0 = p.1 * 2 + y as i32;
                    let nx1 = p.0 + x as i32;
                    let ny1 = p.1 + y as i32;
                    let nx2 = -p.0 + x as i32;
                    let ny2 = -p.1 + y as i32;
                    let nx3 = -p.0 * 2 + x as i32;
                    let ny3 = -p.1 * 2 + y as i32;

                    // Boundary check
                    if bound_check(nx0, ny0, &grid)
                        && bound_check(nx1, ny1, &grid)
                        && bound_check(nx2, ny2, &grid)
                        && bound_check(nx3, ny3, &grid)
                    {
                        let word = format!(
                            "{}{}{}{}{}",
                            grid[(nx0 as usize, ny0 as usize)],
                            grid[(nx1 as usize, ny1 as usize)],
                            c,
                            grid[(nx2 as usize, ny2 as usize)],
                            grid[(nx3 as usize, ny3 as usize)]
                        );

                        if word.contains("XMAS") || word.contains("SAMX") {
                            count += 1;
                        }
                    }
                }
            }
        }
    }

    return count as i64;
}

fn bound_check(nx1: i32, ny1: i32, grid: &Grid<char>) -> bool {
    nx1 >= 0 && ny1 >= 0 && nx1 < grid.cols() as i32 && ny1 < grid.rows() as i32
}
pub fn part2(input: String) -> i64 {
    let mut grid: Grid<char> = Grid::new(0, 0);
    for line in input.lines() {
        let range = line.trim().chars().collect();
        grid.push_row(range);
    }

    let mut count: i64 = 0;
    for x in 1..grid.rows() as i32 - 1 {
        for y in 1..grid.cols() as i32 - 1 {
            let c = grid.get(x, y).unwrap();
            let surrounding: Vec<(i32, i32)> = vec![(1, 1), (-1, 1)];
            let mut words: i32 = 0;
            for p in surrounding {
                let nx1 = p.0 + x as i32;
                let ny1 = p.1 + y as i32;
                let nx2 = -p.0 + x as i32;
                let ny2 = -p.1 + y as i32;

                // Boundary check
                if nx1 >= 0
                    && ny1 >= 0
                    && nx1 < grid.cols() as i32
                    && ny1 < grid.rows() as i32
                    && nx2 >= 0
                    && ny2 >= 0
                    && nx2 < grid.cols() as i32
                    && ny2 < grid.rows() as i32
                {
                    let word = format!(
                        "{}{}{}",
                        grid[(nx1 as usize, ny1 as usize)],
                        c,
                        grid[(nx2 as usize, ny2 as usize)]
                    );

                    if word.contains("MAS") || word.contains("SAM") {
                        words += 1;
                    }
                }
            }
            if words > 1 {
                count += 1;
            }
        }
    }

    return count as i64;
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("A", 'r', "A")]
    #[case("A", 'l', "A")]
    #[case(".A", 'r', ".A")]
    #[case(".A", 'l', ".A")]
    #[case("A.", 'r', "A.")]
    #[case("A.", 'l', "A.")]
    #[case("A.\n.B", 'r', ".A.\n.B.")]
    #[case(".A\nB.\n.X", 'l', ".A..\n.B..\n...X")]
    fn test_diag(#[case] input: String, #[case] dir: char, #[case] out: String) {
        let mut xword: Vec<Vec<char>> = Vec::new();
        for line in input.lines() {
            xword.push(line.chars().collect());
        }
        let diagonal = diagonals(xword, dir);
        let output: String = diagonal
            .iter()
            .map(|line| line.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join("\n");
        assert_eq!(out, output);
    }

    #[rstest]
    #[case(vec![
        vec!['A', 'B', 'X', '.'],
        vec!['S', 'A', 'M', 'X'],
        vec!['G', 'H', 'A', '.'],
        vec!['G', 'H', 'S', '.'],

    ],  'l',
     vec![
        vec!['A', 'B', 'X', '.','.', '.', '.' ],
        vec!['.', 'S', 'A', 'M','X', '.', '.' ],
        vec!['.', '.', 'G', 'H','A', '.', '.' ],
        vec!['.', '.', '.', 'G','H', 'S', '.' ],
    ])]
    #[case(
     vec![
        vec!['X', '.', '.', '.', '.'],
        vec!['.', 'M', '.', '.', '.'],
        vec!['.', '.', 'A', '.', '.'],
        vec!['.', '.', '.', 'S', '.'],
    ], 'r',      vec![
        vec!['.', '.', '.', 'X', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'M', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'A', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'S', '.', '.', '.', '.'],
    ])]
    #[case(
     vec![
        vec!['.', '.', '.', 'X', '.'],
        vec!['.', '.', 'M', '.', '.'],
        vec!['.', 'A', '.', '.','.'],
        vec!['S','.', '.', '.',  '.'],
    ], 'l',      vec![
        vec!['.', '.', '.', 'X', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'M', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'A', '.', '.', '.', '.'],
        vec!['.', '.', '.', 'S', '.', '.', '.', '.'],
    ])]
    fn test_diagonals(
        #[case] xword: Vec<Vec<char>>,
        #[case] dir: char,
        #[case] result: Vec<Vec<char>>,
    ) {
        assert_eq!(result, diagonals(xword, dir));
    }

    #[rstest]
    #[case(
        "MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX",
        18
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }

    #[rstest]
    #[case(
        "MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX",
        9
    )]
    fn test2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}

pub fn main() {
    let path = "".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
