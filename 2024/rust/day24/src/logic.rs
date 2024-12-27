use std::collections::{HashMap, VecDeque};

pub struct Logic {
    pub gates: HashMap<String, Gate>,
}

#[derive(Clone, Debug, PartialEq, Eq)]
pub struct Gate {
    inputs: Vec<String>,
    operation: String,
    output: Option<bool>,
    name: String,
}
impl Gate {
    fn new(line: &str) -> Self {
        if line.contains("->") {
            let mut input = line.split(" -> ");
            let operation = input.next().unwrap();
            let name = input.next().unwrap();
            let mut inputs = operation.split(" ");
            let mut gate = Self {
                inputs: Vec::new(),
                operation: String::new(),
                output: None,
                name: name.to_string(),
            };
            gate.inputs.push(inputs.next().unwrap().to_string());
            gate.operation = inputs.next().unwrap().to_string();
            gate.inputs.push(inputs.next().unwrap().to_string());
            return gate;
        }
        let mut input = line.split(": ");
        let name = input.next().unwrap();
        if let Some(state) = input.next() {
            let output = match state {
                "0" => Some(false),
                "1" => Some(true),
                _ => panic!("Invalid state"),
            };
            // println!("{}: {:?}", name, output);
            Self {
                inputs: Vec::new(),
                operation: String::new(),
                output,
                name: name.to_string(),
            }
        } else {
            Self {
                inputs: Vec::new(),
                operation: String::new(),
                output: None,
                name: name.to_string(),
            }
        }
    }

    fn calculate(&mut self, first: Option<bool>, second: Option<bool>) {
        if first.is_none() || second.is_none() {
            self.output = None;
            return;
        }
        let output = match self.operation.as_str() {
            "AND" => first.unwrap() && second.unwrap(),
            "OR" => first.unwrap() || second.unwrap(),
            "XOR" => first.unwrap() != second.unwrap(),
            _ => panic!("Invalid operation"),
        };
        self.output = Some(output);
    }
}

impl Logic {
    pub fn new(inputs: &str) -> Self {
        let mut gates: HashMap<String, Gate> = HashMap::new();
        for line in inputs.lines() {
            let gate = Gate::new(line);
            gates.insert(gate.name.clone(), gate);
        }
        return Self { gates };
    }

    pub fn run(&mut self) -> i64 {
        let number: i64 = 0;
        let mut unfinished: VecDeque<String> = VecDeque::new();
        for gate in self.gates.values() {
            if gate.output.is_none() {
                unfinished.push_back(gate.name.clone());
            }
        }
        while !unfinished.is_empty() {
            let gate_name = unfinished.pop_front().unwrap();
            let gate = self.gates.get(gate_name.as_str()).unwrap();
            if gate.inputs.len() != 2 {
                println!("Invalid number of inputs: {}", gate.name);
                continue;
            }
            let (first_output, second_output) = {
                let mut first_output = None;
                if let Some(first_input) = gate.inputs.get(0).clone() {
                    first_output = self.gates.get(first_input).and_then(|g| g.output);
                }
                let mut second_output = None;
                if let Some(second_input) = gate.inputs.get(1).clone() {
                    second_output = self.gates.get(second_input).and_then(|g| g.output);
                }
                (first_output, second_output)
            };
            if let Some(gate) = self.gates.get_mut(gate_name.as_str()) {
                if first_output.is_some() && second_output.is_some() {
                    gate.calculate(first_output, second_output);
                } else {
                    unfinished.push_back(gate.name.clone());
                }
            }
        }
        number
    }

    pub fn number(&mut self) -> i64 {
        let digits: Vec<String> = self
            .gates
            .keys()
            .filter(|&x| x.starts_with("z"))
            .cloned()
            .collect();
        let mut number: i64 = 0;
        for digit in digits {
            if let Some(gate) = self.gates.get(&digit) {
                if let Some(output) = gate.output {
                    if output {
                        number |= 1 << digit[1..].parse::<i64>().unwrap();
                    }
                }
            }
        }
        return number;
    }

    pub fn swapped_gates(&mut self) -> i64 {
        self.run();
        let x = self.get_number('x');
        let y = self.get_number('y');
        let z = self.get_number('z');

        println!("x: {}", x);
        println!("y: {}", y);
        println!("z: {:b}", z);
        println!("-: {:b}", x + y);

        let errors = self.get_error_positions(x + y, z);
        for e in errors.iter() {
            println!("Error: {}", e);
        }
        let candidates = self.get_candidates("z02".to_string());
        for c in candidates.iter() {
            println!("Candidate: {}", c);
        }
        z
    }

    pub fn run_adder(&self, bit: usize) -> bool {
        let start_x = self.gates.get(format!("x{:02}", bit).as_str()).unwrap();
        let start_y = self.gates.get(format!("y{:02}", bit).as_str()).unwrap();
        let z_0 = self.gates.get(format!("z{:02}", bit).as_str()).unwrap();
        let z_1 = self.gates.get(format!("z{:02}", bit + 1).as_str()).unwrap();

        for (x, y) in vec![(0, 0), (0, 1), (1, 0), (1, 1)] {
            let gate_stack: Vec<Gate> = Vec::new();
            let x_gates = self.find_input_x(bit, z_0);
            println!("X: {:?}", x_gates);
        }
        true
    }
    pub fn find_input_x(&self, bit: usize, gate: &Gate) -> (Option<Gate>, Vec<Gate>) {
        for i in gate.inputs.iter() {
            if i.starts_with("x") && i[1..].parse::<usize>().unwrap() == bit {
                return (Some(gate.clone()), vec![]);
            } else {
                if let Some(parent) = self.gates.get(i) {
                    let (g, stack) = self.find_input_x(bit, parent);
                    if g.is_some() {
                        return (
                            g.clone(),
                            vec![g.unwrap().clone()]
                                .into_iter()
                                .chain(stack.into_iter())
                                .collect(),
                        );
                    }
                    return (None, vec![]);
                }
            }
        }
        return (None, vec![]);
    }
    pub fn check_adder(&self, pos: usize) -> bool {
        let x = 1 << pos;
        let y = 1 << pos;
        let z = 1 << pos;
        true
    }
    fn get_number(&self, prefix: char) -> i64 {
        let digits: Vec<String> = self
            .gates
            .keys()
            .filter(|&n| n.starts_with(prefix))
            .cloned()
            .collect();
        let mut number: i64 = 0;
        for d in digits {
            if let Some(gate) = self.gates.get::<String>(&d) {
                if let Some(output) = gate.output {
                    if output {
                        number |= 1 << d[1..].parse::<i64>().unwrap();
                    }
                }
            }
        }
        number
    }
    pub fn visualize(&self) {
        for (name, gate) in &self.gates {
            let inputs = gate.inputs.join(", ");
            let output = match gate.output {
                Some(true) => "1",
                Some(false) => "0",
                None => "None",
            };
            println!(
                "Gate {}: {} -> {} [{}]",
                name, inputs, gate.operation, output
            );
        }

        let x_outputs: Vec<_> = self.gates.keys().filter(|k| k.starts_with('x')).collect();
        let y_outputs: Vec<_> = self.gates.keys().filter(|k| k.starts_with('y')).collect();
        let z_outputs: Vec<_> = self.gates.keys().filter(|k| k.starts_with('z')).collect();

        println!("\nX-nodes:");
        for x in x_outputs {
            if let Some(gate) = self.gates.get(x) {
                println!("{}: {:?}", x, gate.output);
            }
        }

        println!("\nY-nodes:");
        for y in y_outputs {
            if let Some(gate) = self.gates.get(y) {
                println!("{}: {:?}", y, gate.output);
            }
        }

        println!("\nZ-nodes:");
        for z in z_outputs {
            if let Some(gate) = self.gates.get(z) {
                println!("{}: {:?}", z, gate.output);
            }
        }
    }

    fn get_error_positions(&self, y: i64, z: i64) -> Vec<String> {
        let mut errors: Vec<String> = Vec::new();
        let mut a_bits = format!("{:b}", y).chars().collect::<Vec<char>>();
        let mut b_bits = format!("{:b}", z).chars().collect::<Vec<char>>();
        let mut pos = 0;
        while a_bits.len() > 0 && b_bits.len() > 0 {
            if let Some(a_bit) = a_bits.pop() {
                if let Some(b_bit) = b_bits.pop() {
                    if a_bit != b_bit {
                        errors.push(format!("z{:02}", pos));
                        // println!("{:?} -> {:?}", pos, errors);
                    }
                }
            }
            pos += 1;
        }
        errors
    }

    fn get_candidates(&self, errors: String) -> Vec<String> {
        let mut candidates: Vec<String> = Vec::new();
        let mut stack: Vec<String> = Vec::new();
        stack.push(errors);
        while !stack.is_empty() {
            let current = stack.pop().unwrap();
            let gate = self.gates.get(&current).unwrap();
            for input in &gate.inputs {
                candidates.push(input.clone());
                stack.push(input.clone());
            }
        }

        candidates
    }
}
