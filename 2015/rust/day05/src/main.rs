use std::{collections::HashSet, fs};

fn wowels(input: &str) -> bool {
    let mut w = 0;
    for c in input.chars() {
        if "aeiou".contains(c) {
            w += 1;
            if w > 2 {
                return true;
            }
        }
    }
    return false;
}

fn twice(input: &str) -> bool {
    let mut l: char = ' ';
    for c in input.chars() {
        if c == l {
            return true;
        }
        l = c;
    }
    return false;
}

fn forbidden(input: &str) -> bool {
    let forbidden_pairs = vec!["ab", "cd", "pq", "xy"];

    // Iterer over alle par av tegn i input-strengen
    for pair in input.chars().collect::<Vec<_>>().windows(2) {
        if let [a, b] = pair {
            let pair_str = format!("{}{}", a, b);
            if forbidden_pairs.contains(&pair_str.as_str()) {
                return false; // Returner false hvis et forbudt par finnes
            }
        }
    }

    true // Returner true hvis ingen forbudte par ble funnet
}

pub fn part1(input: String) -> i64 {
    let mut nice = 0;
    let senteces: Vec<&str> = input.split("\n").collect();
    for sentece in senteces {
        if wowels(sentece) && twice(sentece) && forbidden(sentece) {
            nice += 1;
        }
    }
    return nice;
}

pub fn part2(input: String) -> i64 {
    let mut nice = 0;
    let senteces: Vec<&str> = input.split("\n").collect();
    for sentece in senteces {
        let mut pairs: usize = 0;
        let mut pair_map: HashSet<String> = HashSet::new();
        let mut last: String = "".to_owned();
        for pair in sentece.chars().collect::<Vec<_>>().windows(2) {
            if let [a, b] = pair {
                let pair_str = format!("{}{}", a, b);
                if pair_map.contains(&pair_str) && pair_str != last {
                    pairs += 1;
                } else {
                    pair_map.insert(pair_str.clone());
                }
                last = pair_str.clone();
            }
        }
        let mut repeats: usize = 0;
        let chars: Vec<char> = sentece.chars().collect();
        for (i, c) in chars.iter().enumerate() {
            if i >= 2 && chars[i - 2] == *c {
                repeats += 1;
            }
        }
        if pairs > 0 && repeats > 0 {
            nice += 1;
        }
    }
    return nice;
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[rstest]
    #[case::a("aei", true)]
    #[case::x("xazegov", true)]
    #[case::ae("aeiouaeiouaeiou", true)]
    #[case::ae("dvszwmarrgswjxmb", false)]
    fn wowels_test(#[case] input: &str, #[case] result: bool) {
        assert_eq!(result, wowels(input));
    }

    #[rstest]
    #[case::a("aei", true)]
    #[case::a("aaa", true)]
    #[case::x("xazegov", true)]
    #[case::ae("aeiouaeiouaeiou", true)]
    #[case::ae("dvszwmarrgswjxmb", true)]
    #[case::ae("haegwjzuvuyypxyu", false)]
    fn forbidden_test(#[case] input: &str, #[case] result: bool) {
        assert_eq!(result, forbidden(input));
    }

    #[rstest]
    #[case::first("aeiouaeiouaeiou\ndvszwmarrgswjxmb\nhaegwjzuvuyypxyu", 0)]
    fn test_1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
    }

    #[rstest]
    #[case::first("xxyxx", 1)]
    #[case::first("yyaaaxx", 0)]
    #[case::first("qjhvhtzxzqqjkmpb", 1)]
    #[case::first("uurcxstgmygtbstg", 0)]
    #[case::first("ieodomkazucvgmuy", 0)]
    #[case::first("xxyxx\nqjhvhtzxzqqjkmpb\nuurcxstgmygtbstg\nieodomkazucvgmuy", 2)]
    fn test_2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}

pub fn main() {
    let path = "../".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
