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
pub fn _parse_input(input: String) -> (Vec<(i32, i32)>, Vec<Vec<i32>>) {
    // Split the input into sections using the empty line as a delimiter
    let mut sections = input.split("\n\n");

    // Parse the rules section
    let rules: Vec<(i32, i32)> = sections
        .next()
        .unwrap_or("") // Handle missing sections gracefully
        .lines()
        .map(|line| {
            let mut parts = line.split('|');
            let left = parts.next().unwrap().trim().parse::<i32>().unwrap();
            let right = parts.next().unwrap().trim().parse::<i32>().unwrap();
            (left, right)
        })
        .collect();

    // Parse the updates section
    let updates: Vec<Vec<i32>> = sections
        .next()
        .unwrap_or("")
        .lines()
        .map(|line| {
            line.split(',')
                .filter_map(|n| n.trim().parse::<i32>().ok())
                .collect()
        })
        .collect();

    (rules, updates)
}

pub fn is_valid(update: &Vec<i32>, rules: &Vec<(i32, i32)>) -> (bool, (i32, i32)) {
    let mut valid = update.len() > 0;
    let mut failing_rule = (0, 0);
    for rule in rules.iter() {
        if let (Some(first), Some(last)) = (
            update.iter().position(|&x| x == rule.0),
            update.iter().position(|&x| x == rule.1),
        ) {
            if first > last {
                valid = false;
                failing_rule = *rule;
            }
        }
    }
    (valid, failing_rule)
}

pub fn swap_positions(update: &mut Vec<i32>, rule: &mut (i32, i32)) {
    if let (Some(first), Some(second)) = (
        update.iter().position(|&x| x == rule.0),
        update.iter().position(|&x| x == rule.1),
    ) {
        let element = update.remove(first);
        let adjusted = if first < second { second - 1 } else { second };
        update.insert(adjusted, element);
    }
}

pub fn part1(input: String) -> i64 {
    let (rules, mut updates) = parse_input(input);

    let mut count: i64 = 0;
    for update in updates.iter_mut() {
        let (valid, _rule) = is_valid(update, &rules);
        if valid {
            count += update[update.len() / 2] as i64;
        }
    }
    return count;
}

pub fn part2(input: String) -> i64 {
    let (rules, mut updates) = parse_input(input);

    let mut count: i64 = 0;
    for update in updates.iter_mut() {
        let (mut valid, ref mut rule) = is_valid(update, &rules);

        if !valid && update.len() > 0 {
            while !valid {
                swap_positions(update, rule);
                (valid, *rule) = is_valid(update, &rules);
            }
            count += update[update.len() / 2] as i64;
        }
    }
    return count;
}
