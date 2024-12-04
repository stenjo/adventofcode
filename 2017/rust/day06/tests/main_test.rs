use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day06")
        .unwrap()
        .arg("input6.txt")
        .assert()
        .success()
        .stdout("4074\n21681\n");
}
