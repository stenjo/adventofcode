use itertools::Itertools;
use petgraph::{algo::toposort, graph::NodeIndex, Graph};
use std::{
    borrow::Borrow,
    collections::{HashMap, HashSet},
    fs,
};

#[derive(Debug)]
struct NodeData {
    name: String,
    weight: i32,
    total: i32,
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

    build_tree(input, &mut index, &mut graph);
    let roots: Vec<_> = graph.externals(petgraph::Direction::Incoming).collect();
    let mut r = roots.iter().map(|&i| graph[i].borrow()).collect::<Vec<_>>();

    return r.pop().expect("msg").name.to_string();
}

fn build_tree(
    input: String,
    index: &mut HashMap<String, NodeIndex>,
    graph: &mut Graph<NodeData, ()>,
) {
    for line in input.lines() {
        let (name, weight, children) = parse_node(line);
        let root_idx: NodeIndex = if let Some(&root_idx) = index.get(&name) {
            graph[root_idx].weight = weight;
            graph[root_idx].total = weight;
            root_idx
        } else {
            let root_idx = graph.add_node(NodeData {
                name: name.to_string(),
                weight: weight,
                total: weight,
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
                        total: 0,
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

    // Build the tree
    build_tree(input, &mut index, &mut graph);

    // Find root nodes (nodes with no incoming edges)
    let roots: Vec<_> = graph.externals(petgraph::Direction::Incoming).collect();
    let sorted = toposort(&graph, None).unwrap();

    // Now, find the unbalanced node, starting at the leaves...
    for &node in sorted.iter().rev() {
        // If this node's children aren't all equal
        if !graph.neighbors(node).map(|n| graph[n].total).all_equal() {
            // Find the min and max value of the children
            let (min, max) = graph
                .neighbors(node)
                .map(|n| graph[n].total)
                .minmax()
                .into_option()
                .unwrap();

            // Split the children based on their total (left for min, right for max)
            let (left, right): (Vec<_>, Vec<_>) =
                graph.neighbors(node).partition(|&n| graph[n].total == min);

            // The unbalanced node is the side that has one element
            let unbalanced = if left.len() == 1 {
                &graph[left[0]]
            } else {
                &graph[right[0]]
            };

            return (unbalanced.weight + min - max).into();
            // Find that node's new weight in order to balance the weights
            // println!(
            //     "[Part 2]: New weight (for \"{}\") is: {}",
            //     unbalanced.name,
            //     unbalanced.weight + min - max
            // );

            // break;
        }

        // Otherwise, update this node's total weight
        graph[node].total += graph.neighbors(node).map(|n| graph[n].total).sum::<i32>();
    }
    return 0;
}

impl NodeData {
    // Recursive function to calculate the sum of weights for the node and its children
    fn sum_of_weights(&self, graph: &Graph<NodeData, ()>, node_idx: NodeIndex) -> i32 {
        let mut sum = self.weight;

        // Traverse all children (outgoing edges)
        for child_idx in graph.neighbors(node_idx) {
            let child = &graph[child_idx];
            sum += child.sum_of_weights(graph, child_idx);
        }

        sum
    }

    fn is_balanced(&self, graph: &Graph<NodeData, ()>, node_idx: NodeIndex) -> bool {
        let mut children: Vec<i32> = Vec::<i32>::new();
        for child_idx in graph.neighbors(node_idx) {
            let child = &graph[child_idx];
            children.push(child.sum_of_weights(graph, child_idx));
        }
        return children.windows(2).all(|w| w[0] == w[1]);
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use petgraph::{graph, Graph};
    use rstest::rstest;

    #[rstest]
    #[case(
        "xhth (57)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    cntj (57)",
        "fwft",
        ""
    )]
    #[case(
        "xhth (57)
    ktlj (58)
    fwft (72) -> ktlj, cntj, xhth
    cntj (57)",
        "fwft",
        "ktlj"
    )]
    fn test_get_odd_node(#[case] input: String, #[case] node: String, #[case] result: String) {
        let mut index = HashMap::<String, NodeIndex>::new();
        let mut graph = Graph::<NodeData, ()>::new();
        build_tree(input, &mut index, &mut graph);
        let node_idx = index.get(&node).unwrap();
        let node = &graph[*node_idx];
    }

    #[rstest]
    #[case(
        "xhth (57)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    cntj (57)",
        "fwft",
        true
    )]
    #[case(
        "xhth (57)
    ktlj (58)
    fwft (72) -> ktlj, cntj, xhth
    cntj (57)",
        "fwft",
        false
    )]
    fn test_is_balanced(#[case] input: String, #[case] node: String, #[case] result: bool) {
        let mut index = HashMap::<String, NodeIndex>::new();
        let mut graph = Graph::<NodeData, ()>::new();
        build_tree(input, &mut index, &mut graph);
        let node_idx = index.get(&node).unwrap();
        let node = &graph[*node_idx];
        assert_eq!(result, node.is_balanced(&graph, *node_idx));
    }

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
        60
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
