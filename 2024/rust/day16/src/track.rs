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

    pub fn stands(&self, loc: Loc) -> i64 {
        let mut count: i64 = 0;
        let directions = ['>', 'v', '<', '^'];
        for &d in &directions {
            let next_pos = loc.get_next(d);
            if self.walls.contains(&next_pos) {
                count += 1;
            }
        }
        count
    }

    pub fn get_trail(&self) -> Vec<Loc> {
        let mut trail: Vec<Loc>=Vec::new();
        let mut spot = self.start.clone();
        trail.push(spot);
        let directions = ['>', 'v', '<', '^'];
        let cost = u64::MAX;
        while spot != self.finish {
            let mut lowest = spot.clone();

            for &d in &directions {
                let next_pos = spot.get_next(d);
                if let Some(next) = self.cost_patha.get(&next_pos) {
                    if 
                }
                if self.walls.contains(&next_pos) {
                    count += 1;
                }
            }
        }

        return trail;
    }

    // pub fn run_reindeer(&mut self) -> i64 {
    //     let shortest_path = dynamic_dijkstra(
    //         &self.graph,
    //         self.start_idx,
    //         self.finish_idx,
    //         |prev, current, next| {
    //             if let Some(p) = prev {
    //                 if p != current {
    //                     1000
    //                 } else {
    //                     0
    //                 }
    //             } else {
    //                 0
    //             }
    //         },
    //     );
    //     if let Some(cost) = shortest_path {
    //         println!(
    //             "The shortest path cost from {:?} to {:?} is {}",
    //             self.start, self.finish, cost
    //         );
    //         return cost as i64;
    //     } else {
    //         println!("No path found from {:?} to {:?}", self.start, self.finish);
    //     }
    //     0
    // }

    pub fn run(&mut self) -> i64 {
        let directions = ['<', '^', '>', 'v'];

        self.cost_path.insert(self.finish.clone(), 0);

        for &d in &directions {
            let next_pos = self.finish.get_next(d);
            self.backtrack(next_pos, d, 0);
        }

        if let Some(&cost) = self.cost_path.get(&self.start) {
            return cost as i64;
        }
        0
    }

    pub fn backtrack(&mut self, node: Loc, dir: char, cost: u64) -> u64 {
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

        let directions = ['<', '^', '>', 'v'];
        for &d in &directions {
            let next_pos = node.get_next(d);
            let turn_cost = if d == dir { 0 } else { 1000 };
            let total_cost = turn_cost + new_cost;
            self.backtrack(next_pos, d, total_cost);
        }
        return new_cost;
    }

    // pub fn find_min_cost(&mut self, pos: Loc, dir: char) -> i64 {
    //     if pos == self.finish {
    //         return 0;
    //     }
    //     if self.walls.contains(&pos) || self.path.contains_key(&pos) {
    //         return i64::MAX;
    //     }

    //     self.path.insert(pos.clone(), dir);

    //     let directions = ['>', 'v', '<', '^'];
    //     let mut min_cost = i64::MAX;

    //     for &d in &directions {
    //         let next_pos = pos.get_next(d);
    //         let turn_cost = if d == dir { 0 } else { 1000 };
    //         let move_cost = 1;
    //         let total_cost = turn_cost + move_cost;

    //         let cost = self.find_min_cost(next_pos, d);
    //         if cost != i64::MAX {
    //             min_cost = min_cost.min(cost + total_cost);
    //         }
    //     }

    //     self.path.remove(&pos);
    //     min_cost
    // }

    pub fn print(&self) {
        let (xm, ym) = self.size.as_tuple();
        for y in 0..ym + 1 {
            for x in 0..xm + 1 {
                let loc = Loc::new(x, y);
                if self.walls.contains(&loc) {
                    print!("######");
                    continue;
                }
                if loc == self.start {
                    print!("   S  ");
                } else if loc == self.finish {
                    print!("   E  ");
                } else if self.cost_path.contains_key(&loc) {
                    let &dir = self.cost_path.get(&loc).unwrap();
                    print!(" {:4} ", dir % 1000 + (dir / 1000 * 100));
                } else {
                    print!("   .  ")
                }
            }
            println!("{}", 0);
        }
        println!();
    }
}
