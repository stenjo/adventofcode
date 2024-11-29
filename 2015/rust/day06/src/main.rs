use std::fs;

struct Pos {
    x: i64,
    y: i64,
}

impl Pos {
    fn new(x: i64, y: i64) -> Pos {
        Pos { x, y }
    }
    fn from_coords(coords: Vec<i64>) -> Pos {
        Pos {
            x: coords[0],
            y: coords[1],
        }
    }
}

struct Grid {
    width: i64,
    height: i64,
    grid: Vec<Vec<char>>,
}

impl Grid {
    fn new(width: i64, height: i64) -> Grid {
        Grid {
            width,
            height,
            grid: vec![vec!['.'; width as usize]; height as usize],
        }
    }

    fn get(&self, pos: Pos) -> char {
        return self.grid[pos.y as usize][pos.x as usize];
    }

    fn set(&mut self, pos: Pos, value: char) {
        self.grid[pos.y as usize][pos.x as usize] = value;
    }

    fn print(&self) {
        for row in &self.grid {
            for cell in row {
                print!("{}", cell);
            }
            println!();
        }
    }
}

pub fn parse_cmnd(cmnd: &str) -> (char, Pos, Pos) {
    let mut cmd: char;
    let mut from: Pos;
    let mut to: Pos;
    if cmnd.starts_with("turn on") {
        cmd = '1';
        let from = Pos::from_coords(
            cmnd.split(" ")
                .nth(2)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
    } else if cmnd.starts_with("turn off") {
        cmd = '0';
    } else if cmnd.starts_with("toggle") {
        cmd = 'T';
    }

    return (cmd, from, to);
}

#[cfg(test)]
mod tests_1 {
    use super::*;

    #[test]
    fn test_parse_cmnd() {
        assert_eq!(
            parse_cmnd("turn on 0,0 through 999,999"),
            ('1', Pos::new(0, 0), Pos::new(999, 999))
        );
        // assert_eq!(parse_cmnd("U62"), ('U', 62));
        // assert_eq!(parse_cmnd("L2"), ('L', 2));
        // assert_eq!(parse_cmnd("D99"), ('D', 99));
    }
}

pub fn part1(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first("data", 4)]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }
}

pub fn main() {
    let path = "../".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
