use std::{collections::HashSet, fs};

pub fn part1(input: String) -> i64 {
    let mut x:i64 = 0;
    let mut y:i64 = 0;
    let tup: (i64, i64) = (x,y);
    let mut houses  = HashSet::new();
    houses.insert(tup);
    for c in input.chars() {
        match c {
            '>' => x += 1,
            '<' => x -= 1,
            'v' => y += 1, 
            '^' => y -= 1, 
            _ => ()
        }
        houses.insert((x,y));
    }
    return houses.len().try_into().unwrap()
}

pub fn part2(input:String) -> usize {
    return input.len()
}

pub fn main() {
    let path = "../".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match 
    fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::*;

    #[rstest]
    #[case::first(">", 2)]
    #[case::right_down(">v", 3)]
    #[case::right_left("><", 2)]
    #[case::right_down_left(">v<", 4)]
    #[case::up_right_down_left("^>v<", 4)]
    #[case::bunch("^v^v^v^v^v", 2)]
    fn it_works(#[case] input: String, #[case]result : i64) {
        assert_eq!(result, part1(input));
    }
}
