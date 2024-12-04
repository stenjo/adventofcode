use assert_cmd::Command;

#[test]
fn test_part1_success() {
    Command::cargo_bin("{{ crate_name }}")
        .unwrap()
        .arg("../../data/{{ crate_name }}.txt")
        .assert()
        .success()
        .stdout("321\n386\n");
}
