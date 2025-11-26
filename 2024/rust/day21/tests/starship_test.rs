use day21::starship::Starship;
use rstest::rstest;

const TEST: &str = "029A
980A
179A
456A
379A";

#[rstest]
// #[case::first("029A", 68*29)]
// #[case::first("980A",  60*980)]
// #[case::first("179A", 68*179)]
// #[case::first("456A", 64*456)]
// #[case::first("379A", 64*379)]
#[case::first(TEST, 126384)]
fn test_complexity(#[case] input: &str, #[case] expected: i64) {
    let mut starship = Starship::new(input);

    assert_eq!(expected, starship.complexity());
}

#[test]
fn test_keypresses() {
    let mut s = Starship::new("029A");
    let mut keys = "029A".chars();
    let mut keypresses = 0;

    let mut first = Vec::new();
    while let Some(c1) = keys.next() {
        let (_, keys) = s.pad1.dijkstra_pri(c1);
        first.extend(keys);
        first.push('A');
    }
    println!("{:?}", first.iter().collect::<String>());
    println!("{:?}", "<A^A>^^AvvvA");
    assert_eq!(12, first.len());

    let mut second: Vec<char> = Vec::new();
    first.reverse();
    while let Some(c2) = first.pop() {
        let (_, keys) = s.pad2.dijkstra_pri(c2);
        second.extend(keys);
        second.push('A');
    }
    println!("{:?}", second.iter().collect::<String>());
    println!("{:?}", "v<<A>>^A<A>AvA<^AA>A<vAAA>^A");
    assert_eq!(28, second.len());

    let mut third: Vec<char> = Vec::new();
    second.reverse();
    while let Some(c3) = second.pop() {
        let (length, keys) = s.pad3.dijkstra_pri(c3);
        keypresses += length + 1;
        third.extend(keys);
        third.push('A');
    }

    println!("{:?}", third.iter().collect::<String>());
    println!(
        "{:?}",
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    );
    assert_eq!(68, keypresses);
}
// <v<AA>A>^A<Av>AA^A<v<A>^>AvA^Av<A>^A<A<vA>^>AAvA^A<v<A>A>^AAA<Av>A^A
// <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
