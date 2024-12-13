pub struct Game {
    pub a: (i64, i64),
    pub b: (i64, i64),
    pub prize: (i128, i128),
}

impl Game {
    pub fn new(input: &str) -> Self {
        let mut lines = input.lines();
        let (a, b, price) = (
            lines.next().unwrap(),
            lines.next().unwrap(),
            lines.next().unwrap(),
        );
        let (a, b, price) = (
            Self::parse_button(a),
            Self::parse_button(b),
            Self::parse_prize(price),
        );
        Self { a, b, prize: price }
    }
    pub fn parse(input: &str) -> (i32, i32) {
        let mut iter = input.split_whitespace().map(|x| x.parse().unwrap());

        (iter.next().unwrap(), iter.next().unwrap())
    }

    pub fn parse_button(input: &str) -> (i64, i64) {
        let parts: Vec<&str> = input.split(',').collect();
        let x_part = parts[0].split('+').nth(1).unwrap().trim().parse().unwrap();
        let y_part = parts[1].split('+').nth(1).unwrap().trim().parse().unwrap();
        (x_part, y_part)
    }
    pub fn parse_prize(input: &str) -> (i128, i128) {
        let parts: Vec<&str> = input.split(',').collect();
        let x_part = parts[0].split('=').nth(1).unwrap().trim().parse().unwrap();
        let y_part = parts[1].split('=').nth(1).unwrap().trim().parse().unwrap();
        (x_part, y_part)
    }
    pub fn presses(&self, inc: (i64, i64), target: (i64, i64)) -> Vec<i64> {
        let mut presses: Vec<i64> = Vec::new();
        if target.0 % inc.0 == 0 {
            presses.push(target.0 / inc.0);
        }
        if target.1 % inc.1 == 0 {
            presses.push(target.1 / inc.1);
        }
        return presses;
    }

    pub fn a_btn(&self) -> i128 {
        if (self.prize.0 * self.b.1 as i128 - self.prize.1 * self.b.0 as i128)
            % (self.a.0 * self.b.1 - self.a.1 * self.b.0) as i128
            != 0
        {
            return 0;
        }
        return (self.prize.0 * self.b.1 as i128 - self.prize.1 * self.b.0 as i128)
            / self.has_unique_solution();
    }

    pub fn b_btn(&self) -> i128 {
        if (self.prize.0 * self.a.1 as i128 - self.prize.1 * self.a.0 as i128)
            % (self.b.0 * self.a.1 - self.b.1 * self.a.0) as i128
            != 0
        {
            return 0;
        }
        return (self.prize.0 * self.a.1 as i128 - self.prize.1 * self.a.0 as i128)
            / self.has_unique_solution();
    }

    pub fn has_unique_solution(&self) -> i128 {
        let b = self.b;
        let a = self.a;

        return (a.0 * b.1 - a.1 * b.0) as i128;
    }
    pub fn tokens(&self) -> i128 {
        // let lcm = self.lcm(self.a_btn(), self.b_btn());
        // println!("lcm: {:?}", lcm);
        let i = self.a_btn() as i128;
        let j = self.b_btn() as i128;
        // if i * self.a.0 as i128 + j * self.b.0 as i128 != self.prize.0
        //     || 1 * self.a.1 as i128 + j * self.b.1 as i128 == self.prize.1
        // {
        //     return 0;
        // }
        return i * 3 + j;
    }

    pub fn seed(&mut self, val: i128) {
        self.prize = (self.prize.0 + val, self.prize.1 + val);
    }
}

pub fn games(input: &str) -> Vec<Game> {
    input.split("\n\n").map(|x| Game::new(x)).collect()
}
