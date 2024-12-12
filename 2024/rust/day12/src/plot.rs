use crate::plant::Plant;

#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Plot {
    plant_type: char,
    plants: Vec<Plant>,
}
impl Plot {
    pub fn add_plant(&mut self, plant: Plant) {
        if plant.get_plant() != self.plant_type {
            panic!("Plant type mismatch");
        }
        self.plants.push(plant);
    }
    pub fn perimeter(&self) -> u64 {
        let mut perimeter = self.plants.len() as u64 * 4;
        for first in 0..self.plants.len() {
            for second in first + 1..self.plants.len() {
                if self.is_connected(first, second)
                    && self.plants[first].get_plant() == self.plants[second].get_plant()
                {
                    perimeter -= 2;
                }
            }
        }
        perimeter
    }

    fn is_connected(&self, first: usize, second: usize) -> bool {
        let (x1, y1) = self.plants[first].pos();
        let (x2, y2) = self.plants[second].pos();
        if (x1 - x2).abs() == 1 || (y1 - y2).abs() == 1 {
            return true;
        }
        return false;
    }
    fn max_pos(&self) -> (i64, i64) {
        let mut max_x = 0;
        let mut max_y = 0;
        for plant in &self.plants {
            let (x, y) = plant.pos();
            if x > max_x {
                max_x = x;
            }
            if y > max_y {
                max_y = y;
            }
        }
        (max_x, max_y)
    }

    fn min_pos(&self) -> (i64, i64) {
        let mut min_x = 0;
        let mut min_y = 0;
        for plant in &self.plants {
            let (x, y) = plant.pos();
            if x < min_x {
                min_x = x;
            }
            if y < min_y {
                min_y = y;
            }
        }
        (min_x, min_y)
    }
    pub fn connecting_positions(&self) -> Vec<(i64, i64)> {
        let mut positions: Vec<(i64, i64)> = Vec::new();
        let (max_x, max_y) = self.max_pos();
        let (min_x, min_y) = self.min_pos();
        for x in min_x - 1..max_x + 2 {
            for y in min_y - 1..max_y + 2 {
                for plant in &self.plants {
                    let (px, py) = plant.pos();
                    if is_neighbour(px, x, py, y) && !self.in_plot(x, y) {
                        positions.push((x, y));
                    }
                }
            }
        }
        positions
    }

    fn in_plot(&self, x: i64, y: i64) -> bool {
        for plant in self.plants.clone() {
            if plant.pos() == (x as i64, y as i64) {
                return true;
            }
        }
        false
    }

    pub fn area(&self) -> u64 {
        return self.plants.len() as u64;
    }

    pub fn print(&self, other: Vec<(i64, i64)>) {
        let (max_x, max_y) = self.max_pos();
        let (min_x, min_y) = self.min_pos();
        println!();
        println!("Plant {}: ", self.plant_type);
        for y in min_y - 1..max_y + 2 {
            for x in min_x - 1..max_x + 2 {
                if self.in_plot(x, y) {
                    print!("{}", self.plant_type);
                } else if other.contains(&(x, y)) {
                    print!("+");
                } else {
                    print!(".");
                }
            }
            println!();
        }
    }

    pub fn new(plants: Vec<Plant>) -> Self {
        let c = plants.first().unwrap().get_plant();
        Self {
            plant_type: c,
            plants,
        }
    }

    pub fn plant_type(&self) -> char {
        return self.plant_type;
    }
}

fn is_neighbour(px: i64, x: i64, py: i64, y: i64) -> bool {
    (px - x).abs() == 1 || (py - y).abs() == 1
}
