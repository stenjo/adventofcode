use std::collections::HashSet;

use petgraph::algo::{bellman_ford, dijkstra};
use petgraph::graph::{Graph, NodeIndex};

pub struct Lan {
    graph: Graph<String, f32>,
}

impl Lan {
    fn new(input: &str) -> Lan {
        let mut graph: Graph<String, f32> = Graph::new();
        for line in input.lines() {
            let mut parts = line.split("-");
            let node = parts.next().unwrap();
            let neighbor = parts.next().unwrap();
            let node_index = graph.add_node(node.to_string());
            let neighbor_index = graph.add_node(neighbor.to_string());
            graph.add_edge(node_index, neighbor_index, 1.0);
        }
        Lan { graph }
    }

    pub fn find_chains_of_three(&self) -> HashSet<Vec<String>> {
        let mut chains: HashSet<Vec<String>> = HashSet::new();
        for start_node in self.graph.node_indices() {
            let distances = dijkstra(&self.graph, start_node, None, |_| 1);
            for (mid_node, &dist) in &distances {
                if dist == 1.0 {
                    let mid_distances = dijkstra(&self.graph, *mid_node, None, |_| 1);
                    for (end_node, &mid_dist) in &mid_distances {
                        if mid_dist == 1.0 && end_node != &start_node {
                            let mut chain = vec![
                                self.graph[start_node].clone(),
                                self.graph[*mid_node].clone(),
                                self.graph[*end_node].clone(),
                            ];
                            chain.sort();
                            chains.insert(chain);
                        }
                    }
                }
            }
        }
        chains
    }

    pub fn path(&self, a: String) -> HashSet<String> {
        let a_idx = self
            .graph
            .node_indices()
            .find(|i| self.graph[*i] == a)
            .unwrap();
        let distances = dijkstra(&self.graph, a_idx, None, |_| 1);
        let farthest = distances.iter().max_by_key(|(_, &dist)| dist).unwrap();
        let (farthest_node, longest_distance) = farthest;

        let (distances, predecessors) = bellman_ford(&self.graph, a_idx).unwrap();

        let mut computers: HashSet<String> = HashSet::new();
        // Predecessors for path reconstruction
        println!("\nPredecessors for path reconstruction:");
        for (index, pred) in predecessors.iter().enumerate() {
            println!(
                "Node {:?}: {:?}",
                self.graph.node_weight(NodeIndex::new(index)).unwrap(),
                pred.map(|i| self.graph.node_weight(i).unwrap())
            );
            if let Some(pred) = pred {
                computers.insert(self.graph.node_weight(pred).unwrap().clone());
            }
        }
                // Predecessors for path reconstruction
                println!("\nPredecessors for path reconstruction:");
                for (index, pred) in predecessors.iter().enumerate() {
                    println!(
                        "Node {:?}: {:?}",
                        self.graph.node_weight(NodeIndex::new(index)).unwrap(),
                        pred.map(|i| self.graph.node_weight(i).unwrap())
                    );
                    if let Some(pred) = pred {
                        computers.insert(self.graph.node_weight(pred).unwrap().clone());
                    }
                    computers.insert(pred.map(|i| self.graph.node_weight(i).unwrap()));
                }
            }
            Err(err) => {
                println!("Graph contains a negative weight cycle: {:?}", err);
            }
        }
        return computers;
    }
}
