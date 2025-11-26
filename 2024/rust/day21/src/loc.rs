use bimap::{BiHashMap, BiMap};
use core::panic;
use once_cell::sync::Lazy;
use petgraph::algo::dijkstra;
use petgraph::graph::{NodeIndex, UnGraph};
use petgraph::visit::EdgeRef;
use petgraph::{Graph, Undirected};
use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap, HashSet};

#[derive(Debug, Clone, Copy, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Loc {
    pub x: i64,
    pub y: i64,
}
impl Loc {
    pub fn new(x: i64, y: i64) -> Self {
        Self { x, y }
    }
    pub fn new_from_tuple(p: (i64, i64)) -> Self {
        Self { x: p.0, y: p.1 }
    }

    pub fn update(&mut self, p: (i64, i64)) -> Loc {
        self.x = p.0;
        self.y = p.1;
        return self.clone();
    }

    pub fn up(&mut self) -> Loc {
        self.y -= 1;
        return self.clone();
    }

    pub fn down(&mut self) -> Loc {
        self.y += 1;
        return self.clone();
    }

    pub fn left(&mut self) -> Loc {
        self.x -= 1;
        return self.clone();
    }

    pub fn right(&mut self) -> Loc {
        self.x += 1;
        return self.clone();
    }

    pub fn as_tuple(&self) -> (i64, i64) {
        (self.x, self.y)
    }

    pub(crate) fn add(&mut self, v: &Loc) -> Loc {
        self.x += v.x;
        self.y += v.y;
        self.clone()
    }

    pub fn add_teleport(&mut self, v: &Loc, min: &Loc, max: &Loc) -> Loc {
        let width: i64 = max.x - min.x + 1;
        let height: i64 = max.y - min.y + 1;
        self.add(v);
        self.x = (self.x - min.x) % width + min.x;
        if self.x < min.x {
            self.x += width;
        }
        self.y = (self.y - min.y) % height + min.y;
        if self.y < min.y {
            self.y += height;
        }
        self.clone()
    }

    pub fn get_next(&self, dir: char) -> Loc {
        return self.clone().add(DIRECTION.get(&dir).unwrap());
    }
    pub fn get_next_option(&self, dir: char) -> Option<Loc> {
        if let Some(v) = DIRECTION.get(&dir) {
            return Some(self.clone().add(v));
        }
        return None;
    }

    pub fn is_neighbor(&self, other: &Loc) -> bool {
        ((other.x - self.x).abs() == 1 && other.y == self.y)
            || ((other.y - self.y).abs() == 1 && other.x == self.x)
    }
    pub const DIRECTIONS: [char; 4] = ['>', 'v', '<', '^'];

    fn get_dir_to(&self, next: Loc) -> Option<char> {
        for dir in Loc::DIRECTIONS.iter() {
            if next.get_next(*dir) == self.clone() {
                return Some(*dir);
            }
        }
        return None;
    }
}

pub struct LocMap {
    pub map: HashMap<Loc, char>,
    pub graph: Graph<char, i32, Undirected>,
    pub graph_map: BiHashMap<Loc, NodeIndex>,
    pub key_map: BiHashMap<char, Loc>,
    pub weight_map: HashMap<NodeIndex, i32>,
    pub cost: HashMap<Loc, i32>,
    pub min: Loc,
    pub max: Loc,
    pub current: Loc,
}

impl LocMap {
    pub fn new(input: &str) -> Self {
        let mut map: HashMap<Loc, char> = HashMap::new();
        let mut graph = UnGraph::new_undirected();
        let mut graph_map: BiHashMap<Loc, NodeIndex> = BiHashMap::new();
        let mut key_map: BiHashMap<char, Loc> = BiHashMap::new();
        let mut weight_map: HashMap<NodeIndex, i32> = HashMap::new();
        let mut min = Loc::new(0, 0);
        let mut max = Loc::new(0, 0);
        let mut current = Loc::new(0, 0);
        for (y, ln) in input.lines().enumerate() {
            for (x, c) in ln.chars().enumerate() {
                if c != ' ' {
                    let loc = Loc::new(x as i64, y as i64);
                    map.insert(loc.clone(), c);
                    key_map.insert(c, loc.clone());
                    let loc_idx = graph.add_node(c);
                    graph_map.insert(loc.clone(), loc_idx);

                    if x > 0 {
                        let left = Loc::new(x as i64 - 1, y as i64);
                        if let Some(left_idx) = graph_map.get_by_left(&left) {
                            graph.add_edge(loc_idx, *left_idx, 1);
                        }
                    }
                    if y > 0 {
                        let up = Loc::new(x as i64, y as i64 - 1);
                        if let Some(up_idx) = graph_map.get_by_left(&up) {
                            graph.add_edge(loc_idx, *up_idx, 1);
                        }
                    }

                    if c == 'A' {
                        current = loc.clone();
                    }
                    if loc.x < min.x {
                        min.x = loc.x;
                    }
                    if loc.y < min.y {
                        min.y = loc.y;
                    }
                    if loc.x > max.x {
                        max.x = loc.x;
                    }
                    if loc.y > max.y {
                        max.y = loc.y;
                    }
                }
            }
        }

        if let Some(start) = graph_map.get_by_left(&current) {
            weight_map = dijkstra(&graph, *start, None, |e| *e.weight())
        }

        Self {
            map,
            graph,
            graph_map,
            key_map,
            weight_map,
            cost: HashMap::new(),
            min,
            max,
            current,
        }
    }

    pub fn insert(&mut self, loc: Loc, c: char) {
        self.map.insert(loc.clone(), c);
        if loc.x < self.min.x {
            self.min.x = loc.x;
        }
        if loc.y < self.min.y {
            self.min.y = loc.y;
        }
        if loc.x > self.max.x {
            self.max.x = loc.x;
        }
        if loc.y > self.max.y {
            self.max.y = loc.y;
        }
    }

    pub fn get_loc(&self, c: char) -> Loc {
        if let Some(loc) = self.key_map.get_by_left(&c) {
            return loc.clone();
        }
        panic!("Character not found: {}", c);
    }
    pub fn get(&self, loc: &Loc) -> char {
        if let Some(node_idx) = self.graph_map.get_by_left(loc) {
            let c = self.graph[*node_idx];
            if c == match self.map.get(loc) {
                Some(c) => *c,
                None => ' ',
            } {
                return c;
            }
            panic!("Character mismatch: {:?}", loc);
        }
        panic!("Location not found: {:?}", loc);
    }
    pub fn get_cost_option(&mut self, loc: &Loc) -> Option<&i32> {
        if let Some(idx) = self.graph_map.get_by_left(loc) {
            return calc_weight(self, self.graph_map.get_by_right(idx).unwrap());
            // return self.weight_map.get(idx);
        }
        None
        // if self.cost.len() == 0 {
        //     let ref_loc = self.current;
        //     let start_idx = self.graph_map.get_by_left(&ref_loc).unwrap();
        //     let cost = dijkstra(&self.graph, *start_idx, None, |e| *e.weight());
        //     for (&node_idx, c) in cost.iter() {
        //         let ch = self.graph[node_idx];
        //         let l = self.get_loc(ch);
        //         self.cost.insert(l, *c);
        //     }
        // }
        // return self.cost.get(loc);
    }

    pub fn get_option(&self, loc: &Loc) -> Option<char> {
        return self.map.get(loc).cloned();
    }

    pub fn get_next(&self, loc: &Loc, dir: char) -> char {
        self.get(&loc.get_next(dir))
    }

    pub fn get_path(&mut self, start: &Loc, end: &Loc) -> Vec<Loc> {
        let start_idx = self.graph_map.get_by_left(&start).unwrap();
        let end_idx = self.graph_map.get_by_left(&end).unwrap();

        let path =
            shortest_path_with_priority(&self, &self.weight_map, *start_idx, *end_idx).unwrap();
        let mut locs: Vec<Loc> = Vec::new();
        for &l in &path {
            let key = self.graph[l];
            locs.push(self.get_loc(key).clone());
        }
        // (locs.len() as i32, locs)
        locs
    }

    pub fn get_directions(&mut self, start: &Loc, end: &Loc) -> Vec<char> {
        let mut directions: Vec<char> = Vec::new();
        let mut path = self.get_path(start, end);
        path.reverse();
        let mut current = path.pop().unwrap();
        while let Some(next) = path.pop() {
            if let Some(dir) = current.get_dir_to(next) {
                directions.push(dir);
                current = next;
            } else {
                println!("No direction from {:?} to {:?}", current, next);
            }
        }
        directions
    }

    pub fn directions_to(&mut self, to: char) -> Vec<char> {
        let (_, idx_list) = self.dijkstra_pri(to);
        idx_list
    }

    pub fn distance_to(&mut self, to: char) -> i32 {
        let (cost, _) = self.dijkstra_pri(to);
        cost
    }

    pub fn convert(&self, path: &Vec<char>) -> Vec<char> {
        let mut new_path: Vec<char> = Vec::new();
        let mut current = self.current;
        for &dir in path.iter() {
            if dir == 'A' {
                if let Some(cr) = self.get_option(&current) {
                    new_path.push(cr);
                } else {
                    new_path.push('x');
                }
            } else {
                if let Some(next) = current.get_next_option(dir) {
                    current = next;
                } else {
                    println!("No option for {:?} : {}", current, dir);
                }
            }
        }
        new_path
    }

    // pub fn dijkstra_to(&mut self, to: char) -> (i32, Vec<char>) {
    //     let end = self.key_map.get(&to).unwrap();
    //     let start = self.current;
    //     let start_idx = self.graph_map.get(&start).unwrap();
    //     let end_idx = self.graph_map.get(end).unwrap();

    //     let path = dijkstra_with_paths(&self.graph, *start_idx, *end_idx).unwrap();
    //     self.current = end.clone();
    //     let mut keys: Vec<char> = Vec::new();
    //     let mut locs: Vec<Loc> = Vec::new();
    //     let mut dirs: Vec<char> = Vec::new();
    //     for &l in &path {
    //         let key = self.graph[l];
    //         locs.push(self.get_loc(key).clone());
    //         keys.push(key.clone());
    //     }

    //     locs.reverse();
    //     let mut current = locs.pop().unwrap();
    //     while let Some(loc) = locs.pop() {
    //         let dir = loc.get_dir_to(current).unwrap();
    //         dirs.push(dir);
    //         current = loc;
    //     }

    //     (dirs.len() as i32, dirs)
    // }

    pub fn dijkstra_pri(&mut self, to: char) -> (i32, Vec<char>) {
        let end = self.key_map.get_by_left(&to).unwrap();
        let start = self.current;
        let start_idx = self.graph_map.get_by_left(&start).unwrap();
        let end_idx = self.graph_map.get_by_left(end).unwrap();

        if let Some(path) =
            shortest_path_with_priority(&self, &self.weight_map, *start_idx, *end_idx)
        {
            self.current = end.clone();

            let mut dirs: Vec<char> = Vec::new();

            let mut location_path: Vec<Loc> = path
                .iter()
                .map(|&n| self.graph_map.get_by_right(&n).unwrap().clone())
                .collect();
            location_path.reverse();
            let mut current = location_path.pop().unwrap();
            while let Some(loc) = location_path.pop() {
                let dir = loc.get_dir_to(current).unwrap();
                dirs.push(dir);
                current = loc;
            }
            // println!(
            //     "Prioritert korteste vei: {:?}",
            //     dirs.iter().collect::<String>()
            // );

            return (dirs.len() as i32, dirs);
        } else {
            println!(
                "Ingen vei funnet fra {:?} til {:?}",
                self.map[&start], self.map[end]
            );
        }
        (0 as i32, vec![])
    }

    // pub fn cost_sort(&mut self, dirs: &Vec<char>) -> Vec<char> {
    //     let mut sorted = dirs.clone();
    //     sorted.sort_by(|a, b| {
    //         let a_loc = &self.get_loc(*a);
    //         let b_loc = &self.get_loc(*b);
    //         let a_cost = *self.get_cost_option(a_loc).unwrap();
    //         let b_cost = *self.get_cost_option(b_loc).unwrap();
    //         b_cost.cmp(&a_cost)
    //     }); // Sorter etter retning

    //     sorted
    // }

    pub fn visualize(&self, path: &Vec<Loc>, c: char) {
        for y in self.min.y..self.max.y + 1 {
            for x in self.min.x..self.max.x + 1 {
                let l = Loc::new(x, y);
                if path.contains(&l) {
                    print!("{}", c);
                } else {
                    if self.map.contains_key(&l) {
                        print!("{}", self.get(&l));
                    } else {
                        print!("-");
                    }
                }
            }
            println!();
        }
    }

    pub fn visualize_cost(&mut self, path: &Vec<Loc>, c: char) {
        for y in self.min.y..self.max.y + 1 {
            for x in self.min.x..self.max.x + 1 {
                let l = Loc::new(x, y);
                if path.contains(&l) {
                    print!("  {}", c);
                } else {
                    if let Some(cost) = self.get_cost_option(&l) {
                        print!(" {:2}", cost % 100);
                    } else {
                        print!("   ");
                    }
                }
            }
            println!();
        }
    }
}
pub static DIRECTION: Lazy<HashMap<char, Loc>> = Lazy::new(|| {
    let mut map = HashMap::new();
    map.insert('>', Loc { x: 1, y: 0 });
    map.insert('<', Loc { x: -1, y: 0 });
    map.insert('^', Loc { x: 0, y: -1 });
    map.insert('v', Loc { x: 0, y: 1 });
    map
});

#[derive(Debug, PartialEq, Eq)]
struct PathState {
    cost: i32,
    x_value: i32, // x-verdi for slutt-noden
    path: Vec<NodeIndex>,
}

// Tilpasset sortering for å prioritere korteste vei, sekundært basert på lexikografisk rekkefølge
impl Ord for PathState {
    fn cmp(&self, other: &Self) -> Ordering {
        other
            .cost
            .cmp(&self.cost) // Minimer kostnad
            .then_with(|| self.x_value.cmp(&other.x_value)) // Minimer x-verdi
                                                            // .then_with(|| self.x_value.cmp(&other.x_value)) // Minimer x-verdi
    }
}

impl PartialOrd for PathState {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

// Modifisert Dijkstra for å prioritere veier
fn shortest_path_with_priority(
    loc_map: &LocMap,
    weight_map: &HashMap<NodeIndex, i32>,
    start: NodeIndex,
    end: NodeIndex,
) -> Option<Vec<NodeIndex>> {
    let mut visited: HashSet<NodeIndex> = HashSet::new();
    let mut heap = BinaryHeap::new();
    let start_x = calc_weight(loc_map, start);

    heap.push(PathState {
        cost: 0,
        x_value: start_x as i32,
        path: vec![start],
    });

    while let Some(PathState {
        cost,
        x_value,
        path,
    }) = heap.pop()
    {
        let current = *path.last().unwrap();

        if current == end {
            return Some(path);
        }

        if !visited.insert(current) {
            continue;
        }

        for edge in loc_map.graph.edges(current) {
            let neighbor = edge.target();
            let weight = *edge.weight();
            let neighbor_x = calc_weight(loc_map, neighbor);
            // let neghbor = key_map[&graph[neighbor]].clone();
            // let neighbor_x = neghbor.x * 10 - neghbor.y;

            if !visited.contains(&neighbor) {
                let mut new_path = path.clone();
                new_path.push(neighbor);

                heap.push(PathState {
                    cost: cost + weight,
                    x_value: neighbor_x as i32,
                    path: new_path,
                });
            }
        }
    }

    None
}

fn calc_weight(lm: &LocMap, node_index: NodeIndex) -> i32 {
    let ch = lm.graph[node_index];
    return match ch {
        'A' => 0,
        '<' => 4,
        '^' | 'v' => 3,
        '>' => 2,
        _ => lm.weight_map[&node_index],
    };
}

// fn dijkstra_with_paths(
//     graph: &UnGraph<char, i32>,
//     start: NodeIndex,
//     end: NodeIndex,
// ) -> Option<Vec<NodeIndex>> {
//     let distances = dijkstra(graph, start, None, |e| *e.weight());

//     // Sjekk om mål-node kan nås
//     if !distances.contains_key(&end) {
//         return None; // Ingen vei til mål
//     }

//     // Bygg forgjenger-tabell
//     let mut predecessors: HashMap<NodeIndex, NodeIndex> = HashMap::new();

//     // Gå gjennom alle kanter og oppdater forgjenger
//     for edge in graph.edge_references() {
//         let (source, target) = (edge.source(), edge.target());
//         let weight = *edge.weight();

//         if let (Some(&source_dist), Some(&target_dist)) =
//             (distances.get(&source), distances.get(&target))
//         {
//             if source_dist + weight == target_dist {
//                 predecessors.insert(target, source);
//             } else if target_dist + weight == source_dist {
//                 predecessors.insert(source, target);
//             }
//         }
//     }

//     // Konstruer veien ved å gå bakover fra end
//     let mut path = Vec::new();
//     let mut current = end;

//     while current != start {
//         path.push(current);
//         current = *predecessors.get(&current)?;
//     }

//     path.push(start);
//     path.reverse(); // Gjør veien i riktig rekkefølge

//     Some(path)
// }
