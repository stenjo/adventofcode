use std::collections::{HashMap, HashSet};

use crate::loc::Loc;

pub struct Warehouse {
    pub walls: HashSet<Loc>,
    pub boxes: HashSet<Loc>,
    pub box_map: HashMap<Loc, char>,
    pub robot: Loc,
    pub moves: Vec<char>,
    size: Loc,
}

impl Warehouse {
    pub fn new(input: &str) -> Self {
        let mut parts = input.split("\n\n");
        let (map_txt, moves_txt) = (parts.next().unwrap(), parts.next().unwrap());

        let moves = moves_txt
            .trim()
            .chars()
            .filter(|c| vec!['^', '<', '>', 'v'].contains(c))
            .collect();
        let mut walls: HashSet<Loc> = HashSet::new();
        let mut boxes: HashSet<Loc> = HashSet::new();
        let mut robot: Loc = Loc::new(0, 0);
        let mut size: Loc = Loc::new(0, 0);
        for (y, line) in map_txt.lines().into_iter().enumerate() {
            for (x, c) in line.chars().into_iter().enumerate() {
                if c == '#' {
                    walls.insert(Loc::new(x as i64, y as i64));
                } else if c == '@' {
                    robot = Loc::new(x as i64, y as i64);
                } else if c == 'O' {
                    boxes.insert(Loc::new(x as i64, y as i64));
                }
                size = Loc::new(x as i64, y as i64);
            }
        }
        Self {
            walls,
            boxes,
            box_map: HashMap::new(),
            robot,
            moves,
            size,
        }
    }

    pub fn expand(&mut self) {
        let mut exp_walls: HashSet<Loc> = HashSet::new();

        for w in self.walls.clone() {
            exp_walls.insert(Loc { x: w.x * 2, y: w.y });
            exp_walls.insert(Loc {
                x: w.x * 2 + 1,
                y: w.y,
            });
            if self.size.x < w.x * 2 + 1 {
                self.size.x = w.x * 2 + 1;
            }
        }

        self.robot.x *= 2;

        self.walls = exp_walls;

        let mut exp_boxes: HashSet<Loc> = HashSet::new();
        for b in self.boxes.clone() {
            let b1 = Loc::new(b.x * 2, b.y);
            let b2 = Loc::new(b.x * 2 + 1, b.y);

            exp_boxes.insert(b1.clone());
            exp_boxes.insert(b2.clone());
            self.box_map.insert(b1, '[');
            self.box_map.insert(b2, ']');
        }

        self.boxes = exp_boxes;
    }

    pub fn gps_sum(&self) -> i64 {
        return self
            .boxes
            .clone()
            .into_iter()
            .enumerate()
            .map(|(_k, b)| b.gps())
            .sum();
    }

    pub fn gps_sum_2(&self) -> i64 {
        return self
            .boxes
            .clone()
            .into_iter()
            .enumerate()
            .filter(|(k, _v)| k % 2 == 0)
            .map(|(_k, b)| b.gps())
            .sum();
    }

    pub fn run_robot(&mut self) {
        for dir in self.moves.clone() {
            self.move_robot(dir);
        }
    }

    pub fn move_robot(&mut self, dir: char) -> bool {
        let next_pos = self.robot.get_next(dir);
        if self.walls.contains(&next_pos) {
            return false;
        }
        if self.boxes.contains(&next_pos) {
            if !self.push_boxes(&next_pos, dir) {
                return false;
            }
        }
        self.robot = next_pos;
        return true;
    }

    pub fn move_robot_2(&mut self, dir: char) -> bool {
        let next_pos = self.robot.get_next(dir);
        if self.walls.contains(&next_pos) {
            return false;
        }
        if self.boxes.contains(&next_pos) {
            if !self.push_boxes_2(&next_pos, dir) {
                return false;
            }
        }
        self.robot = next_pos;
        return true;
    }

    fn push_boxes(&mut self, loc: &Loc, dir: char) -> bool {
        let next_pos = loc.get_next(dir);
        if self.walls.contains(&next_pos) {
            return false;
        }
        if self.boxes.contains(&next_pos) {
            if !self.push_boxes(&next_pos, dir) {
                return false;
            }
        }
        self.boxes.remove(&loc);
        self.boxes.insert(next_pos);
        return true;
    }

    fn push_boxes_2(&mut self, loc: &Loc, dir: char) -> bool {
        let next_pos = loc.get_next(dir);
        let other_pos = self.get_other_pos(&loc).unwrap();
        let other_next = other_pos.get_next(dir);

        if self.walls.contains(&next_pos) || self.walls.contains(&other_next) {
            return false;
        }
        if self.boxes.contains(&next_pos) {
            if !self.push_boxes_2(&next_pos, dir) {
                return false;
            }
            if !self.push_boxes_2(&other_next, dir) {
                return false;
            }
        }
        self.boxes.remove(&loc);
        self.boxes.remove(&other_pos);
        self.boxes.insert(next_pos.clone());
        self.boxes.insert(other_next.clone());
        if let Some(b1) = self.box_map.remove(&loc) {
            self.box_map.insert(next_pos, b1);
        }
        if let Some(b2) = self.box_map.remove(&other_pos) {
            self.box_map.insert(other_next, b2);
        }
        return true;
    }

    pub fn get_other_pos(&self, loc: &Loc) -> Option<Loc> {
        if let Some(box_side) = self.box_map.get(loc) {
            if *box_side == '[' {
                return Some(loc.clone().add(&Loc { x: 1, y: 0 }));
            }
            if *box_side == ']' {
                return Some(loc.clone().add(&Loc { x: -1, y: 0 }));
            }
        }
        println!("{:?}", loc.as_tuple());
        None
    }
    pub fn print(&self) {
        let (xm, ym) = self.size.as_tuple();
        for y in 0..ym + 1 {
            for x in 0..xm + 1 {
                let loc = Loc::new(x, y);
                if self.walls.contains(&loc) {
                    print!("#");
                } else if self.boxes.contains(&loc) {
                    if let Some(value) = self.box_map.get(&loc) {
                        print!("{}", value);
                    } else {
                        print!("X");
                    }
                } else if loc == self.robot {
                    print!("@");
                } else {
                    print!(".")
                }
            }
            println!();
        }
        println!();
    }
}
