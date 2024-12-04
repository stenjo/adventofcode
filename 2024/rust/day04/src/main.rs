use std::fs;

pub fn part1(input: String) -> i64 {
    let mut xword: Vec<Vec<char>> = Vec::new();
    for line in input.lines() {
        xword.push(line.chars().collect());
    }
    let mut count: i64 = 0;
    count += search_lines(xword.clone());
    count += search_lines(transpose(xword.clone()));
    let right_diags = diagonals(xword.clone(), 'r');
    count += search_lines(right_diags.clone());
    count += search_lines(transpose(right_diags.clone()));
    let left_diags = diagonals(xword.clone(), 'l');
    count += search_lines(left_diags.clone());
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

fn search_lines(xword: Vec<Vec<char>>) -> i64 {
    let mut count = 0;
    for i in 0..xword.len() {
        let line: String = xword[i].iter().collect();
        if line.contains("XMAS") {
            count += 1;
        }
        if xword[i].iter().rev().collect::<String>().contains("XMAS") {
            count += 1;
        }
    }
    return count;
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
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
    #[case(
        "A.
    .B",
        'r',
        ".A.
    .B."
    )]
    #[case(
        "A.
    .B",
        'l',
        "A..
    .B."
    )]
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

    // #[rstest]
    // #[case(vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['S', 'A', 'M', 'X'],
    //     vec!['G', 'H', 'A', '.'],
    //     vec!['G', 'H', 'S', '.'],

    // ],  'r',
    //  vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['A', 'M', 'X', '.'],
    //     vec!['A', '.', '.', '.'],
    //     vec!['.', '.', '.', '.'],
    // ])]
    // #[case(vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['S', 'A', 'M', 'X'],
    //     vec!['G', 'H', 'A', '.'],
    //     vec!['G', 'H', 'S', '.'],

    // ],  'l',
    //  vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['.', 'S', 'A', 'M'],
    //     vec!['.', '.', 'G', 'H'],
    //     vec!['.', '.', '.', 'G'],
    // ])]
    // #[case(
    //  vec![
    //     vec!['X', '.', '.', '.', '.'],
    //     vec!['.', 'M', '.', '.', '.'],
    //     vec!['.', '.', 'A', '.', '.'],
    //     vec!['.', '.', '.', 'S', '.'],
    // ], 'r',      vec![
    //     vec!['X', '.', '.', '.', '.'],
    //     vec!['M', '.', '.', '.', '.'],
    //     vec!['A', '.', '.', '.', '.'],
    //     vec!['S', '.', '.', '.', '.'],
    // ])]
    // #[case(
    //  vec![
    //     vec!['.', '.', '.', 'X', '.'],
    //     vec!['.', '.', 'M', '.', '.'],
    //     vec!['.', 'A', '.', '.','.'],
    //     vec!['S','.', '.', '.',  '.'],
    // ], 'l',      vec![
    //     vec!['X', '.', '.', '.', '.'],
    //     vec!['M', '.', '.', '.', '.'],
    //     vec!['A', '.', '.', '.', '.'],
    //     vec!['S', '.', '.', '.', '.'],
    // ])]
    // fn test_diagonals(
    //     #[case] xword: Vec<Vec<char>>,
    //     #[case] dir: char,
    //     #[case] result: Vec<Vec<char>>,
    // ) {
    //     assert_eq!(result, diagonals(xword, dir));
    // }

    // #[rstest]
    // #[case(transpose(vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['D', 'E', 'M', '.'],
    //     vec!['G', 'H', 'A', '.'],
    //     vec!['G', 'H', 'S', '.'],
    // ]), 1)]
    // #[case(vec![
    //     vec!['A', 'B', 'X', '.'],
    //     vec!['S', 'A', 'M', 'X'],
    //     vec!['G', 'H', 'A', '.'],
    //     vec!['G', 'H', 'S', '.'],
    // ], 0)]
    // fn test_search_lines(#[case] xword: Vec<Vec<char>>, #[case] result: i64) {
    //     assert_eq!(1, search_lines(xword));
    // }

    // #[test]
    // fn test_transpose() {
    //     let xword: Vec<Vec<char>> = vec![
    //         vec!['A', 'B', 'C'],
    //         vec!['D', 'E', 'F'],
    //         vec!['G', 'H', 'I'],
    //     ];
    //     let xword_transposed: Vec<Vec<char>> = vec![
    //         vec!['A', 'D', 'G'],
    //         vec!['B', 'E', 'H'],
    //         vec!['C', 'F', 'I'],
    //     ];
    //     assert_eq!(xword_transposed, transpose(xword));
    // }

    // #[test]
    // fn test_transpose_2() {
    //     let xword: Vec<Vec<char>> = vec![vec!['A', 'B', 'C'], vec!['D', 'E', 'F']];
    //     let xword_transposed: Vec<Vec<char>> = vec![vec!['A', 'D'], vec!['B', 'E'], vec!['C', 'F']];
    //     assert_eq!(xword_transposed, transpose(xword));
    // }

    //     #[rstest]
    //     #[case(
    //         "MMMSXXMASM
    //     MSAMXMSMSA
    //     AMXSXMAAMM
    //     MSAMASMSMX
    //     XMASAMXAMM
    //     XXAMMXXAMA
    //     SMSMSASXSS
    //     SAXAMASAAA
    //     MAMMMXMMMM
    //     MXMXAXMASX",
    //         18
    //     )]
    //     #[case(
    //         ".........X
    // .........M
    // .........A
    // .........S
    // .........A
    // .........M
    // .........X",
    //         2
    //     )]
    //     #[case(
    //         "....X
    // ....M
    // ....A
    // ....S",
    //         1
    //     )]
    //     #[case(
    //         "X....
    //         .M...
    //         ..A..
    //         ...S.",
    //         1
    //     )]
    //     fn test1(#[case] input: String, #[case] result: i64) {
    //         assert_eq!(result, part1(input));
    //     }
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
