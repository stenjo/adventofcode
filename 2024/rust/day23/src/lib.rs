use std::collections::{BTreeSet, HashMap, HashSet, VecDeque};
type Graph = HashMap<String, HashSet<String>>;
pub mod lan;

fn add_edge(graph: &mut Graph, node1: &str, node2: &str) {
    graph
        .entry(node1.to_string())
        .or_default()
        .insert(node2.to_string());
    graph
        .entry(node2.to_string())
        .or_default()
        .insert(node1.to_string());
}

fn parse_input(input: &str) -> Graph {
    let mut graph = Graph::new();
    for line in input.lines() {
        let mut parts = line.split("-");
        let node = parts.next().unwrap();
        let neighbor = parts.next().unwrap();
        add_edge(&mut graph, node, neighbor);
    }
    return graph;
}

fn find_triangles(graph: &Graph) -> HashSet<BTreeSet<String>> {
    let mut triangles: HashSet<BTreeSet<String>> = HashSet::new();
    for (node, neighbors) in graph {
        for neighbor1 in neighbors {
            for neighbor2 in neighbors {
                if neighbor1 < neighbor2 && graph[neighbor1].contains(neighbor2) {
                    let mut triangle: BTreeSet<String> = BTreeSet::new();
                    triangle.insert(node.to_string());
                    triangle.insert(neighbor1.clone());
                    triangle.insert(neighbor2.clone());
                    triangles.insert(triangle);
                }
            }
        }
    }
    triangles
}

pub fn bfs_longest(graph: &Graph, start: &str) -> (String, i64, HashSet<String>) {
    let mut visited: HashSet<String> = HashSet::new();
    let mut queue: VecDeque<(String, i64)> = VecDeque::from(vec![(start.to_string(), 0)]);
    let mut parents: HashMap<String, String> = HashMap::new();
    visited.insert(start.to_string());
    let mut furthest = (start.to_string(), 0);
    while !queue.is_empty() {
        if let Some((node, distance)) = queue.pop_front() {
            if distance > furthest.1 {
                furthest = (node.clone(), distance as i64);
            }
            visited.insert(node.clone());
            for neighbor in &graph[&node] {
                if !visited.contains(neighbor) {
                    queue.push_back((neighbor.clone(), distance + 1));
                    parents.insert(neighbor.clone(), node.clone());
                }
            }
        }
    }
    let mut computers: HashSet<String> = HashSet::new();
    let mut current: String = furthest.0.clone();
    computers.insert(current.to_string());
    while let Some(node) = parents.get(&current) {
        computers.insert(node.clone());
        current = node.clone();
    }

    return (furthest.0, furthest.1, computers);
}

pub fn longest(graph: &Graph) -> HashSet<String> {
    let start_node = graph.keys().next().unwrap();
    let (farthest, _, _) = bfs_longest(graph, start_node);
    let (_, _, nodes) = bfs_longest(graph, farthest.as_str());
    return nodes;
}
pub fn part1(input: String) -> i64 {
    let graph = parse_input(&input);
    let triangles = find_triangles(&graph);
    let mut count = 0;
    for triangle in triangles {
        if triangle.iter().any(|v| v.starts_with("t")) {
            count += 1;
        }
    }
    return count;
}

pub fn part2(input: String) -> String {
    let graph = parse_input(&input);
    let computers = longest(&graph);
    let mut password_vec: Vec<_> = computers.iter().cloned().collect();
    password_vec.sort();
    let password = password_vec.join(",");
    return password;
}
