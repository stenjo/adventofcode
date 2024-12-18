use crate::loc::Loc;
use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::visit::EdgeRef;
use std::cmp::Reverse;
use std::collections::HashSet;
use std::collections::{BinaryHeap, HashMap};
use std::u64;

#[derive(Debug, Clone, Eq, PartialEq)]
pub struct Track {
    pub walls: HashSet<Loc>,
    pub start: Loc,
    pub start_idx: NodeIndex,
    pub finish: Loc,
    pub finish_idx: NodeIndex,
    pub size: Loc,
    pub path: HashMap<Loc, char>,
    pub cost_path: HashMap<Loc, u64>,
}

impl Track {
    pub fn new(input: &str) -> Self {
        let mut walls: HashSet<Loc> = HashSet::new();
        let mut start: Loc = Loc::new(0, 0);
        let mut finish: Loc = Loc::new(0, 0);
        let mut start_idx: NodeIndex = NodeIndex::new(0);
        let mut finish_idx: NodeIndex = NodeIndex::new(0);
        let mut size: Loc = Loc::new(0, 0);
        for (y, line) in input.lines().into_iter().enumerate() {
            for (x, c) in line.chars().into_iter().enumerate() {
                if c == '#' {
                    walls.insert(Loc::new(x as i64, y as i64));
                } else if c == 'S' {
                    start = Loc::new(x as i64, y as i64);
                } else if c == 'E' {
                    finish = Loc::new(x as i64, y as i64);
                }
                size = Loc::new(x as i64, y as i64);
            }
        }
        for y in 0..size.y + 1 {
            for x in 0..size.x + 1 {
                let loc = Loc::new(x, y);
            }
        }

        Self {
            walls,
            start,
            start_idx,
            finish,
            finish_idx,
            size,
            path: HashMap::new(),
            cost_path: HashMap::new(),
        }
    }

    pub fn stands(&self, loc: &Loc) -> HashSet<Loc> {
        let mut stands: HashSet<Loc> = HashSet::new();
        let directions = ['>', 'v', '<', '^'];
        for &d in &directions {
            let next_pos = loc.get_next(d);
            if self.walls.contains(&next_pos) {
                stands.insert(next_pos);
            }
        }
        return stands;
    }

    pub fn get_stands(&self, directions: [char; 4]) -> HashSet<Loc> {
        let mut trail: HashSet<Loc> = HashSet::new();
        let mut spot = self.start.clone();
        let mut cost = u64::MAX;
        trail.insert(self.finish.clone());
        trail.insert(self.start.clone());
        while spot != self.finish {
            let mut lowest = spot.clone();
            for &d in &directions {
                let next_pos = spot.get_next(d);a
                if let Some(next) = self.cost_path.get(&next_pos) {
                    if next < &cost {
                        lowest = next_pos.clone();
                        cost = *next;
                    }
                }
            }
            spot = lowest.clone();
            trail.insert(lowest);
        }

        return trail;
    }

    pub fn run(&mut self) -> i64 {
        let directions: [[char; 4]; 4] = [
            ['>', 'v', '<', '^'],
            ['v', '<', '^', '>'],
            ['<', '^', '>', 'v'],
            ['^', '>', 'v', '<'],
        ];
        self.cost_path.insert(self.finish.clone(), 0);
        for dir in directions {
            for &d in &dir {
                let next_pos = self.finish.get_next(d);
                self.backtrack(next_pos, d, 0, dir);
            }
        }

        if let Some(&cost) = self.cost_path.get(&self.start) {
            return cost as i64;
        }
        0
    }

    pub fn backtrack(&mut self, node: Loc, dir: char, cost: u64, directions: [char; 4]) -> u64 {
        if node == self.finish {
            return u64::MAX;
        }
        if self.walls.contains(&node) {
            return u64::MAX;
        }
        let mut new_cost = 1 + cost;
        if node == self.start {
            if dir != '<' {
                new_cost += 1000;
            }
            self.cost_path.insert(node.clone(), new_cost);
            return new_cost;
        }
        if let Some(&earlier_cost) = self.cost_path.get(&node) {
            if new_cost > earlier_cost {
                return earlier_cost;
            }
        }

        self.cost_path.insert(node.clone(), new_cost);

        for &d in &directions {
            let next_pos = node.get_next(d);
            let turn_cost = if d == dir { 0 } else { 1000 };
            let total_cost = turn_cost + new_cost;
            self.backtrack(next_pos, d, total_cost, directions);
        }
        return new_cost;
    }

    pub fn print(&self, set: &HashSet<Loc>) {
        let (xm, ym) = self.size.as_tuple();
        for y in 0..ym + 1 {
            for x in 0..xm + 1 {
                let loc = Loc::new(x, y);
                if self.walls.contains(&loc) {
                    print!("#");
                    continue;
                }
                if set.contains(&loc) {
                    print!("O");
                    continue;
                }
                if loc == self.start {
                    print!("S");
                } else if loc == self.finish {
                    print!("E");
                } else if self.cost_path.contains_key(&loc) {
                    print!(" ");
                } else {
                    print!(".")
                }
            }
            println!("{}", 0);
        }
        println!();
    }
}
