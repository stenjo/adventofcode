use std::collections::{HashMap, HashSet};

use crate::loc::Loc;

pub struct Warehouse {
    pub walls: HashSet<Loc>,
    pub boxes: HashSet<Loc>,
    pub box_pair: HashMap<Loc, Loc>,
    pub robot: Loc,
    pub moves: Vec<char>,
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

        for (y, line) in map_txt.lines().into_iter().enumerate() {
            for (x, c) in line.chars().into_iter().enumerate() {
                if c == '#' {
                    walls.insert(Loc::new(x as i64, y as i64));
                } else if c == '@' {
                    robot = Loc::new(x as i64, y as i64);
                } else if c == 'O' {
                    boxes.insert(Loc::new(x as i64, y as i64));
                }
            }
        }
        Self {
            walls,
            boxes,
            box_pair: HashMap::new(),
            robot,
            moves,
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
        }

        self.walls = exp_walls;

        let mut exp_boxes: HashSet<Loc> = HashSet::new();
        for b in self.boxes.clone() {
            let b1 = Loc::new(b.x * 2, b.y);
            let b2 = Loc::new(b.x * 2 + 1, b.y);

            exp_boxes.insert(b1.clone());
            exp_boxes.insert(b2.clone());
            self.box_pair.insert(b1.clone(), b2.clone());
            self.box_pair.insert(b2, b1);
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
}
