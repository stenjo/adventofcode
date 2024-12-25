pub struct Matching {
    pub keys: Vec<Vec<i32>>,
    pub locks: Vec<Vec<i32>>,
}

impl Matching {
    pub fn new(inputs: &str) -> Self {
        let mut keys: Vec<Vec<i32>> = Vec::new();
        let mut locks: Vec<Vec<i32>> = Vec::new();
        let patterns = inputs.split("\n\n");
        for pattern in patterns {
            let mut pins: Vec<i32> = vec![0, 0, 0, 0, 0];
            let mut lines = pattern.lines();
            let lock = lines.next().unwrap().chars().all(|c| c == '#');
            for (line_no, line) in lines.enumerate() {
                if line_no > 4 {
                    continue;
                }
                for (i, c) in line.chars().enumerate() {
                    if c == '#' {
                        pins[i] += 1;
                    }
                }
            }
            if lock {
                locks.push(pins.clone());
                // println!("lock: {:?}", pins)
            } else {
                keys.push(pins.clone());
                // println!("key: {:?}", pins)
            }
            // println!();
        }
        return Self { keys, locks };
    }

    pub fn run(&mut self) -> i64 {
        let mut number: i64 = 0;
        for key in self.keys.iter() {
            for lock in self.locks.iter() {
                let mut fits = true;
                for i in 0..5 {
                    if key[i] + lock[i] > 5 {
                        fits = false;
                        break;
                    }
                }
                if fits {
                    println!(" key: {:?},", key);
                    println!("lock: {:?}, match: {}", lock, fits);
                    println!(
                        "   -  {:?}\n",
                        key.iter()
                            .enumerate()
                            .map(|(i, x)| x + lock[i])
                            .collect::<Vec<i32>>()
                    );
                    number += 1;
                }
            }
        }
        number
    }
}

pub fn part1(input: String) -> i64 {
    let mut m = Matching::new(&input);
    return m.run();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
