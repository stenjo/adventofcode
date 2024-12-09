use std::{collections::HashMap, io};

#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Block {
    id: i32,
    block_ids: Vec<i32>,
    size: usize,
}

impl Block {
    pub fn new(id: i32, size: usize) -> Block {
        Block {
            id,
            size: size,
            block_ids: vec![
                id / 2;
                {
                    if id % 2 == 0 {
                        size
                    } else {
                        0
                    }
                }
            ],
        }
    }

    pub fn used(&self) -> usize {
        return self.block_ids.len();
    }
    pub fn avail(&self) -> usize {
        return self.size - self.block_ids.len();
    }
    pub fn add(&mut self, block: i32) {
        if self.avail() > 0 {
            self.block_ids.push(block);
        } else {
            println!("Block {} is full", self.id);
        };
    }

    pub fn pop(&mut self) -> i32 {
        match self.block_ids.pop() {
            Some(val) => return val,
            None => return -1,
        }
    }

    pub fn free_space(&self) -> i64 {
        return (self.size - self.block_ids.len()) as i64;
    }

    pub fn blocks(&self) -> Vec<i32> {
        return self
            .block_ids
            .clone()
            .into_iter()
            .chain(vec![0; self.avail()].into_iter())
            .collect();
    }

    pub fn checksum(&self) -> i64 {
        let mut checksum = 0;
        self.block_ids.iter().enumerate().for_each(|(_, &v)| {
            checksum += self.id as i64 * v as i64;
        });
        println!("{} * {} = {}", self.id, self.block_ids.len(), checksum);
        return checksum;
    }

    pub fn print(&self) -> io::Result<()> {
        let mut s: String = "".to_owned();
        for block in &self.block_ids {
            s.push_str(&block.to_string());
        }
        for _i in 0..(self.size - self.block_ids.len()) {
            s.push_str(".");
        }
        print!("{}", s);
        return Ok(());
    }
}

#[derive(Debug, Clone, Eq, PartialEq)]
pub struct DiskMap {
    map: String,
    space: HashMap<i32, Block>,
}

impl DiskMap {
    pub fn new(input: String) -> DiskMap {
        let mut dm = DiskMap {
            map: input.trim().to_string(),
            space: HashMap::new(),
        };
        dm.parse();

        return dm;
    }

    fn parse(&mut self) {
        for (id, b) in self.map.chars().enumerate() {
            self.space.insert(
                id as i32,
                Block::new(id as i32, b.to_string().parse::<usize>().unwrap()),
            );
        }
    }

    pub fn free_space(&self) -> i64 {
        let mut free_space = 0;
        for block in self.space.values() {
            free_space += block.free_space();
        }
        return free_space;
    }

    pub fn checksum(&self) -> i64 {
        let mut blocks: Vec<_> = self.space.iter().collect();
        blocks.sort_by_key(|&(id, _)| id);
        let mut block_ids: Vec<i32> = Vec::new();
        blocks
            .iter()
            .map(|(_, block)| block.blocks())
            .for_each(|b| {
                block_ids.extend(b);
            });
        return block_ids
            .iter()
            .enumerate()
            .fold(0, |acc, (i, &v)| acc + (i as i64 * v as i64));
    }

    pub fn optimize(&mut self) {
        let mut front = 0;
        let mut back = self.space.len() as i32 - 1;

        while front < back {
            while {
                let front_avail = self.space.get(&front).unwrap().avail();
                let back_used = self.space.get(&back).unwrap().used();
                front_avail > 0 && back_used > 0
            } {
                // Extract the blocks into temporary variables to avoid mutable borrow conflicts
                let mut front_block = self.space.remove(&front).unwrap();
                let mut back_block = self.space.remove(&back).unwrap();

                // Perform the operation
                front_block.add(back_block.pop());

                // Insert the blocks back into the HashMap
                self.space.insert(front, front_block);
                self.space.insert(back, back_block);
            }

            // Update front and back indices
            if self.space.get(&front).unwrap().avail() == 0 {
                front += 1;
            }

            if self.space.get(&back).unwrap().used() == 0 {
                back -= 1;
            }
        }
    }

    pub fn optimize2(&mut self) {
        let mut front = 0;

        while front < self.space.len() as i32 - 2 {
            let mut back = self.space.len() as i32 - 1;
            while front < back {
                // println!("front: {}, back: {}", front, back);
                if {
                    let front_avail = self.space.get(&front).unwrap().avail();
                    let back_used = self.space.get(&back).unwrap().used();
                    front_avail > 0 && back_used > 0 && front_avail >= back_used
                } {
                    self.move_file(front, back);
                    front = 0;
                    back = self.space.len() as i32 - 1;
                } else if front < back {
                    back -= 1;
                } else {
                    break;
                }
            }
            front += 1;
        }
    }

    fn move_file(&mut self, front: i32, back: i32) {
        // Extract the blocks into temporary variables to avoid mutable borrow conflicts
        let mut front_block = self.space.remove(&front).unwrap();
        let mut back_block = self.space.remove(&back).unwrap();

        // Perform the operation
        while front_block.avail() > 0 && back_block.used() > 0 {
            front_block.add(back_block.pop());
        }

        // Insert the blocks back into the HashMap
        self.space.insert(front, front_block);
        self.space.insert(back, back_block);
    }

    pub fn print(&self) -> io::Result<()> {
        for i in 0..self.space.len() {
            self.space.get(&(i as i32)).unwrap().print()?;
        }
        println!();
        return Ok(());
    }
}

pub fn part1(input: String) -> i64 {
    let mut dm = DiskMap::new(input);
    dm.optimize();

    return dm.checksum();
}

pub fn part2(input: String) -> i64 {
    let mut dm = DiskMap::new(input);
    dm.optimize2();

    return dm.checksum();
}
