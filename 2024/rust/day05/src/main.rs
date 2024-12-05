use std::fs;

pub fn part1(input: String) -> i64 {
    let rules: Vec<(i32, i32)> = Vec::new();
    let updates: Vec<Vec<i32>> = Vec::new();
    let mut second = false;
    for line in input.lines().map(|l| l.trim()) {
        if line.len() == 0 {
            second = true;
            break;
        }
        if !second {
            let pair = line.split('|').collect();
            rules.push((pair.0, pair.1));
        } else {
            updates.push(line.split(',').map(|n| n.try_into()).collect());
        }
    }
    let parts: Vec<String> = input.split("\n\n").map(|s| s.to_string()).collect();
    return rules.count().try_into().unwrap();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::first(
        "47|53
    97|13
    97|61
    97|47
    75|29
    61|13
    75|53
    29|13
    97|29
    53|29
    61|53
    97|53
    61|29
    47|13
    75|47
    97|75
    47|61
    75|61
    47|29
    75|13
    53|13
    
    75,47,61,53,29
    97,61,53,29,13
    75,29,13
    75,97,47,61,53
    61,13,29
    97,13,75,29,47",
        4
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }
}

pub fn main() {
    let path = "".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
