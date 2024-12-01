use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day01")
        .unwrap()
        .arg("day01.txt")
        .assert()
        .success()
        .stdout("2164381\n20719933\n");
}
