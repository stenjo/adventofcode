use std::fs;

pub fn part1(measures: String) -> i64 {
    let measure_list: Vec<&str> = measures.split("\n").collect();
    let mut paper_length = 0;
    for measure in measure_list {
        if measure.is_empty() {
            continue;
        }
        let parts: Vec<i64> = measure.split('x').map(|x| x.parse().expect("Invalid number")).collect();
        let (l, w, h) = (parts[0], parts[1], parts[2]);
        
        let f = l * w;
        let s = w * h;
        let t = h * l;
        paper_length += 2 * f + 2 * s + 2 * t + f.min(s).min(t);
    }
    return  paper_length;
}

pub fn part2(measures: String) -> i64 {
    let measure_list: Vec<&str> = measures.split("\n").collect();
    let mut ribbon_length = 0;
    for measure in measure_list {
        if measure.is_empty() {
            continue;
        }
        let parts: Vec<i64> = measure.split('x').map(|x| x.parse().expect("Invalid number")).collect();
        let (l, w, h) = (parts[0], parts[1], parts[2]);

        ribbon_length += 2*l + 2*w + 2 * h + l*w*h;
    }
    return ribbon_length;
}

pub fn main() {
    let path = std::env::args().nth(1).expect("Expected input argument");
    let input = match 
    fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
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
    #[case::size_2x3x4("2x3x4", 58)]
    #[case::size_1x1x10("1x1x10", 43)]
    #[case::size_joint("1x1x10\n2x3x4", 101)]
    fn package(#[case] measures: String, #[case] expected: i64) {
        assert_eq!(expected, part1(measures));
    }

    #[rstest]
    #[case::size_1x1x1("1x1x1", 7)]
    fn ribbon(#[case] measures: String, #[case] expected: i64) {
        assert_eq!(expected, part2(measures));
    }
}
