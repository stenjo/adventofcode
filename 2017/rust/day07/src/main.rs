use petgraph::{graph::NodeIndex, Graph};
use std::{borrow::Borrow, collections::HashMap, fs};

#[derive(Debug)]
struct NodeData {
    name: String,
    weight: i32,
}

fn parse_node(input: &str) -> (String, i32, Vec<String>) {
    // Split the input into parts by " -> "
    let parts: Vec<&str> = input.split(" -> ").collect();

    // Extract name and weight from the first part
    let main_part = parts[0]; // "fwft (72)"
    let mut main_iter = main_part.split_whitespace();
    let name = main_iter.next().unwrap().to_string(); // First word is the name
    let weight = main_iter.next().unwrap(); // Second part is the weight in parentheses
    let weight = weight
        .trim_matches(|c| c == '(' || c == ')')
        .parse::<i32>()
        .unwrap();

    // Extract children from the second part, if it exists
    let children = if parts.len() > 1 {
        parts[1].split(", ").map(|s| s.to_string()).collect()
    } else {
        Vec::new() // No children if " -> " is not present
    };

    (name, weight, children)
}

pub fn part1(input: String) -> String {
    let mut graph = Graph::<NodeData, ()>::new();
    let mut index: HashMap<String, NodeIndex> = HashMap::new();

    build_tree(input, index, &mut graph);
    let roots: Vec<_> = graph.externals(petgraph::Direction::Incoming).collect();
    let mut r = roots.iter().map(|&i| graph[i].borrow()).collect::<Vec<_>>();

    return r.pop().expect("msg").name.to_string();
}

fn build_tree(
    input: String,
    mut index: HashMap<String, NodeIndex>,
    graph: &mut Graph<NodeData, ()>,
) {
    for line in input.lines() {
        let (name, weight, children) = parse_node(line);
        let root_idx: NodeIndex = if let Some(&root_idx) = index.get(&name) {
            graph[root_idx].weight = weight;
            root_idx
        } else {
            let root_idx = graph.add_node(NodeData {
                name: name.to_string(),
                weight: weight,
            });
            index.insert(name, root_idx);
            root_idx
        };
        if !children.is_empty() {
            for child in children {
                // Retrieve or create child node
                let child_idx = if let Some(&child_idx) = index.get(&child) {
                    child_idx
                } else {
                    // Add new node to the graph if it doesn't exist
                    let new_child_idx = graph.add_node(NodeData {
                        name: child.to_string(),
                        weight: 0,
                    });
                    index.insert(child.clone(), new_child_idx); // Insert the new node into the index
                    new_child_idx
                };

                // Add edge from root to child
                graph.add_edge(root_idx, child_idx, ());
            }
        }
    }
}

pub fn part2(input: String) -> i64 {
    let mut graph = Graph::<NodeData, ()>::new();
    let mut index: HashMap<String, NodeIndex> = HashMap::new();

    build_tree(input, index, &mut graph);
    let roots: Vec<_> = graph.externals(petgraph::Direction::Incoming).collect();
    let mut r = roots.iter().map(|&i| graph[i].borrow()).collect::<Vec<_>>();

    return r.pop().expect("msg").weight as i64;
}

fn sum_of_weights(&self) -> i32 {
    let mut sum = self.weight;
    for child in self.children.iter() {
        sum += child.sum_of_weights();
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;
    use petgraph::Graph;
    use rstest::rstest;

    #[test]
    fn node_test() {
        let mut graph = Graph::<&str, ()>::new();

        // Add nodes
        let root = graph.add_node("root");
        let child1 = graph.add_node("child1");
        let child2 = graph.add_node("child2");

        // Add edges (directed)
        graph.add_edge(root, child1, ());
        graph.add_edge(root, child2, ());

        // Identify root (a node with no incoming edges)
        let roots: Vec<_> = graph.externals(petgraph::Direction::Incoming).collect();
        let r = roots
            .iter()
            .map(|&i| graph[i])
            .collect::<Vec<_>>()
            .join(":");

        assert_eq!("root", r);
    }

    #[test]
    fn parse_node_test() {
        let input = "fwft (72) -> ktlj, cntj, xhth";
        let (name, weight, _children) = parse_node(input);

        assert_eq!("fwft", name);
        assert_eq!(72, weight);
    }

    #[rstest]
    #[case::first(
        "pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)",
        "tknk"
    )]
    fn test1(#[case] input: String, #[case] result: String) {
        assert_eq!(result, part1(input));
    }

    #[rstest]
    #[case::second(
        "pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)",
        100
    )]
    fn test2(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part2(input));
    }
}

pub fn main() {
    let path = "../data/".to_string() + &std::env::args().nth(1).expect("Expected input argument");
    let input = match fs::read_to_string(&path) {
        Ok(input) => input,
        Err(e) => panic!("Error reading file: {}", e),
    };
    println!("{}", part1(input.clone()));
    println!("{}", part2(input));
}
