use std::collections::HashSet;

pub fn part1(input: String) -> usize {
    let mut x = 0;
    let mut y: usize = 0;
    let tup: (usize, usize) = (x,y);
    let mut houses  = HashSet::new();
    houses.insert(tup);
    for c in input.chars() {
        match c {
            '>' => x += 1,
            'v' => y +=1, 
            _ => ()
        }
        let tup: (usize, usize) = (x,y);
        houses.insert(tup);
    }
    return houses.len()
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
    #[case::first(">", 2)]
    fn it_works(#[case] input: String, #[case]result : usize) {
        assert_eq!(result, part1(input));
    }
}
