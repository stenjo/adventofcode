use std::collections::HashMap;

pub struct OpCode {
    pub op: String,
    pub a: i64,
    pub b: i64,
    pub c: i64,
}

#[derive(Clone)]
pub struct Computer {
    pub program: Vec<i64>,
    pub reg: HashMap<char, u128>,
    pub ip: i32,
    pub output: Vec<i64>,
}

impl Computer {
    pub fn new(input: &str) -> Self {
        let mut program: Vec<i64> = Vec::new();
        let mut reg: HashMap<char, u128> = HashMap::from([('A', 0), ('B', 0), ('C', 0)]);
        let ip: i32 = 0;

        let mut parts = input.split("\n\n");
        let (state, prog) = (parts.next().unwrap(), parts.next().unwrap());
        let registers = state.lines();
        for reg_line in registers {
            let mut reg_parts = reg_line.split(":");
            let register = reg_parts
                .next()
                .unwrap()
                .split(" ")
                .last()
                .unwrap()
                .chars()
                .next()
                .unwrap();
            let value_str = reg_parts.next().unwrap().trim();
            let value = value_str.parse().unwrap();
            reg.insert(register, value);
        }

        for instr in prog.split(":").last().unwrap().trim().split(",") {
            let i: i64 = instr.parse().unwrap();
            program.push(i);
        }

        Self {
            program,
            reg,
            ip,
            output: Vec::new(),
        }
    }

    pub fn step(&mut self) -> i64 {
        let code = self.program[self.ip as usize];
        let op = self.program[(self.ip + 1) as usize];
        let result: i64 = match code {
            0 => self.adv(op),
            1 => self.bxl(op),
            2 => self.bst(op),
            3 => self.jnz(op),
            4 => self.bxc(op),
            5 => self.out(op),
            6 => self.bdv(op),
            7 => self.cdv(op),
            _ => panic!("Unknown opcode: {}", code),
        };
        self.ip += 2;
        return result;
    }

    pub fn combo(&self, op: i64) -> i64 {
        let a = self.reg.get(&'A').unwrap();
        let b = self.reg.get(&'B').unwrap();
        let c = self.reg.get(&'C').unwrap();

        return match op {
            0 | 1 | 2 | 3 => op,
            4 => a.clone() as i64,
            5 => b.clone() as i64,
            6 => c.clone() as i64,
            _ => panic!("Unknown operand: {}", op),
        };
    }

    pub fn adv(&mut self, op: i64) -> i64 {
        let result = self.reg.get(&'A').unwrap() / (1 << self.combo(op));
        self.reg.insert('A', result);
        return result as i64;
    }

    pub fn bxl(&mut self, op: i64) -> i64 {
        let b = self.reg.get(&'B').unwrap();
        let result = b ^ op as u128;
        self.reg.insert('B', result);
        return result as i64;
    }

    pub fn bst(&mut self, op: i64) -> i64 {
        let result = self.combo(op) % 8;
        self.reg.insert('B', result as u128);
        // println!("B: {:?}, from combo({}) -> B:{}", result, op, result);
        return result as i64;
    }

    fn jnz(&mut self, op: i64) -> i64 {
        let a = self.reg.get(&'A').unwrap();
        if *a != 0 {
            self.ip = (op - 2) as i32;
            return op as i64;
        }
        return 0;
    }

    fn bxc(&mut self, _op: i64) -> i64 {
        let b = self.reg.get(&'B').unwrap();
        let c = self.reg.get(&'C').unwrap();

        let result = b ^ c;
        self.reg.insert('B', result);
        return result as i64;
    }

    fn out(&mut self, op: i64) -> i64 {
        self.output.push(self.combo(op) % 8);
        // println!(
        //     "Out: {:?}, from combo({}) -> B:{}",
        //     self.output.last().unwrap(),
        //     op,
        //     self.reg.get(&'B').unwrap()
        // );
        return self.output.last().unwrap().clone();
    }

    fn bdv(&mut self, op: i64) -> i64 {
        let result = self.reg.get(&'A').unwrap() / (1 << self.combo(op));
        self.reg.insert('B', result);
        return result as i64;
    }

    fn cdv(&mut self, op: i64) -> i64 {
        let result = self.reg.get(&'A').unwrap() / (1 << self.combo(op));
        self.reg.insert('C', result);
        return result as i64;
    }

    pub(crate) fn output(&self) -> Vec<i64> {
        return self.output.clone();
    }

    pub fn run(&mut self) -> Vec<i64> {
        while self.ip < self.program.len() as i32 {
            self.step();
        }
        return self.output();
    }

    pub(crate) fn run_to_copy(&self) -> u128 {
        let mut take = 1;
        let mut shifter: usize = 0;
        let mut initial: u128 = 0;
        let mut working: u128 = initial;
        let mut i = 0;
        println!(
            "Initial: {:b}, target: {:o}",
            initial,
            vec_as_u128(take, self.program.clone())
        );
        let mut hash = vec_as_u128(take, self.program.clone());
        let original = self.clone();
        loop {
            let mut c = original.clone();
            c.reg.insert('A', working);
            c.run();
            let out = vec_as_u128(take, c.output.clone());

            if i > 1024 {
                // println!(
                //     "Increment {} takes too long. Trying: {} (bit:{})",
                //     (1 as u128) << shifter,
                //     (1 as u128) << (shifter + 1),
                //     shifter
                // );
                shifter += 1;
                if shifter > 64 {
                    println!("Fail! Shifter: {}, Take: {}", shifter, take);
                    return 0;
                }
                working = initial;
                i = 0;
            }
            if out == hash {
                initial = working;
                if take >= self.program.len() {
                    println!("Winner: {} -> Initial: {} ({})", out, initial, i);
                    return initial as u128;
                }
                println!("Out: {} -> first {} digits done. {}", out, take, initial);
                take += 1;
                hash = vec_as_u128(take, self.program.clone());
            }
            working += (1 as u128) << shifter;
            i += 1;
        }
    }
}

fn vec_as_u128(take: usize, v: Vec<i64>) -> u128 {
    let out: u128 = v
        .iter()
        .take(take)
        .map(|p| p.to_string())
        .collect::<Vec<String>>()
        .join("")
        .parse()
        .unwrap();
    out
}
