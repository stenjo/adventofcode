use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day02")
        .unwrap()
        .arg("../../data/day02.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
