use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day05")
        .unwrap()
        .arg("../../data/day05.txt")
        .assert()
        .success()
        .stdout("5639\n5273\n");
}
