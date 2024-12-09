#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Pos {
    row: usize,
    col: usize,
    dir: Direction,
}

#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

pub struct Area {
    map: Vec<Vec<char>>,
    guard: Pos,
}

impl Area {
    /// Constructs a new Area from the given input string
    pub fn new(input: String) -> Self {
        let map: Vec<Vec<char>> = input.lines().map(|line| line.chars().collect()).collect();
        let mut guard = Pos {
            row: 0,
            col: 0,
            dir: Direction::Up,
        };

        // Find the initial guard position (`^`) in the map
        for (i, row) in map.iter().enumerate() {
            for (j, &cell) in row.iter().enumerate() {
                if cell == '^' {
                    guard = Pos {
                        row: i,
                        col: j,
                        dir: Direction::Up,
                    };
                }
            }
        }

        Self { map, guard }
    }

    /// Checks if a given position is within bounds
    fn inbound(&self, pos: Pos) -> bool {
        pos.row < self.map.len() && pos.col < self.map[0].len()
    }

    /// Returns the next position based on the direction
    fn next_pos(&self, pos: Pos) -> Pos {
        let (delta_row, delta_col) = match pos.dir {
            Direction::Up => (-1, 0),
            Direction::Down => (1, 0),
            Direction::Left => (0, -1),
            Direction::Right => (0, 1),
        };

        Pos {
            row: (pos.row as isize + delta_row) as usize,
            col: (pos.col as isize + delta_col) as usize,
            dir: pos.dir,
        }
    }

    /// Turns the guard to the right
    fn turn(&self, pos: Pos) -> Pos {
        let new_dir = match pos.dir {
            Direction::Up => Direction::Right,
            Direction::Right => Direction::Down,
            Direction::Down => Direction::Left,
            Direction::Left => Direction::Up,
        };

        Pos {
            row: pos.row,
            col: pos.col,
            dir: new_dir,
        }
    }

    /// Steps the guard to the next valid position or returns `None` if out of bounds
    fn step(&self, pos: Pos) -> Option<Pos> {
        let mut current_pos = pos;

        loop {
            let next = self.next_pos(current_pos);

            if !self.inbound(next) {
                return None; // Out of bounds
            } else if self.map[next.row][next.col] == '.' {
                current_pos = self.turn(current_pos); // Turn right
            } else {
                return Some(next); // Valid next step
            }
        }
    }

    /// Moves the guard and returns the path taken
    pub fn walk(&mut self) -> Vec<Pos> {
        let mut path = Vec::new();
        let mut current_pos = self.guard;

        while let Some(next_pos) = self.step(current_pos) {
            path.push(next_pos);
            current_pos = next_pos;
        }

        path
    }
}
