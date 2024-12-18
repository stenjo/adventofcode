use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day18")
        .unwrap()
        .arg("../../data/day18.txt")
        .assert()
        .success()
        .stdout("322\n60,21\n");
}
