use assert_cmd::Command;

#[cfg(test)]
mod tests {
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
        use day05::part1;

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
        use day05::part2;

        assert_eq!(result, part2(input));
    }
}

#[test]
fn test_part1_success() {
    Command::cargo_bin("day05")
        .unwrap()
        .arg("../../data/day05.txt")
        .assert()
        .success()
        .stdout("5639\n5273\n");
}
