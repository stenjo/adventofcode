// Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number.
// Finally, prune the secret number.
// Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
// Then, mix this result into the secret number. Finally, prune the secret number.
// Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.

// Each step of the above process involves mixing and pruning:

// To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
// To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)

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

    return result;
}

pub fn sequences(secret: u64) -> HashMap<u64, Vec<u64>> {
    let mut result: HashMap<u64, Vec<u64>> = HashMap::new();
    let mut changes: Vec<u64> = vec![];
    let mut current = calculate_price(secret, 1) % 10;
    for _i in 0..1999 {
        let next = calculate_price(current, 1) % 10;
        let change = next - current;
        changes.push(change);
        if changes.len() >= 4 && !result.contains_key(&next) {
            result.insert(next, changes.clone());
            if result.len() == 10 {
                break;
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

    return sum as i64;
}

pub fn part2(input: String) -> i64 {
    let lines = input.lines();
    let mut sum = 0;
    for line in lines {
        let secret = line.parse::<u64>().unwrap();
        let result = calculate_price(secret, 2000);
        sum += result;
    }

    return sum as i64;
}
