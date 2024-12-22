use crate::loc::Loc;
use std::collections::HashMap;

pub struct Keypad {
    pub keys: HashMap<char, Loc>,
}

impl Keypad {
    pub fn new(input: Vec<&str>) -> Self {
        let mut keys = HashMap::new();
        for (y, line) in input.iter().enumerate() {
            for (x, c) in line.chars().enumerate() {
                if c != ' ' {
                    keys.insert(c, Loc::new(x as i64, y as i64));
                }
            }
        }
        Keypad { keys }
    }
    pub fn get_loc(&self, c: char) -> Option<Loc> {
        return self.keys.get(&c).cloned();
    }

    pub fn get_key(&self, loc: &Loc) -> char {
        for (key, value) in self.keys.iter() {
            if value == loc {
                return *key;
            }
        }
        return ' ';
    }

    pub fn get_moves(&self, from: &Loc, to: &Loc) -> Vec<char> {
        let mut moves = vec![];
        let change = Loc::new(to.x - from.x, to.y - from.y);
        while change.x.abs() > 0 {
            if change.x > 0 {
                moves.push('>');
            } else {
                moves.push('<');
            }
        }
        while change.y.abs() > 0 {
            if change.y > 0 {
                moves.push('v');
            } else {
                moves.push('^');
            }
        }
        moves.push('A');
        return moves;
    }
}

pub struct Starship {
    pub codes: Vec<String>,
    pub keypads: Vec<Keypad>,
}

impl Starship {
    pub fn new(input: &str) -> Self {
        let mut keypads = vec![];
        keypads.push(Keypad::new(vec!["789", "456", "123", " 0A"]));

        let mut codes: Vec<String> = vec![];
        for line in input.lines() {
            codes.push(line.to_string());
        }

        Starship { codes, keypads }
    }

    pub fn complexity(&self, code: &str) -> i64 {
        let keypresses = self
            .codes
            .iter()
            .map(|c| {
                let mut loc = Loc::new(1, 1);
                let mut keypresses = 0;
                for ch in c.chars() {
                    let keypad = self
                        .keypads
                        .iter()
                        .find(|k| k.get_loc(ch).is_some())
                        .unwrap();
                    let target = keypad.get_loc(ch).unwrap();
                    let moves = keypad.get_moves(&loc, &target);
                    keypresses += moves.len() as i64;
                    loc = target;
                }
                keypresses
            })
            .collect::<Vec<i64>>();
        return keypresses.len() as i64 * self.numeric(code);
    }

    fn numeric(&self, code: &str) -> i64 {
        return code
            .chars()
            .take(3)
            .collect::<String>()
            .parse::<i64>()
            .unwrap();
    }
}
