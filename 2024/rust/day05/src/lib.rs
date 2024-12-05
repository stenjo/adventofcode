pub fn parse_input(input: String) -> (Vec<(i32, i32)>, Vec<Vec<i32>>) {
    let mut rules: Vec<(i32, i32)> = Vec::new();
    let mut updates: Vec<Vec<i32>> = Vec::new();
    let mut second = false;
    for line in input.lines().map(|l| l.trim()) {
        if line.len() == 0 {
            second = true;
        }
        if !second {
            let pair: Vec<&str> = line.split('|').collect();
            rules.push((pair[0].parse().unwrap(), pair[1].parse().unwrap()));
        } else {
            updates.push(
                line.split(',')
                    .filter_map(|n| n.parse::<i32>().ok())
                    .collect(),
            );
        }
    }
    (rules, updates)
}

pub fn is_valid(update: &Vec<i32>, rules: &Vec<(i32, i32)>) -> (bool, (i32, i32)) {
    let mut valid = update.len() > 0;
    let mut failing_rule = (0, 0);
    for rule in rules.iter() {
        if update.contains(&rule.0) && update.contains(&rule.1) {
            let pos1: usize = update
                .iter()
                .position(|&x| x == rule.0)
                .unwrap_or(usize::MAX);
            let pos2: usize = update
                .iter()
                .position(|&x| x == rule.1)
                .unwrap_or(usize::MAX);
            if pos1 == usize::MAX || pos2 == usize::MAX || pos1 > pos2 {
                valid = false;
                if pos1 > pos2 {
                    failing_rule = *rule;
                }
            }
        }
    }
    (valid, failing_rule)
}

pub fn adjust_positions_based_on_rule(update: &mut Vec<i32>, rule: &mut (i32, i32)) {
    let first_pos = update.iter().position(|&x| x == rule.0).unwrap();
    let second_pos = update.iter().position(|&x| x == rule.1).unwrap();
    update.remove(first_pos);
    update.insert(second_pos, rule.0);
}
