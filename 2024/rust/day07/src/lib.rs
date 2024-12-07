#[derive(Debug, Clone)]
pub struct Equation {
    pub val: i64,
    pub nums: Vec<i64>,
}

impl Equation {
    pub fn new(input: &str) -> Result<Self, String> {
        let mut parts = input.split(':');
        let val = parts
            .next()
            .ok_or("Missing value")?
            .trim()
            .parse::<i64>()
            .map_err(|_| "Failed to parse value")?;

        let nums = parts
            .next()
            .ok_or("Missing numbers")?
            .split_whitespace()
            .map(|n| n.parse::<i64>().map_err(|_| "Failed to parse number"))
            .collect::<Result<Vec<_>, _>>()?;

        Ok(Self { val, nums })
    }

    pub fn gen_operations(&self, length: usize) -> Vec<Vec<char>> {
        let mut operations = Vec::new();
        let operators = vec!['*', '+'];

        for combination in (0..2_usize.pow(length as u32)).map(|n| {
            (0..length)
                .map(|i| {
                    if n & (1 << i) != 0 {
                        operators[1] // '+'
                    } else {
                        operators[0] // '*'
                    }
                })
                .collect::<Vec<char>>()
        }) {
            operations.push(combination);
        }

        operations
    }

    pub fn solve(&self) -> i64 {
        let mut options = self.gen_operations(self.nums.len() - 1);
        while let Some(option) = options.pop() {
            // println!("option: {:?}", option);
            if self.calculate(option) {
                return self.val;
            }
        }
        return 0;
    }

    fn calculate(&self, mut operators: Vec<char>) -> bool {
        let mut numbers: Vec<i64> = self.nums.clone().into_iter().rev().collect();
        let mut result = numbers.pop().unwrap();

        let mut s = "".to_string() + &result.to_string();
        if result > self.val {
            return false;
        } else if result == self.val {
            return true;
        }
        while let Some(n) = numbers.pop() {
            if let Some(operator) = operators.pop() {
                if operator == '*' {
                    result *= n;
                    s += " * ";
                    s += &n.to_string();
                } else if operator == '+' {
                    result += n;
                    s += " + ";
                    s += &n.to_string();
                }

                if result > self.val {
                    // println!("failure: {}", s);
                    return false;
                } else if result == self.val {
                    // println!("success: {}", s);
                    return true;
                }
            } else {
                // println!("no operator.");
                break;
            }
        }
        return false;
    }
}

#[derive(Debug, Clone)]
pub struct Equator {
    pub equations: Vec<Equation>,
}

impl Equator {
    pub fn new(input: String) -> Self {
        let equations = input
            .lines()
            .filter_map(|line| Equation::new(line.trim()).ok()) // Keep only successful results
            .collect();
        Self { equations }
    }
}

pub fn part1(input: String) -> i64 {
    let mut calibration: i64 = 0;
    let solver: Equator = Equator::new(input);

    for e in solver.equations {
        calibration += e.solve();
    }
    return calibration;
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}
