pub struct Design {
    pub inventory: Trie,
    pub designs: Vec<String>,
}

impl Design {
    pub fn new(input: &str) -> Self {
        let mut inventory: Trie = Trie::new();
        let mut designs = Vec::new();
        let mut parts = input.split("\n\n");
        let inventory_list = parts.next().unwrap();
        let design_list = parts.next().unwrap();

        for towel in inventory_list.trim().split(", ") {
            inventory.insert(towel);
        }

        for design in design_list.trim().lines() {
            designs.push(design.to_string());
        }

        Self { inventory, designs }
    }

    pub(crate) fn valid_designs(&self) -> i64 {
        let mut valid_designs = 0;

        for design in self.designs.iter() {
            if self.inventory.can_form_string(design) {
                valid_designs += 1;
            }
        }
        return valid_designs;
    }

    pub fn max_combinations(&self) -> u128 {
        let mut max_combinations: u128 = 0;
        for design in self.designs.iter() {
            max_combinations += self.inventory.count_ways(&design);
        }
        max_combinations
    }
}

use std::collections::HashMap;

#[derive(Debug, Default)]
struct TrieNode {
    children: HashMap<char, TrieNode>,
    is_end_of_word: bool,
}

#[derive(Debug, Default)]
pub struct Trie {
    root: TrieNode,
}

impl Trie {
    /// Creates a new Trie.
    pub fn new() -> Self {
        Trie {
            root: TrieNode::default(),
        }
    }

    /// Inserts a word into the Trie.
    pub fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for ch in word.chars() {
            node = node.children.entry(ch).or_insert_with(TrieNode::default);
        }
        node.is_end_of_word = true;
    }

    /// Checks if a word exists in the Trie.
    pub fn contains(&self, word: &str) -> bool {
        let mut node = &self.root;
        for ch in word.chars() {
            if let Some(next_node) = node.children.get(&ch) {
                node = next_node;
            } else {
                return false;
            }
        }
        node.is_end_of_word
    }

    /// Finds the total number of ways a string can be built from the available words in the Trie.
    pub fn count_ways(&self, string: &str) -> u128 {
        let n = string.len();
        let mut dp = vec![0; n + 1];
        dp[0] = 1;

        for i in 1..=n {
            for j in 0..i {
                if dp[j] > 0 && self.contains(&string[j..i]) {
                    dp[i] += dp[j];
                }
            }
        }

        dp[n]
    }
    /// Checks if a string can be decomposed into known words.
    pub fn can_form_string(&self, string: &str) -> bool {
        let n = string.len();
        let mut dp = vec![false; n + 1];
        dp[0] = true;

        for i in 1..=n {
            for j in 0..i {
                if dp[j] && self.contains(&string[j..i]) {
                    dp[i] = true;
                    break;
                }
            }
        }

        dp[n]
    }
}
