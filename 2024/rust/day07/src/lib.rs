#[derive(Debug, Clone)]
pub struct Equation {
    pub val: i64,
    pub nums: Vec<Vec<i64>>,
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

        let numbers: Vec<i64> = parts
            .next()
            .ok_or("Missing numbers")?
            .split_whitespace()
            .map(|n| n.parse::<i64>().map_err(|_| "Failed to parse number"))
            .collect::<Result<Vec<_>, _>>()?;
        let nums = vec![numbers];
        Ok(Self { val, nums })
    }

    pub fn variations(&self, nums: Vec<i64>) -> Vec<Vec<i64>> {
        let mut variation_list = Vec::new();

        // Base case: If the list has one or zero elements, add it to variations
        if nums.len() <= 1 {
            variation_list.push(nums.clone());
            return variation_list;
        }

        // Iterate through all pairs of consecutive numbers
        for i in 0..nums.len() - 1 {
            let mut new_nums = nums.clone();
            let merged_value = format!("{}{}", new_nums[i], new_nums[i + 1])
                .parse::<i64>()
                .unwrap();
            new_nums[i] = merged_value; // Replace the first number with the merged value
            new_nums.remove(i + 1); // Remove the second number

            // Recursively generate variations for the reduced list
            let deeper_variations = self.variations(new_nums);

            // Add all deeper variations to the result
            variation_list.extend(deeper_variations);
        }

        // Also include the current list as a variation
        if nums.iter().sum::<i64>() <= self.val {
            variation_list.push(nums);
        }

        variation_list
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
        for l in self.nums.clone() {
            let mut options = self.gen_operations(l.len() - 1);
            while let Some(option) = options.pop() {
                // println!("option: {:?}", option);
                if self.calculate(option.clone(), l.clone()) {
                    return self.val;
                }
            }
        }
        return 0;
    }

    pub fn calculate(&self, mut operators: Vec<char>, nums: Vec<i64>) -> bool {
        let mut numbers: Vec<i64> = nums.clone().into_iter().rev().collect();
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

    pub fn add_variations(&mut self) {
        let merged = self.variations(self.nums[0].clone());
        self.nums = merged;
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
    let mut calibration: i64 = 0;
    let solver: Equator = Equator::new(input);
    for mut e in solver.equations {
        print!("{}", '.');
        // e.add_variations();
        calibration += e.solve();
    }
    return calibration;
}
