pub fn part1(input: String) -> usize {
    return input.len()
}

pub fn part2(input:String) -> usize {
    return input.len()
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

pub fn main() {
    let path = "../".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match 
    fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
