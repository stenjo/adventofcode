use once_cell::sync::Lazy;
use std::collections::{HashMap, VecDeque};

#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Loc {
    pub x: i64,
    pub y: i64,
}
impl Loc {
    pub fn new(x: i64, y: i64) -> Self {
        Self { x, y }
    }
    pub fn new_from_tuple(p: (i64, i64)) -> Self {
        Self { x: p.0, y: p.1 }
    }

    pub fn update(&mut self, p: (i64, i64)) -> Loc {
        self.x = p.0;
        self.y = p.1;
        return self.clone();
    }

    pub fn up(&mut self) -> Loc {
        self.y -= 1;
        return self.clone();
    }

    pub fn down(&mut self) -> Loc {
        self.y += 1;
        return self.clone();
    }

    pub fn left(&mut self) -> Loc {
        self.x -= 1;
        return self.clone();
    }

    pub fn right(&mut self) -> Loc {
        self.x += 1;
        return self.clone();
    }

    pub fn as_tuple(&self) -> (i64, i64) {
        (self.x, self.y)
    }

    pub(crate) fn add(&mut self, v: &Loc) -> Loc {
        self.x += v.x;
        self.y += v.y;
        self.clone()
    }

    pub fn add_teleport(&mut self, v: &Loc, min: &Loc, max: &Loc) -> Loc {
        let width: i64 = max.x - min.x + 1;
        let height: i64 = max.y - min.y + 1;
        self.add(v);
        self.x = (self.x - min.x) % width + min.x;
        if self.x < min.x {
            self.x += width;
        }
        self.y = (self.y - min.y) % height + min.y;
        if self.y < min.y {
            self.y += height;
        }
        self.clone()
    }

    pub fn get_next(&self, dir: char) -> Loc {
        return self.clone().add(DIRECTION.get(&dir).unwrap());
    }

    pub fn is_neighbor(&self, other: &Loc) -> bool {
        ((other.x - self.x).abs() == 1 && other.y == self.y)
            || ((other.y - self.y).abs() == 1 && other.x == self.x)
    }
    pub const DIRECTIONS: [char; 4] = ['>', 'v', '<', '^'];
}

pub struct LocMap {
    pub map: HashMap<Loc, char>,
    pub cost: HashMap<Loc, i32>,
    pub min: Loc,
    pub max: Loc,
}

impl LocMap {
    pub fn new(input: &str) -> Self {
        let mut map: HashMap<Loc, char> = HashMap::new();
        let mut min = Loc::new(0, 0);
        let mut max = Loc::new(0, 0);
        for (y, ln) in input.lines().enumerate() {
            for (x, c) in ln.chars().enumerate() {
                if c != ' ' {
                    let loc = Loc::new(x as i64, y as i64);
                    map.insert(loc.clone(), c);
                    if loc.x < min.x {
                        min.x = loc.x;
                    }
                    if loc.y < min.y {
                        min.y = loc.y;
                    }
                    if loc.x > max.x {
                        max.x = loc.x;
                    }
                    if loc.y > max.y {
                        max.y = loc.y;
                    }
                }
            }
        }

        Self {
            map,
            cost: HashMap::new(),
            min,
            max,
        }
    }

    pub fn insert(&mut self, loc: Loc, c: char) {
        self.map.insert(loc.clone(), c);
        if loc.x < self.min.x {
            self.min.x = loc.x;
        }
        if loc.y < self.min.y {
            self.min.y = loc.y;
        }
        if loc.x > self.max.x {
            self.max.x = loc.x;
        }
        if loc.y > self.max.y {
            self.max.y = loc.y;
        }
    }

    pub fn get(&self, loc: &Loc) -> char {
        match self.map.get(loc) {
            Some(c) => *c,
            None => ' ',
        }
    }
    pub fn get_cost_option(&self, loc: &Loc) -> Option<&i32> {
        return self.cost.get(loc);
    }

    pub fn get_option(&self, loc: &Loc) -> Option<char> {
        return self.map.get(loc).cloned();
    }

    pub fn get_next(&self, loc: &Loc, dir: char) -> char {
        self.get(&loc.get_next(dir))
    }

    pub fn get_path(&mut self, start: &Loc, end: &Loc) -> Vec<Loc> {
        let mut path = vec![];
        let mut visited: HashMap<Loc, i32> = HashMap::new();
        let mut queue: VecDeque<(Loc, i32)> = VecDeque::new();
        let mut loc = start.clone();
        let mut cost = 0;
        visited.insert(loc.clone(), cost);
        self.cost.insert(loc.clone(), cost);
        while queue.len() > 0 || loc != *end {
            for dir in Loc::DIRECTIONS.iter() {
                let next_loc = loc.get_next(*dir);
                if let Some(next) = self.get_option(&next_loc) {
                    if next == ' ' {
                        visited.insert(next_loc.clone(), i32::MAX);
                        continue;
                    }
                    if visited.contains_key(&next_loc) {
                        if visited[&next_loc] > cost + 1 {
                            if let Some(v) = visited.get_mut(&next_loc) {
                                *v = cost + 1;
                            }
                        }
                        continue;
                    }
                    queue.push_back((next_loc.clone(), cost + 1));
                    visited.insert(next_loc.clone(), cost + 1);
                }
            }
            let (node, node_cost) = match queue.pop_front() {
                Some((node, node_cost)) => (node, node_cost),
                None => break,
            };
            cost = node_cost;
            loc = node;
            self.cost.insert(loc.clone(), cost);
        }
        cost = *self.cost.get(&end).unwrap();
        while cost > 0 {
            cost -= 1;
            if let Some((l, c)) = self
                .cost
                .iter()
                .find(|(&l, v)| loc.is_neighbor(&l) && **v == cost)
            {
                loc = l.clone();
                path.push(loc.clone());
            }
        }
        path
    }

    pub fn visualize(&self, path: &Vec<Loc>, c: char) {
        for y in self.min.y..self.max.y + 1 {
            for x in self.min.x..self.max.x + 1 {
                let l = Loc::new(x, y);
                if path.contains(&l) {
                    print!("{}", c);
                } else {
                    print!("{}", self.get(&l));
                }
            }
            println!();
        }
    }

    pub fn visualize_cost(&self, path: &Vec<Loc>, c: char) {
        for y in self.min.y..self.max.y + 1 {
            for x in self.min.x..self.max.x + 1 {
                let l = Loc::new(x, y);
                if path.contains(&l) {
                    print!("  {}", c);
                } else {
                    if let Some(cost) = self.get_cost_option(&l) {
                        print!(" {:2}", cost % 100);
                    } else {
                        print!("   ");
                    }
                }
            }
            println!();
        }
    }
}
pub static DIRECTION: Lazy<HashMap<char, Loc>> = Lazy::new(|| {
    let mut map = HashMap::new();
    map.insert('>', Loc { x: 1, y: 0 });
    map.insert('<', Loc { x: -1, y: 0 });
    map.insert('^', Loc { x: 0, y: -1 });
    map.insert('v', Loc { x: 0, y: 1 });
    map
});
