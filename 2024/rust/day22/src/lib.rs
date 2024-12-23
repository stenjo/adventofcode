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

pub fn buy_orders(mut secret: u64) -> HashMap<Vec<i8>, u16> {
    let mut result: HashMap<Vec<i8>, u16> = HashMap::new();
    let mut changes: Vec<i8> = vec![];
    secret = calculate_price(secret, 1);
    let mut current: i8 = (secret % 10) as i8;
    changes.push(current);
    for _i in 0..1999 {
        secret = calculate_price(secret, 1);
        let next = (secret % 10) as i8;
        let change = next - current;
        changes.push(change);
        if changes.len() == 4 {
            if !result.contains_key(&changes) {
                result.insert(changes.clone(), next as u16);
            }
            changes.remove(0);
        }
        current = next;
    }

    return result;
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
    let mut buyers: Vec<u64> = input.lines().map(|x| x.parse::<u64>().unwrap()).collect();
    let mut patterns = buy_orders(buyers.pop().unwrap());
    while let Some(buyer) = buyers.pop() {
        let new_patterns = buy_orders(buyer);
        for (pattern, value) in new_patterns {
            if patterns.contains_key(&pattern) {
                patterns.insert(pattern.clone(), patterns[&pattern] + value);
                continue;
            }

            patterns.insert(pattern.clone(), value);
        }
    }
    return patterns.values().max().unwrap().clone() as i64;
}
