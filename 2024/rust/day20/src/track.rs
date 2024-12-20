use crate::loc::Loc;
use std::collections::HashMap;
use std::collections::HashSet;
use std::u64;

#[derive(Debug, Clone, Eq, PartialEq)]
pub struct Track {
    pub walls: HashSet<Loc>,
    pub start: Loc,
    pub finish: Loc,
    pub size: Loc,
    pub path: HashMap<Loc, char>,
    pub cost_path: HashMap<Loc, u64>,
}

impl Track {
    pub fn new(input: &str) -> Self {
        let mut walls: HashSet<Loc> = HashSet::new();
        let mut start: Loc = Loc::new(0, 0);
        let mut finish: Loc = Loc::new(0, 0);
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
            finish,
            size,
            path: HashMap::new(),
            cost_path: HashMap::new(),
        }
    }

    pub fn track(&mut self, node: Loc, cost: i64) -> HashMap<Loc, i64> {
        let mut map = HashMap::new();
        if self.walls.contains(&node) {
            return map;
        }
        let new_cost = 1 + cost;
        if node == self.start {
            map.insert(node.clone(), new_cost);
            return map;
        }
        for &d in Loc::DIRECTIONS.iter() {
            let next_pos = node.get_next(d);
            if self.path.contains_key(&next_pos) {
                continue;
            }
            self.path.insert(next_pos.clone(), d);
            let next_path = self.track(next_pos.clone(), new_cost);
            map.extend(next_path);
        }
        map.insert(node, new_cost);
        return map;
    }

    pub fn map_track(&mut self) -> HashMap<Loc, i64> {
        self.path.insert(self.finish.clone(), ' ');
        return self.track(self.finish.clone(), 0);
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

    pub fn print_map(&self, cost: &HashMap<Loc, i64>) {
        let (xm, ym) = self.size.as_tuple();
        for y in 0..ym + 1 {
            for x in 0..xm + 1 {
                let loc = Loc::new(x, y);
                if y == 0 || y == ym {
                    print!("###");
                    continue;
                }
                if self.walls.contains(&loc) {
                    print!(" # ");
                    continue;
                }
                if cost.contains_key(&loc) {
                    let &v = cost.get(&loc).unwrap();
                    print!(" {:02}", v);
                    continue;
                }
                if loc == self.start {
                    print!(" S ");
                } else if loc == self.finish {
                    print!(" E ");
                } else if self.cost_path.contains_key(&loc) {
                    print!("   ");
                } else {
                    print!(" . ")
                }
            }
            println!("{}", 0);
        }
        println!();
    }

    pub fn best_cheats(&mut self, minimum: i64) -> Option<i64> {
        let cheats: Vec<i64> = self
            .cheats()
            .iter()
            .filter(|&&c| c > minimum)
            .cloned()
            .collect();
        return Some(cheats.len() as i64);
    }

    fn cheats(&mut self) -> Vec<i64> {
        let track = self.map_track();
        let mut cheat_list: Vec<i64> = Vec::new();
        for w in self
            .walls
            .iter()
            .filter(|&loc| loc.x > 0 && loc.y > 0 && loc.x < self.size.x && loc.y < self.size.y)
        {
            if let Some(saving) = is_saving(&track, w.clone().left(), w.clone().right()) {
                cheat_list.push(saving);
            };
            if let Some(saving) = is_saving(&track, w.clone().up(), w.clone().down()) {
                cheat_list.push(saving);
            };
        }
        return cheat_list;
    }
}

fn is_saving(track: &HashMap<Loc, i64>, one: Loc, other: Loc) -> Option<i64> {
    let one = track.get(&one);
    let other = track.get(&other);
    if one.is_some() && other.is_some() {
        return Some((one.unwrap() - other.unwrap()).abs());
    }
    return None;
}
