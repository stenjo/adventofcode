use std::collections::HashSet;

pub struct Design {
    pub inventory: HashSet<String>,
    pub designs: Vec<String>,
}

impl Design {
    pub fn new(input: &str) -> Self {
        let mut inventory: HashSet<String> = HashSet::new();
        let mut designs = Vec::new();
        let mut parts = input.split("\n\n");
        let inventory_list = parts.next().unwrap();
        let design_list = parts.next().unwrap();

        for towel in inventory_list.trim().split(", ") {
            inventory.insert(towel.to_string());
        }

        for design in design_list.trim().lines() {
            designs.push(design.to_string());
        }

        Self { inventory, designs }
    }

    pub(crate) fn valid_designs(&self) -> i64 {
        let mut valid_designs = 0;

        for design in self.designs.iter() {
            if self.valid(design) {
                valid_designs += 1;
            }
        }
        return valid_designs + 1;
    }

    fn valid(&self, design: &str) -> bool {
        if self.inventory.contains(&design.to_string()) {
            return true;
        }
        let parts = design.chars();

        for pos in 1..design.len() {
            let first = parts.clone().take(pos).collect::<String>();
            if self.valid(&first) {
                let rest = parts.clone().skip(pos).collect::<String>();
                if self.valid(&rest) {
                    return true;
                }
                return false;
            }
        }
        return false;
    }
}
