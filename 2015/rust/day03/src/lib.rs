pub fn part1(left: u64, right: u64) -> u64 {
    left + right
}

pub fn part2(input:&str) -> u64 {
    return 0;
}

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::*;

    #[rstest]
    fn it_works() {
        let result = part1(2, 2);
        assert_eq!(result, 4);
    }
}
