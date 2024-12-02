use std::fs;

fn is_safe(input: String) -> bool {
    let levels: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("Invalid number"))
        .collect();
    if levels.len() < 2 {
        return false;
    }
    let mut direction: i32 = levels[1] - levels[0];
    if direction == 0 {
        return false;
    } else {
        direction /= direction.abs();
    }

    for idx in 1..levels.len() {
        let diff = levels[idx] - levels[idx - 1];
        let abs_diff = diff.abs();
        if diff.abs() == 0 {
            return false;
        } else if (diff / abs_diff) != direction {
            return false;
        }
        if abs_diff < 1 || abs_diff > 3 {
            return false;
        }
    }

    return true;
}

fn is_safe_dampened(input: String) -> bool {
    let levels: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse::<i32>().expect("Invalid number"))
        .collect();

    if levels.len() < 2 {
        return false;
    }

    let mut unsafe_level = get_unsafe_level(&levels);
    if unsafe_level == -1 {
        return true;
    }

    let dampened = {
        let mut temp = levels.clone();
        temp.remove(unsafe_level as usize);
        temp
    };

    unsafe_level = get_unsafe_level(&dampened);
    if unsafe_level == -1 {
        return true;
    }

    if unsafe_level > 0 {
        let dampened2 = {
            let mut temp = levels.clone();
            temp.remove((unsafe_level - 1) as usize);
            temp
        };

        unsafe_level = get_unsafe_level(&dampened2);
        if unsafe_level == -1 {
            return true;
        }
    }

    return false;
}

fn get_unsafe_level(levels: &Vec<i32>) -> i32 {
    let mut direction: i32 = levels[1] - levels[0];
    if direction == 0 {
        return 0;
    } else {
        direction /= direction.abs();
    }
    for idx in 1..levels.len() {
        let diff = levels[idx] - levels[idx - 1];
        let abs_diff = diff.abs();
        if diff.abs() == 0 {
            return idx as i32;
        } else if (diff / abs_diff) != direction {
            return idx as i32;
        }
        if abs_diff < 1 || abs_diff > 3 {
            return idx as i32;
        }
    }
    return -1;
}

pub fn part1(input: String) -> i64 {
    let mut safe_lines: i64 = 0;
    for line in input.lines() {
        if is_safe(line.to_owned()) {
            safe_lines += 1;
        }
    }
    return safe_lines;
}

pub fn part2(input: String) -> i64 {
    let mut safe_lines: i64 = 0;
    for line in input.lines() {
        if is_safe_dampened(line.to_owned()) {
            safe_lines += 1;
        }
    }
    return safe_lines;
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case("0 1 2 3 4", true)]
    #[case("", false)]
    #[case("4 3 2 1 0", true)]
    #[case("3 2 1 0 0", false)]
    #[case("7 6 4 2 1", true)]
    #[case("1 2 7 8 9", false)]
    #[case("9 7 6 2 1", false)]
    #[case("1 3 2 4 5", false)]
    #[case("8 6 4 4 1", false)]
    #[case("1 3 6 7 9", true)]
    fn test_safe(#[case] input: String, #[case] result: bool) {
        assert_eq!(result, is_safe(input))
    }
    #[rstest]
    #[case("7 6 4 2 1", true)]
    #[case("1 2 7 8 9", false)]
    #[case("9 7 6 2 1", false)]
    #[case("1 3 2 4 5", true)]
    #[case("8 6 4 4 1", true)]
    #[case("1 3 6 7 9", true)]
    fn test_dampened(#[case] input: String, #[case] result: bool) {
        assert_eq!(result, is_safe_dampened(input))
    }

    #[rstest]
    #[case::first(
        "7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9",
        2
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }
}

pub fn main() {
    let path = "../data/".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
