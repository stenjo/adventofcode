pub fn part1(input: String) -> usize {
    return input.len()
}

pub fn part2(input:String) -> usize {
    return input.len()
}

pub fn main() {
    let input = std::env::args().nth(1).expect("Expected input argument");
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));

}

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::*;

    #[rstest]
    #[case::first("data", 4)]
    fn it_works(#[case] input: String, #[case]result : usize) {
        assert_eq!(result, part1(input));
    }
}
