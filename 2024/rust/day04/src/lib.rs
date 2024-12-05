pub fn search_lines(xword: &Vec<Vec<char>>) -> i64 {
    let mut count = 0;
    for i in 0..xword.len() {
        let line: String = xword[i].iter().collect();
        if line.contains("XMAS") {
            count += 1;
        }
        if line.contains("SAMX") {
            count += 1;
        }
    }
    return count;
}
