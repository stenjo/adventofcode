use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day04")
        .unwrap()
        .arg("../../data/day04.txt")
        .assert()
        .success()
        .stdout("2397\n1824\n");
}
