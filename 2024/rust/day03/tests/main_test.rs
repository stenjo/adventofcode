use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("day03")
        .unwrap()
        .arg("../../data/day03.txt")
        .assert()
        .success()
        .stdout("169021493\n111762583\n");
}
