use std::fs;

#[derive(Debug, PartialEq)]
pub struct Pos {
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

pub struct Grid {
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
    fn on(&mut self, from: Pos, to: Pos) {
        for y in from.y..=to.y {
            for x in from.x..=to.x {
                self.set(Pos::new(x, y), '#');
            }
        }
    }
    fn off(&mut self, from: Pos, to: Pos) {
        for y in from.y..=to.y {
            for x in from.x..=to.x {
                self.set(Pos::new(x, y), '.');
            }
        }
    }
    fn toggle(&mut self, from: Pos, to: Pos) {
        for y in from.y..=to.y {
            for x in from.x..=to.x {
                if self.get(Pos::new(x, y)) == '#' {
                    self.set(Pos::new(x, y), '.');
                } else {
                    self.set(Pos::new(x, y), '#');
                }
            }
        }
    }
    fn count(&self) -> i64 {
        let mut count = 0;
        for row in &self.grid {
            for cell in row {
                if *cell == '#' {
                    count += 1;
                }
            }
        }
        return count;
    }
}

pub fn parse_cmnd(cmnd: &str) -> (char, Pos, Pos) {
    let cmd: char;
    let mut from: Pos = Pos::new(0, 0);
    let mut to: Pos = Pos::new(0, 0);
    if cmnd.starts_with("turn on") {
        cmd = '1';
        from = Pos::from_coords(
            cmnd.split(" ")
                .nth(2)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
        to = Pos::from_coords(
            cmnd.split(" ")
                .nth(4)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
    } else if cmnd.starts_with("turn off") {
        cmd = '0';
        from = Pos::from_coords(
            cmnd.split(" ")
                .nth(2)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
        to = Pos::from_coords(
            cmnd.split(" ")
                .nth(4)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
    } else if cmnd.starts_with("toggle") {
        from = Pos::from_coords(
            cmnd.split(" ")
                .nth(1)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
        to = Pos::from_coords(
            cmnd.split(" ")
                .nth(3)
                .unwrap()
                .split(",")
                .map(|s| s.parse().unwrap())
                .collect::<Vec<i64>>(),
        );
        cmd = 'T';
    } else {
        panic!("Invalid command");
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
        assert_eq!(
            parse_cmnd("toggle 0,0 through 999,0"),
            ('T', Pos::new(0, 0), Pos::new(999, 0))
        );
        assert_eq!(
            parse_cmnd("turn off 499,499 through 500,500"),
            ('0', Pos::new(499, 499), Pos::new(500, 500))
        );
    }
}

pub fn part1(input: String) -> i64 {
    let mut grid = Grid::new(1000, 1000);
    for line in input.lines() {
        let (cmd, from, to) = parse_cmnd(line);
        println!("{:?} {:?} {:?}", cmd, from, to);
        match cmd {
            '1' => grid.on(from, to),
            '0' => grid.off(from, to),
            'T' => grid.toggle(from, to),
            _ => panic!("Invalid command"),
        }
    }
    return grid.count();
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
