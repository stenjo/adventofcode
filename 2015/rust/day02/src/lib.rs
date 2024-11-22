
pub fn part1(measures: &str) -> usize {
    let parts: Vec<usize> = measures.split('x').map(|x| x.parse().expect("Invalid number")).collect();
    let (l, w, h) = (parts[0], parts[1], parts[2]);

    let f = l * w;
    let s = w * h;
    let t = h * l;
    return 2 * f + 2 * s + 2 * t + f.min(s).min(t);
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
    #[case::size_2x1x1("2x1x1", 11)]
    #[case::size_2x3x4("2x3x4", 52)]
    #[case::size_1x1x10("1x1x10", 42)]
    fn package(#[case] measures: &str, #[case] expected: usize) {
        assert_eq!(expected, part1(measures));
    }
}
