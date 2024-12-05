use day05::{adjust_positions_based_on_rule, is_valid, parse_input};
use std::fs;

pub fn part1(input: String) -> i64 {
    let (rules, mut updates) = parse_input(input);

    let mut count: i64 = 0;
    for update in updates.iter_mut() {
        let (valid, _rule) = is_valid(update, &rules);
        if valid {
            count += update[update.len() / 2] as i64;
        }
    }
    return count;
}

pub fn part2(input: String) -> i64 {
    let (rules, mut updates) = parse_input(input);

    let mut count: i64 = 0;
    for update in updates.iter_mut() {
        let (mut valid, ref mut rule) = is_valid(update, &rules);

        if !valid && update.len() > 0 {
            while !valid {
                adjust_positions_based_on_rule(update, rule);
                (valid, *rule) = is_valid(update, &rules);
            }
            count += update[update.len() / 2] as i64;
        }
    }
    return count;
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
        143
    )]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }

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
        123
    )]
    fn test2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
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
