use crate::loc::LocMap;

pub struct Starship {
    pub codes: Vec<String>,
    pub pad1: LocMap,
    pub pad2: LocMap,
    pub pad3: LocMap,
}

impl Starship {
    pub fn new(input: &str) -> Self {
        let mut codes = vec![];
        let pad1 = LocMap::new("789\n456\n123\n 0A");
        let pad2 = LocMap::new(" ^A\n<v>");
        let pad3 = LocMap::new(" ^A\n<v>");
        for ln in input.lines() {
            codes.push(ln.to_string());
        }
        Self {
            codes,
            pad1,
            pad2,
            pad3,
        }
    }

    pub fn complexity(&mut self) -> i64 {
        let mut complexity = 0;
        for ln in self.codes.clone() {
            let num = ln[0..3].parse::<i64>().unwrap();
            let keys = self.get_keypresses(ln.as_str());
            complexity += num * keys.len() as i64;
        }
        complexity
    }

    fn get_keypresses(&mut self, ln: &str) -> Vec<char> {
        let mut keys = ln.chars();

        let mut first = Vec::new();
        while let Some(c) = keys.next() {
            let (_, keys) = self.pad1.dijkstra_pri(c);
            first.extend(keys);
            first.push('A');
        }
        // println!("{:?}", first.iter().collect::<String>());

        let mut second: Vec<char> = Vec::new();
        first.reverse();
        while let Some(c2) = first.pop() {
            let (_, keys) = self.pad2.dijkstra_pri(c2);
            second.extend(keys);
            second.push('A');
        }
        // println!("{:?}", second.iter().collect::<String>());

        let mut third: Vec<char> = Vec::new();
        second.reverse();
        while let Some(c3) = second.pop() {
            let (_, keys) = self.pad3.dijkstra_pri(c3);
            third.extend(keys);
            third.push('A');
        }
        // println!("{:?}", third.iter().collect::<String>());
        third
    }
}
