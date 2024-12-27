use std::vec;

use day21::{
    keypad::{Keypad, Starship},
    loc::Loc,
};
use rstest::rstest;

#[rstest]
#[case::first(vec!["A"], "A", (0,0))]
#[case::first(vec!["   "," A "], 'A', (1,1))]
fn test_parse(#[case] input: Vec<&str>, #[case] expected: char, #[case] loc: (i64, i64)) {
    let keypad = Keypad::new(input);
    assert_eq!(expected, keypad.get_key(&Loc::new(loc.0, loc.1)));
    assert_eq!(loc, keypad.get_loc(expected).unwrap().as_tuple());
}

#[test]
fn test_keypad_new() {
    let input = vec!["789", "456", "123", " 0A"];
    let keypad = Keypad::new(input);
    assert_eq!(keypad.keys.len(), 11);
    assert_eq!(keypad.get_key(&Loc::new(0, 0)), '7');
    assert_eq!(keypad.get_key(&Loc::new(1, 1)), '5');
    assert_eq!(keypad.get_key(&Loc::new(2, 3)), 'A');
}

#[test]
fn test_keypad_get_loc() {
    let input = vec!["789", "456", "123", " 0A"];
    let keypad = Keypad::new(input);
    assert_eq!(keypad.get_loc('7'), Some(Loc::new(0, 0)));
    assert_eq!(keypad.get_loc('5'), Some(Loc::new(1, 1)));
    assert_eq!(keypad.get_loc('A'), Some(Loc::new(2, 3)));
    assert_eq!(keypad.get_loc('X'), None);
}

#[test]
fn test_starship_new() {
    let input = "123\n456\n789";
    let starship = Starship::new(input);
    assert_eq!(starship.codes.len(), 3);
    assert_eq!(starship.keypads.len(), 1);
    assert_eq!(starship.keypads[0].keys.len(), 11);
}

// #[rstest]
// #[case::first("0753A", 9)]
// #[case::first("0003A", 18)]
// fn test_starship_complexity(#[case] input: &str, #[case] expected: i64) {
//     let starship = Starship::new(input);
//     assert_eq!(expected, starship.complexity(input));
// }

// #[rstest]
// #[case('A','0', vec!['<'])]
// fn test_keypad_get_moves(
//     #[case] from_char: char,
//     #[case] to_char: char,
//     #[case] expected: Vec<char>,
// ) {
//     let input = vec!["789", "456", "123", " 0A"];
//     let keypad = Keypad::new(input);
//     let from = keypad.get_loc(from_char).unwrap();
//     let to = keypad.get_loc(to_char).unwrap();
//     let moves = keypad.get_moves(&from, &to);
//     assert_eq!(expected, moves);
// }
