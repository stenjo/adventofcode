use crate::loc::Loc;

#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Robot {
    pub p: Loc,
    v: Loc,
}

impl Robot {
    /// Constructs a new `Robot` by parsing a string like "p=6,3 v=-1,-3".
    pub fn new(input: &str) -> Result<Self, String> {
        let mut position = None;
        let mut velocity = None;

        for part in input.split_whitespace() {
            if let Some(pos_part) = part.strip_prefix("p=") {
                position = parse_loc(pos_part);
            } else if let Some(vel_part) = part.strip_prefix("v=") {
                velocity = parse_loc(vel_part);
            }
        }

        if let (Some(p), Some(v)) = (position, velocity) {
            Ok(Self { p, v })
        } else {
            Err("Invalid input format. Expected 'p=x,y v=x,y'.".to_string())
        }
    }

    /// Moves the robot by updating its position based on its velocity.
    pub fn move_robot(&mut self) {
        self.p = self.p.add(&self.v);
    }

    fn move_steps(&mut self, steps: u64, min: &Loc, max: &Loc) {
        let (vx, vy) = self.v.as_tuple();
        let v = Loc::new(vx * steps as i64, vy * steps as i64);
        self.p = self.p.add_teleport(&v, min, max);
    }
}

fn parse_loc(input: &str) -> Option<Loc> {
    let coords: Vec<&str> = input.split(',').collect();
    if coords.len() == 2 {
        if let (Ok(x), Ok(y)) = (coords[0].parse::<i64>(), coords[1].parse::<i64>()) {
            return Some(Loc::new(x, y));
        }
    }
    None
}

pub struct Restroom {
    robots: Vec<Robot>,
    space: (Loc, Loc),
}
impl Restroom {
    pub fn new(input: &str, max_x: i64, max_y: i64) -> Self {
        let robots: Vec<Robot> = input.lines().map(|l| Robot::new(l).expect("_")).collect();
        let min = Loc::new(0, 0);
        let max = Loc::new(max_x - 1, max_y - 1);
        let space = (min, max);

        Self { robots, space }
    }

    pub fn get_robots(&self) -> Vec<Robot> {
        return self.robots.clone();
    }

    pub fn safety_factor(&self) -> i64 {
        let mut factor = 1;

        for robots in self.quadrants() {
            factor *= robots.len() as i64;
        }

        return factor;
    }

    pub fn tree(&mut self) -> u64 {
        let (min, max) = &self.space;
        let mut count = 0;
        loop {
            for robot in self.robots.iter_mut() {
                robot.move_steps(1, &min, &max);
            }
            if self
                .quadrants()
                .into_iter()
                .map(|q| q.len())
                .all(|m| m == 1)
            {
                self.print();
                return count;
            }
            count += 1;
        }
        count
    }

    pub fn move_robots(&mut self, steps: u64) {
        let (min, max) = &self.space;
        for robot in self.robots.iter_mut() {
            robot.move_steps(steps, &min, &max);
        }
    }

    pub fn quadrants(&self) -> Vec<Vec<Robot>> {
        let mut result: Vec<Vec<Robot>> = Vec::new();
        let (min, max) = &self.space; // Assuming space provides `min` and `max` bounds as Loc.

        // Define quadrant boundaries
        let quads = get_quadrants(min, max);

        // Collect robots for each quadrant
        for ((x0, x1), (y0, y1)) in quads {
            let quadrant_robots: Vec<Robot> = self
                .robots
                .iter()
                .filter(|r| {
                    let (x, y) = r.p.as_tuple();
                    x >= x0 && x <= x1 && y >= y0 && y <= y1
                })
                .cloned()
                .collect();
            result.push(quadrant_robots);
        }

        result
    }

    pub fn print(&self) {
        let (min, max) = &self.space;

        for y in 0..max.as_tuple().1 + 1 {
            for x in 0..max.as_tuple().0 + 1 {
                let count = self
                    .robots
                    .iter()
                    .filter(|r| {
                        let (xn, yn) = r.p.as_tuple();
                        x == xn && y == yn
                    })
                    .cloned()
                    .collect::<Vec<_>>()
                    .len();
                if !in_quadrant((x, y), min, max) {
                    print!(" {} ", count);
                } else if count > 0 {
                    print!("{}", count);
                } else {
                    print!(".");
                }
            }
            println!();
        }
        let quad_str: String = self
            .quadrants()
            .into_iter()
            .map(|q| q.len().to_string())
            .collect::<Vec<String>>()
            .join(" * ");
        println!(" {} = {}", quad_str, self.safety_factor())
    }
}

pub fn in_quadrant(p: (i64, i64), min: &Loc, max: &Loc) -> bool {
    let (x, y) = p;
    for ((x1, x2), (y1, y2)) in get_quadrants(min, max) {
        if x1 <= x && x <= x2 && y1 <= y && y <= y2 {
            return true;
        }
    }
    return false;
}

fn get_quadrants(min: &Loc, max: &Loc) -> Vec<((i64, i64), (i64, i64))> {
    let quads = vec![
        (
            // Top-left
            (min.as_tuple().0, (max.as_tuple().0) / 2 - 1),
            (min.as_tuple().1, (max.as_tuple().1) / 2 - 1),
        ),
        (
            // Top-right
            ((max.as_tuple().0) / 2 + 1, max.as_tuple().0 + 1),
            (min.as_tuple().1, (max.as_tuple().1) / 2 - 1),
        ),
        (
            // Bottom-left
            (min.as_tuple().0, (max.as_tuple().0) / 2 - 1),
            ((max.as_tuple().1) / 2 + 1, max.as_tuple().1 + 1),
        ),
        (
            // Bottom-right
            ((max.as_tuple().0) / 2 + 1, max.as_tuple().0 + 1),
            ((max.as_tuple().1) / 2 + 1, max.as_tuple().1 + 1),
        ),
    ];
    quads
}
