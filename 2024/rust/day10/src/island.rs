#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Pos {
    loc: Coord,
    height: usize,
}
#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Coord {
    row: usize,
    col: usize,
}

impl Coord {
    pub fn new(row: usize, col: usize) -> Self {
        Self { row, col }
    }
    pub fn to_tuple(&self) -> (usize, usize) {
        (self.row, self.col)
    }
}

#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Island {
    pub map: Vec<Vec<usize>>,
}

impl Island {
    /// Constructs a new Area from the given input string
    pub fn new(input: String) -> Self {
        let map: Vec<Vec<usize>> = input
            .lines()
            .map(|line| {
                line.trim()
                    .chars()
                    .map(|c| c.to_string().parse().unwrap())
                    .collect::<Vec<usize>>()
            })
            .collect();

        Self { map }
    }

    /// Gets the height of the position at the given coordinates
    pub fn get_height(&self, loc: Coord) -> Option<usize> {
        if self.inbound(loc) {
            Some(self.map[loc.row][loc.col])
        } else {
            None
        }
    }

    /// Checks if a given position is within bounds
    fn inbound(&self, loc: Coord) -> bool {
        let (rows, cols) = (self.map.len(), self.map.get(0).map_or(0, |row| row.len()));
        loc.row < rows && loc.col < cols
    }

    /// Returns the next position based on the direction
    fn next_step(&self, loc: Coord, visited: &Vec<Coord>) -> Vec<Coord> {
        let directions = vec![(-1, 0), (1, 0), (0, -1), (0, 1)];
        let mut next_steps: Vec<Coord> = Vec::new();
        for i in directions.iter() {
            let next = Coord {
                row: (loc.row as isize + i.0) as usize,
                col: (loc.col as isize + i.1) as usize,
            };
            if !self.inbound(next) {
                continue;
            }
            let current_height = self.get_height(loc).unwrap();
            let mut heights: Vec<usize> = vec![current_height, current_height + 1];
            if current_height > 0 {
                heights.push(current_height - 1)
            };
            if let Some(height) = self.get_height(next) {
                if heights.contains(&height) && !visited.contains(&next) && height > 0 {
                    let t = next.to_tuple();
                    next_steps.push(next);
                }
            }
        }
        // print!("{:?}", next_steps);
        return next_steps;
    }

    pub fn get_starting_points(&self) -> Vec<Coord> {
        let mut starting_points: Vec<Coord> = Vec::new();
        for (i, row) in self.map.iter().enumerate() {
            for (col, height) in row.iter().enumerate() {
                if *height == 0 {
                    starting_points.push(Coord::new(i, col));
                }
            }
        }
        return starting_points;
    }

    pub fn walk(
        &mut self,
        loc: Coord,
        visited: &mut Vec<Coord>,
        trails: &mut Vec<Vec<Coord>>,
    ) -> Option<usize> {
        visited.push(loc);
        if self.get_height(loc) == Some(9) {
            trails.push(visited.clone());
            return Some(9);
        };
        for next in self.next_step(loc, visited) {
            if let Some(_result) = self.walk(next, visited, trails) {
            } else {
                visited.pop();
                return None;
            }
        }
        return self.get_height(loc);
    }
    pub fn print(&self, trail: &Vec<Coord>) {
        for (i, row) in self.map.iter().enumerate() {
            for (col, height) in row.iter().enumerate() {
                let loc = Coord::new(i, col);
                if trail.contains(&loc) {
                    print!("{}", height);
                } else {
                    print!(".");
                }
            }
            println!();
        }
    }
}
