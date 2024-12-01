use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day07")
        .unwrap()
        .arg("input07.txt")
        .assert()
        .success()
        .stdout("21681\n21681\n");
}
