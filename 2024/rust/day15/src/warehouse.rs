use std::collections::HashSet;

use crate::loc::Loc;

pub struct Warehouse {
    pub walls: HashSet<Loc>,
    pub boxes: HashSet<Loc>,
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
            robot,
            moves,
        }
    }

    pub fn gps_sum(&self) -> i64 {
        return self.boxes.clone().into_iter().map(|b| b.gps()).sum();
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
