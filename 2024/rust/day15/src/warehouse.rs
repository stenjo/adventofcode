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

    pub fn move_robot(&mut self, dir: char) -> bool {
        if dir == '^' {
            let above = self.robot.clone().add(&Loc::new(0, -1));
            if self.boxes.contains(&above) {
                if self.push_boxes_up() {
                    return false;
                }
            }
            self.robot.up();
            return true;
        }
        if dir == 'v' {
            let below = self.robot.clone().add(&Loc::new(0, 1));
            if self.boxes.contains(&below) {
                if !self.push_boxes_down() {
                    return false;
                }
            }
            self.robot.down();
            return true;
        }
        if dir == '>' {
            let right = self.robot.clone().add(&Loc::new(1, 0));
            if self.boxes.contains(&right) {
                if !self.push_boxes_right() {
                    return false;
                }
            }
            self.robot.right();
            return true;
        }
        if dir == '<' {
            let left = self.robot.clone().add(&Loc::new(1, 0));
            if self.boxes.contains(&left) {
                if !self.push_boxes_left() {
                    return false;
                }
            }
            self.robot.left();
            return true;
        }
        return false;
    }

    fn push_boxes_up(&self) -> bool {
        todo!()
    }

    fn push_boxes_down(&self) -> bool {
        todo!()
    }

    fn push_boxes_right(&self) -> bool {
        todo!()
    }

    fn push_boxes_left(&self) -> bool {
        todo!()
    }
}
