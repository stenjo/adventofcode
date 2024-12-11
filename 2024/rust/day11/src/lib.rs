use std::collections::HashMap;

pub struct Stones {
    stones: HashMap<u128, u32>,
}

impl Stones {
    pub fn new(input: String) -> Stones {
        Stones {
            stones: input.split_whitespace().fold(HashMap::new(), |mut acc, x| {
                let num = x.parse::<u128>().unwrap();
                *acc.entry(num).or_insert(0) += 1;
                acc
            }),
        }
    }
    pub fn get(&self, stone: u128) -> u32 {
        *self.stones.get(&stone).unwrap_or(&0)
    }

    pub fn tuples(&self) -> Vec<(u128, u32)> {
        self.stones.iter().map(|(k, v)| (*k, *v)).collect()
    }

    pub fn count(&self) -> u128 {
        self.stones.values().copied().sum::<u32>() as u128
    }

    pub fn sum(&self) -> u128 {
        self.stones.values().copied().map(u128::from).sum()
    }
    pub fn keys(&self) -> Vec<u128> {
        let mut k: Vec<u128> = self.stones.keys().cloned().collect();
        k.sort();
        k
    }
    pub fn values(&self) -> Vec<u128> {
        let mut keys: Vec<_> = self.stones.keys().cloned().collect();
        keys.sort();
        keys.iter().map(|k| self.stones[k] as u128).collect()
    }
    fn inc(&mut self, stone: u128, incr: u32) {
        let count = self.get(stone);
        self.stones.insert(stone, count + incr);
    }

    fn remove(&mut self, stone: &u128, count: u32) {
        let val = self.get(*stone);
        if val < count {
            panic!("Can't remove more stones than we have");
        } else if val == count {
            self.stones.remove(stone);
        } else {
            self.stones.insert(*stone, val - count);
        }
    }

    pub fn blink(&mut self, blinks: usize) {
        for _i in 0..blinks {
            let old_stones: Vec<u128> = self.stones.keys().cloned().collect();

            for stone in old_stones.iter() {
                let count = self.get(*stone);
                self.remove(stone, count);
                for (num, count) in self.process_number(stone, count).iter() {
                    self.inc(*num, *count);
                }
            }
            // self.stones = new_stones;
            // print!(".")
        }
    }

    pub fn process_number(&mut self, stone: &u128, count: u32) -> Vec<(u128, u32)> {
        let mut out: Vec<(u128, u32)> = Vec::new();
        if stone == &0 {
            out.push((1, count));
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
            out.push((first_stone, count));
            let second_stone = stone_digits
                .clone()
                .skip(stone_len / 2)
                .collect::<String>()
                .parse::<u128>()
                .unwrap();
            out.push((second_stone, count));
        } else {
            out.push(((*stone as u128) * 2024, count));
        }
        return out;
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
