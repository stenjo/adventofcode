use memory::Memory;

pub mod loc;
pub mod memory;
use loc::Loc;

pub fn part1(input: String) -> i64 {
    let mut m = Memory::new(input.as_str(), (70, 70));

    m.drop(1024);
    let path = m.least_cost_distance();

    // m.print(path.clone());

    let cost = path.get(&m.memory[&Loc { x: 70, y: 70 }]).unwrap();

    return *cost as i64;
}

pub fn part2(input: String) -> String {
    let mut m = Memory::new(input.as_str(), (70, 70));
    let exit = Loc { x: 70, y: 70 };
    for i in 0..m.bytes.len() {
        m.drop_byte(i);
        let path = m.least_cost_distance();
        let exit_node = m.memory[&exit];
        if !path.contains_key(&exit_node) {
            let (x, y) = m.bytes[i].as_tuple();
            return format!("{},{}", x, y);
        }
    }
    return "Not found".to_string();
}
