// Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number.
// Finally, prune the secret number.
// Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
// Then, mix this result into the secret number. Finally, prune the secret number.
// Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

// Each step of the above process involves mixing and pruning:

// To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
// To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)

use std::cmp::max;
use std::collections::HashMap;

pub fn calculate_price(secret: u64, iterations: usize) -> u64 {
    let mut result: u64 = secret;
    for _i in 0..iterations {
        result = result ^ result << 6;
        result = result % 16777216; // 1000000000000000000000000
        result = result ^ result >> 5;
        result = result % 16777216;

        result = result ^ result << 11;
        result = result % 16777216;
    }

    result
}

pub fn sequences(mut secret: u64) -> HashMap<u64, Vec<i32>> {
    let mut result: HashMap<u64, Vec<i32>> = HashMap::new();
    let mut changes: Vec<i32> = vec![];
    secret = calculate_price(secret, 1);
    let mut current = secret % 10;
    changes.push(current as i32);
    for _i in 0..1999 {
        secret = calculate_price(secret, 1);
        let next = secret % 10;
        let change = next as i32 - current as i32;
        changes.push(change);
        if changes.len() == 4 {
            if !result.contains_key(&next) {
                result.insert(next, changes.clone());
                if result.len() == 10 {
                    break;
                }
            }
            changes.remove(0);
        }
        current = next;
    }

    return result;
}

/// Matches a given pattern in the sequence generated from the secret number.
///
/// # Arguments
///
/// * `secret` - The initial secret number.
/// * `pattern` - A vector of i32 representing the pattern to match.
///
/// # Returns
///
/// * `u64` - The next number in the sequence if the pattern is matched, otherwise 0.
pub fn match_pattern(mut secret: u64, pattern: Vec<i32>) -> u64 {
    let mut changes: Vec<i32> = vec![];
    let mut current = secret % 10;
    changes.push(current as i32);
    for i in 0..1999 {
        secret = calculate_price(secret, 1);
        let next = secret % 10;
        let change = next as i32 - current as i32;
        changes.push(change);
        if changes.len() >= 4 {
            if changes[0] == pattern[0]
                && changes[1] == pattern[1]
                && changes[2] == pattern[2]
                && changes[3] == pattern[3]
            {
                println!("{} {:?} == {:?}", i, changes, pattern);
            }
            if changes == pattern {
                return next;
            }
            changes.remove(0);
        }
        current = next;
    }

    0
}

pub fn part1(input: String) -> i64 {
    let lines = input.lines();
    let mut sum = 0;
    for line in lines {
        let secret = line.parse::<u64>().unwrap();
        let result = calculate_price(secret, 2000);
        sum += result;
    }

    sum as i64
}

pub fn part2(input: String) -> i64 {
    let buyers: Vec<u64> = input.lines().map(|x| x.parse::<u64>().unwrap()).collect();
    let mut best = 0;
    for i in 0..buyers.len() {
        let buyer = buyers[i];
        let result = check_for(buyer, buyers.clone());
        if let Some(value) = result {
            best = max(best, value);
        }
    }
    best
}

pub fn check_for(starter: u64, buyers: Vec<u64>) -> Option<i64> {
    let mut best = 0;
    let startset = sequences(starter);
    let keys: Vec<&u64> = startset.keys().collect();
    for i in keys.into_iter().rev() {
        let mut sum = i.clone() as i64;
        let pattern = startset[&i].clone();
        println!("{} : {:?}", i, pattern);
        for buyer in &buyers {
            if *buyer == starter {
                continue;
            }
            let seq = match_pattern(*buyer, pattern.clone());
            println!("{} : {:?}", seq, buyer);
            sum += seq as i64;
        }
        best = max(best, sum);
    }
    Some(best as i64)
}
