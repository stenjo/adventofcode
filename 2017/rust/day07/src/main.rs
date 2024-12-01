use std::borrow::BorrowMut;
use std::cell::RefCell;
use std::fs;
use std::ops::Deref;
use std::rc::Rc;

#[derive(Debug)]
pub struct Node {
    id: String,
    children: Vec<Rc<RefCell<Node>>>,
    parents: Vec<Rc<RefCell<Node>>>,
}

impl Node {
    // Constructor for a new Node
    pub fn new(id: &str) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Node {
            id: id.to_string(),
            children: Vec::new(),
            parents: Vec::new(),
        }))
    }

    pub fn set_parent(&mut self, other: Rc<RefCell<Node>>) {
        self.parents.push(other);
    }
    // Add a connection to another node
    pub fn set_child(&mut self, other: Rc<RefCell<Node>>) {
        self.children.push(other.clone()); // Add the child to this node

        // Borrow the other node mutably to update its parents field
        other
            .borrow_mut()
            .set_parent(Rc::new(RefCell::new(self.deref())));
    }
    pub fn children(&mut self) -> usize {
        return self.children.len();
    }
    fn parents(&mut self) -> usize {
        return self.parents.len();
    }
}

pub fn part1(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

pub fn part2(input: String) -> i64 {
    return input.len().try_into().unwrap();
}

#[cfg(test)]
mod tests {
    use super::*;
    use rstest::rstest;

    #[test]
    fn node_test() {
        let node1 = Node::new("node1");
        let node2 = Node::new("node2");

        node1.borrow_mut().set_child(node2.clone());
        let child_count = node1.borrow_mut().children();
        assert_eq!(1, child_count);
        let parent_count = node2.borrow_mut().parents();
        assert_eq!(1, parent_count);
    }

    #[rstest]
    #[case::first("data", 4)]
    fn test1(#[case] input: String, #[case] result: i64) {
        assert_eq!(result, part1(input));
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
