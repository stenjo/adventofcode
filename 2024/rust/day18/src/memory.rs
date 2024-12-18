use std::cmp::min;
use std::collections::{HashMap, HashSet};

use crate::loc::Loc;
use petgraph::algo::dijkstra;
use petgraph::graph::{DiGraph, NodeIndex};
use petgraph::Graph;

pub struct Memory {
    pub corrupted: HashSet<Loc>,
    pub memory: HashMap<Loc, NodeIndex>,
    pub graph: DiGraph<Loc, u64>,
    pub bytes: Vec<Loc>,
    pub size: (i64, i64),
}

impl Memory {
    pub fn new(input: &str, size: (i64, i64)) -> Self {
        let mut bytes: Vec<Loc> = Vec::new();
        let mut graph: Graph<Loc, u64> = DiGraph::new();
        let mut memory: HashMap<Loc, NodeIndex> = HashMap::new();
        for b in input.lines() {
            let parts: Vec<i64> = b.trim().split(',').map(|x| x.parse().unwrap()).collect();
            let x = parts[0];
            let y = parts[1];
            bytes.push(Loc { x, y });
        }
        for y in 0..size.1 + 1 {
            for x in 0..size.0 + 1 {
                let loc = Loc { x, y };
                let node_idx = graph.add_node(loc.clone());
                memory.insert(loc, node_idx);
            }
        }

        for y in 0..size.1 + 1 {
            for x in 0..size.0 + 1 {
                let loc = Loc { x, y };
                let node = memory[&loc];

                let directions = ['>', 'v', '<', '^'];
                for &d in &directions {
                    let neighbor = loc.get_next(d);

                    if neighbor.in_grid(size) {
                        let neighbor_node = memory[&neighbor];
                        let cost = 1;
                        graph.add_edge(node, neighbor_node, cost);
                        graph.add_edge(neighbor_node, node, cost);
                    }
                }
            }
        }
        Self {
            corrupted: HashSet::new(),
            memory,
            graph,
            bytes,
            size,
        }
    }

    pub fn least_cost_distance(&mut self) -> HashMap<NodeIndex, u64> {
        let start = self.memory[&Loc { x: 0, y: 0 }];
        let end = self.memory[&Loc {
            x: self.size.0,
            y: self.size.1,
        }];
        let result = dijkstra(&self.graph, start, Some(end), |e| *e.weight());

        return result;
    }

    pub fn drop(&mut self, bytes: usize) {
        let mut i = 0;
        while i < min(bytes, self.bytes.len()) {
            self.drop_byte(i);
            i += 1;
        }
    }

    pub fn drop_byte(&mut self, i: usize) {
        let loc = self.bytes[i].clone();
        self.corrupted.insert(loc.clone());
        let node_idx = self.memory[&loc];
        self.graph.remove_node(node_idx);
        self.memory.clear();
        self.memory = self
            .graph
            .node_indices()
            .map(|idx| (self.graph[idx].clone(), idx))
            .collect();
    }

    pub fn print(&self, nodes: HashMap<NodeIndex, u64>) {
        for y in 0..self.size.1 + 1 {
            for x in 0..self.size.0 + 1 {
                let loc = Loc { x, y };
                if self.corrupted.contains(&loc) {
                    print!("  # ");
                } else if self.memory.contains_key(&loc) {
                    let node = self.memory[&loc];
                    if nodes.contains_key(&node) {
                        print!(" {:02} ", nodes[&self.memory[&loc]]);
                    } else {
                        print!(" {:02} ", node.index());
                    }
                } else {
                    print!("  . ");
                }
            }
            println!();
        }
        println!();
    }
}
