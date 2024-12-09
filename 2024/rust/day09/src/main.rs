use std::{cmp::Reverse, collections::BinaryHeap, fs, time::Instant};

use day09::part1;

// Borrowed from https://github.com/smith61/advent_of_code/blob/main/src/year_2024/day_09.rs

pub fn part2(input: &str) -> u64 {
    struct Block {
        disk_offset: usize,
        block_size: usize,
        block_id: u64,
    }

    let mut file_blocks = Vec::new();
    let mut free_blocks = [0; 10].map(|_| BinaryHeap::default());
    let mut is_free_block = false;
    let mut block_id = 0;
    let mut disk_offset = 0;
    for c in input.bytes() {
        let size = (c - b'0') as usize;
        if is_free_block {
            free_blocks[size].push(Reverse(disk_offset));
        } else {
            file_blocks.push(Block {
                disk_offset,
                block_size: size,
                block_id: block_id,
            });

            block_id += 1;
        }

        is_free_block = !is_free_block;
        disk_offset += size;
    }

    for file_index in (0..file_blocks.len()).rev() {
        let file_block = &mut file_blocks[file_index];

        let free_block = (file_block.block_size..10)
            .flat_map(|size| free_blocks[size].peek().map(|&Reverse(v)| (v, size)))
            .min();

        if let Some((disk_offset, free_size)) = free_block {
            if disk_offset >= file_block.disk_offset {
                continue;
            }

            file_block.disk_offset = disk_offset;
            free_blocks[free_size].pop();
            if free_size > file_block.block_size {
                free_blocks[free_size - file_block.block_size]
                    .push(Reverse(disk_offset + file_block.block_size));
            }
        }
    }

    file_blocks
        .iter()
        .map(|block| {
            let mut value = 0;
            for idx in 0..block.block_size {
                value += (block.disk_offset + idx) as u64 * block.block_id;
            }

            value
        })
        .sum()
}

pub fn main() {
    let path = "".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(&input.clone().trim()));
}
