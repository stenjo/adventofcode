use std::collections::{HashMap, VecDeque};

pub struct Logic {
    pub gates: HashMap<String, Gate>,
}

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
            println!("{}: {:?}", name, output);
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
        let dk = self
            .gates
            .keys()
            .map(|s| s.as_str())
            .collect::<Vec<&str>>()
            .join(",");
        println!("{}", dk);
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
}
