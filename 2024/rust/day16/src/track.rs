use crate::loc::Loc;
use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::visit::EdgeRef;
use std::cmp::Reverse;
use std::collections::HashSet;
use std::collections::{BinaryHeap, HashMap};

#[derive(Debug, Clone, Eq, PartialEq)]
struct State {
    cost: usize,
    node: NodeIndex,
    previous: Option<NodeIndex>,
}

impl Ord for State {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        other.cost.cmp(&self.cost) // Reverse to make min-heap
    }
}

impl PartialOrd for State {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        Some(self.cmp(other))
    }
}

pub struct Track {
    pub walls: HashSet<Loc>,
    pub start: Loc,
    pub start_idx: NodeIndex,
    pub finish: Loc,
    pub finish_idx: NodeIndex,
    pub size: Loc,
    pub path: HashMap<Loc, char>,
    graph: DiGraph<Loc, usize>,
}

fn dynamic_dijkstra<F>(
    graph: &DiGraph<Loc, usize>,
    source: NodeIndex,
    target: NodeIndex,
    mut direction_cost: F,
) -> Option<usize>
where
    F: FnMut(Option<NodeIndex>, NodeIndex, NodeIndex) -> usize,
{
    let mut dist: HashMap<NodeIndex, usize> = HashMap::new();
    let mut heap = BinaryHeap::new();

    // Initialize distances
    dist.insert(source, 0);
    heap.push(Reverse(State {
        cost: 0,
        node: source,
        previous: None,
    }));

    while let Some(Reverse(State {
        cost,
        node,
        previous,
    })) = heap.pop()
    {
        // If we've reached the target node, return the cost
        if node == target {
            return Some(cost);
        }

        // Skip if we've already found a better path
        if cost > *dist.get(&node).unwrap_or(&usize::MAX) {
            continue;
        }

        // Visit all neighbors
        for edge in graph.edges(node) {
            let next = edge.target();
            let base_cost = *edge.weight();

            // Add the dynamic direction change cost
            let direction_penalty = direction_cost(previous, node, next);

            let next_cost = cost + base_cost + direction_penalty;

            if next_cost < *dist.get(&next).unwrap_or(&usize::MAX) {
                dist.insert(next, next_cost);
                heap.push(Reverse(State {
                    cost: next_cost,
                    node: next,
                    previous: Some(node),
                }));
            }
        }
    }

    // No path found
    None
}

impl Track {
    pub fn new(input: &str) -> Self {
        let mut walls: HashSet<Loc> = HashSet::new();
        let mut start: Loc = Loc::new(0, 0);
        let mut finish: Loc = Loc::new(0, 0);
        let mut start_idx: NodeIndex = NodeIndex::new(0);
        let mut finish_idx: NodeIndex = NodeIndex::new(0);
        let mut size: Loc = Loc::new(0, 0);
        let mut graph: DiGraph<Loc, usize> = DiGraph::new();
        for (y, line) in input.lines().into_iter().enumerate() {
            for (x, c) in line.chars().into_iter().enumerate() {
                if c == '#' {
                    walls.insert(Loc::new(x as i64, y as i64));
                } else if c == 'S' {
                    start = Loc::new(x as i64, y as i64);
                    start_idx = graph.add_node(start.clone());
                } else if c == 'E' {
                    finish = Loc::new(x as i64, y as i64);
                    finish_idx = graph.add_node(finish.clone());
                } else {
                    graph.add_node(Loc::new(x as i64, y as i64));
                }
                size = Loc::new(x as i64, y as i64);
            }
        }
        for y in 0..size.y + 1 {
            for x in 0..size.x + 1 {
                let loc = Loc::new(x, y);
                if !walls.contains(&loc) {
                    let directions = ['>', 'v', '<', '^'];
                    let loc_idx = graph.node_indices().find(|i| graph[*i] == loc).unwrap();
                    for &d in &directions {
                        let next_pos = loc.get_next(d);
                        if !walls.contains(&next_pos) {
                            let next_idx = graph
                                .node_indices()
                                .find(|i| graph[*i] == next_pos)
                                .unwrap();
                            graph.add_edge(loc_idx, next_idx, 1);
                        }
                    }
                }
            }
        }

        Self {
            walls,
            start,
            start_idx,
            finish,
            finish_idx,
            size,
            path: HashMap::new(),
            graph,
        }
    }

    pub fn run_reindeer(&mut self) -> i64 {
        let shortest_path = dynamic_dijkstra(
            &self.graph,
            self.start_idx,
            self.finish_idx,
            |prev, current, next| {
                if let Some(p) = prev {
                    if p != current {
                        1000
                    } else {
                        0
                    }
                } else {
                    0
                }
            },
        );
        if let Some(cost) = shortest_path {
            println!(
                "The shortest path cost from {:?} to {:?} is {}",
                self.start, self.finish, cost
            );
            return cost as i64;
        } else {
            println!("No path found from {:?} to {:?}", self.start, self.finish);
        }
        0
    }

    pub fn run(&mut self) -> i64 {
        let directions = ['>', 'v', '<', '^'];
        let mut cost_path: HashMap<Loc, u64> = HashMap::new();
        let mut min_cost = u64::MAX;

        cost_path.insert(self.finish.clone(), u64::MAX);

        for &d in &directions {
            let next_pos = self.finish.get_next(d);
            let cost = self.backtrack(next_pos, d, 0, &mut cost_path);
            if cost != u64::MAX {
                min_cost = min_cost.min(cost);
            }
        }
        return cost_path.get(&self.start).unwrap().clone() as i64;
    }

    pub fn backtrack(
        &self,
        node: Loc,
        dir: char,
        acc_cost: u64,
        cost_path: &mut HashMap<Loc, u64>,
    ) -> u64 {
        if node == self.finish {
            return 0;
        }
        if self.walls.contains(&node) {
            return u64::MAX;
        }
        let new_cost = acc_cost + 1;
        if let Some(cost) = cost_path.get(&node) {
            if new_cost < *cost {
                cost_path.insert(node.clone(), new_cost);
                return new_cost;
            }
            return *cost;
        } else {
            cost_path.insert(node.clone(), new_cost);

            let directions = ['>', 'v', '<', '^'];

            for &d in &directions {
                let next_pos = node.get_next(d);
                let turn_cost = if d == dir { 0 } else { 1000 };
                let total_cost = turn_cost + new_cost;
                self.backtrack(next_pos, d, total_cost, cost_path);
            }
        }
        cost_path.get(&node).unwrap().clone()
    }

    // pub fn find_min_cost(&mut self, pos: Loc, dir: char) -> i64 {
    //     if pos == self.finish {
    //         return 0;
    //     }
    //     if self.walls.contains(&pos) || self.path.contains_key(&pos) {
    //         return i64::MAX;
    //     }

    //     self.path.insert(pos.clone(), dir);

    //     let directions = ['>', 'v', '<', '^'];
    //     let mut min_cost = i64::MAX;

    //     for &d in &directions {
    //         let next_pos = pos.get_next(d);
    //         let turn_cost = if d == dir { 0 } else { 1000 };
    //         let move_cost = 1;
    //         let total_cost = turn_cost + move_cost;

    //         let cost = self.find_min_cost(next_pos, d);
    //         if cost != i64::MAX {
    //             min_cost = min_cost.min(cost + total_cost);
    //         }
    //     }

    //     self.path.remove(&pos);
    //     min_cost
    // }

    pub fn print(&self) {
        let (xm, ym) = self.size.as_tuple();
        for y in 0..ym + 1 {
            for x in 0..xm + 1 {
                let loc = Loc::new(x, y);
                let loc_idx = self
                    .graph
                    .node_indices()
                    .find(|i| self.graph[*i] == loc)
                    .unwrap();
                if self.walls.contains(&loc) {
                    print!("#");
                    continue;
                }
                if loc == self.start {
                    print!("S");
                } else if loc == self.finish {
                    print!("E");
                } else if self.path.contains_key(&loc) {
                    let dir = self.path.get(&loc).unwrap();
                    print!("{}", dir);
                } else {
                    print!(".")
                }
            }
            println!("{}", 0);
        }
        println!();
    }
}
