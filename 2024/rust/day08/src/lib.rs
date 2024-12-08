use std::collections::HashSet;

#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Loc {
    row: isize,
    col: isize,
}
impl Loc {
    pub fn as_tuple(&self) -> (isize, isize) {
        (self.row, self.col)
    }
    pub fn new(row: isize, col: isize) -> Self {
        Self { row, col }
    }
}
#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Pos {
    pub loc: Loc,
    pub freq: char,
}

impl Pos {
    pub fn new(row: isize, col: isize, freq: char) -> Self {
        let loc = Loc { row: row, col: col };
        Self { freq, loc }
    }

    pub fn dist(&self, other: Pos) -> usize {
        let dx = (self.loc.row as isize - other.loc.row as isize).abs();
        let dy = (self.loc.col as isize - other.loc.col as isize).abs();
        dx.max(dy) as usize
    }
}

pub struct Area {
    map: Vec<Vec<Pos>>,
}

impl Area {
    /// Constructs a new Area from the given input string
    pub fn new(input: String) -> Self {
        let map: Vec<Vec<Pos>> = input
            .lines()
            .enumerate() // Enumerate to get the row index
            .map(|(row, line)| {
                line.chars()
                    .enumerate() // Enumerate to get the column index
                    .map(|(col, freq)| {
                        Pos::new(row.try_into().unwrap(), col.try_into().unwrap(), freq)
                    })
                    .collect()
            })
            .collect();

        Self { map }
    }

    pub fn get(&self, row: isize, col: isize) -> Option<&Pos> {
        let pos = Pos {
            loc: Loc { row, col },
            freq: '@',
        };
        if self.inbound(pos) {
            return Some(&self.map[row as usize][col as usize]);
        }
        return None;
    }

    /// Checks if a given position is within bounds
    fn inbound(&self, pos: Pos) -> bool {
        pos.loc.row >= 0
            && pos.loc.col >= 0
            && pos.loc.row < self.map.len() as isize
            && pos.loc.col < self.map[0].len() as isize
    }

    pub fn display(&self, other: HashSet<Loc>) {
        for row in &self.map {
            for pos in row {
                if other.contains(&pos.loc) {
                    print!("{}", '#')
                } else {
                    print!("{}", pos.freq);
                }
            }
            println!();
        }
    }

    fn gcd(&self, a: isize, b: isize) -> isize {
        if b == 0 {
            a.abs()
        } else {
            self.gcd(b, a % b)
        }
    }

    /// Finds positions along the diagonal from `p1` to `p2`
    pub fn get_diagonal(&self, p1: Pos, p2: Pos) -> Vec<Pos> {
        let mut positions: Vec<Pos> = Vec::new();
        if p1.loc == p2.loc {
            return positions;
        }

        // Calculate the direction vector
        let mut dr = p2.loc.row as isize - p1.loc.row as isize;
        let mut dc = p2.loc.col as isize - p1.loc.col as isize;

        // Normalize the direction vector
        let g = self.gcd(dr, dc);
        dr /= g;
        dc /= g;

        // Forward direction
        let mut current = p1;
        while self.inbound(current) {
            positions.push(current);
            current.loc.row += dr;
            current.loc.col += dc;
        }

        // Backward direction
        let mut current: Pos = p1;
        current.loc.row -= dr;
        current.loc.col -= dc;
        while self.inbound(current) {
            positions.push(current);
            current.loc.row -= dr;
            current.loc.col -= dc;
        }

        positions.sort();
        positions
    }

    fn get_antennas(&self) -> Vec<&Pos> {
        let antennas = self
            .map
            .iter()
            .flatten()
            .filter(|&a| a.freq != '.')
            .collect();
        return antennas;
    }

    pub fn antinodes(&self, current: &Pos, other: &Pos) -> Option<Loc> {
        if current.loc == other.loc {
            return None;
        }
        let distance = current.dist(*other); // Calculate distance between current and other
        let candidates = self.get_diagonal(*current, *other); // Find diagonal positions

        // Find the first valid antinode
        let antinode = candidates
            .iter()
            .find(|&p| current.dist(*p) == distance && p != other) // Check conditions
            .map(|&l| l.loc);

        return antinode;
    }
}

pub fn part1(input: String) -> i64 {
    let mut antinodes: HashSet<Loc> = HashSet::new();
    let area = Area::new(input);

    // Get all unique frequencies
    let frequency: HashSet<char> = area.get_antennas().iter().map(|p| p.freq).collect();

    for &freq in &frequency {
        // Get all positions with the same frequency
        let same_freq: Vec<&Pos> = area
            .get_antennas()
            .iter()
            .filter(|&p| p.freq == freq)
            .map(|s| *s)
            .collect();

        // Iterate over all unique pairs of positions
        for current in same_freq.clone() {
            for &other in same_freq.clone() {
                // Calculate and add antinodes
                if let Some(loc) = area.antinodes(&current, &other) {
                    antinodes.insert(loc.clone()); // Add all locations to the HashSet
                }
            }
        }
    }
    // area.display(antinodes.clone());

    return antinodes.len() as i64;
}

pub fn part2(input: String) -> i64 {
    let area = Area::new(input);
    let mut interference: HashSet<Loc> = HashSet::new();
    let frequency: HashSet<char> = area.get_antennas().iter().map(|p| p.freq).collect();

    for &freq in &frequency {
        // Get all positions with the same frequency
        let same_freq: Vec<&Pos> = area
            .get_antennas()
            .iter()
            .filter(|&p| p.freq == freq)
            .map(|s| *s)
            .collect();

        // Iterate over all unique pairs of positions
        for current in same_freq.clone() {
            for &other in same_freq.clone() {
                let diagonal = area.get_diagonal(*current, other);

                if diagonal.contains(current) && diagonal.contains(&other) {
                    for p in diagonal {
                        interference.insert(p.loc);
                    }
                }
            }
        }
    }
    return interference.len() as i64;
}
