
pub fn part1(measures: &str) -> u64 {
    let [l,w,h] = measures.split("x").collect().as_slice();
    return 7
}

#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::*;

// A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper 
// plus 6 square feet of slack, for a total of 58 square feet.

// A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper 
// plus 1 square foot of slack, for a total of 43 square feet.

    #[rstest]
    #[case::size_1x1x1("1x1x1", 7)]
    #[case::size_2x1x1("2x1x1", 9)]
    fn package(#[case] measures: &str, #[case] expected: u64) {
        assert_eq!(expected, part1(measures));
    }
}
