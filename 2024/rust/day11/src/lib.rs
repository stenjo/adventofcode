pub struct Stones {
    stones: Vec<u128>,
}

impl Stones {
    pub fn new(input: String) -> Stones {
        Stones {
            stones: input
                .split_whitespace()
                .map(|x| x.parse::<u128>().unwrap())
                .collect(),
        }
    }
    pub fn get(&self, stone: u32) -> u128 {
        *self.stones.get(stone as usize).unwrap_or(&0)
    }

    pub fn count(&self) -> u128 {
        self.stones.len() as u128
    }

    pub fn sum(&self) -> u128 {
        self.stones.iter().sum()
    }
    pub fn values(&self) -> Vec<u128> {
        self.stones.clone()
    }

    pub fn blink(&mut self, blinks: usize) {
        for _i in 1..blinks + 1 {
            let old_stones: Vec<u128> = self.stones.clone();
            self.stones = Vec::new();
            for stone in old_stones.iter() {
                if stone == &0 {
                    self.stones.push(1);
                } else if stone.to_string().len() % 2 == 0 {
                    let stone_str = stone.to_string();
                    let stone_digits = stone_str.chars();
                    let stone_len = stone_str.len();
                    let first_stone = stone_digits
                        .clone()
                        .take(stone_len / 2)
                        .collect::<String>()
                        .parse::<u128>()
                        .unwrap();
                    self.stones.push(first_stone);
                    let second_stone = stone_digits
                        .clone()
                        .skip(stone_len / 2)
                        .collect::<String>()
                        .parse::<u128>()
                        .unwrap();
                    self.stones.push(second_stone);
                } else {
                    self.stones.push((*stone as u128) * 2024);
                }
            }
            print!(".")
        }
    }
}

pub fn part1(input: String) -> i64 {
    let mut stones = Stones::new(input);
    stones.blink(25);
    return stones.count().try_into().unwrap();
}

pub fn part2(input: String) -> i64 {
    let mut stones = Stones::new(input);
    stones.blink(75);
    return stones.count().try_into().unwrap();
}
