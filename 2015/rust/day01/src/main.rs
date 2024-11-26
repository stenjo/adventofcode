use std::fs;

pub fn part1(floors: String) -> i64 {
        let _ = floors;
        let mut level:i64 = 0;
        for c in floors.chars()  {
            if c == '('  {
                level += 1;
            }
            else {
                level -= 1;
            }
        }
        return level;
    }
    
    pub fn part2(floors: String) ->usize {
        let _ = floors;
        let mut level:i64 = 0;
        for (i,c) in floors.chars().enumerate()  {
            level += if c == '(' { 1 } else { -1};
            if level < 0 {
                return i+1;
            }
        }

        return 0;
    }
    
#[cfg(test)]
mod tests {
    use rstest::rstest;
    use super::*;

    #[rstest]
    #[case("((((", 4)] // Case name: four_floors_up
    #[case("(())", 0)]
    #[case("(()(", 2)]
    #[case("(()(()(", 3)]
    #[case("(()(()(", 3)]
    #[case("))(((((", 3)]
    #[case("())", -1)]
    #[case(")))", -3)]
    #[case(")())())", -3)]
    fn day01_1(#[case] input:String, #[case] expected: i64) {
        let result: i64 = part1(input);
        assert_eq!(result, expected);
    }

    #[rstest]
    #[case::one_floor(")", 1)]
    #[case::five_floors("()())", 5)]
    #[case::nine_floors("()()()())", 9)] // Case name: stair_training
    fn day01_2(#[case] input:String, #[case] expected: usize) {
        assert_eq!(expected, part2(input));
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