use std::fs;
use std::process::Command;
use regex::Regex;
use std::error::Error;

fn run_day_binaries() -> Result<(), Box<dyn Error>> {
    // Regex to match files like day01.txt, day25.txt, etc.
    let file_pattern = Regex::new(r"^day(\d{2})\.txt$")?;

    // Read parent directory
    for entry in fs::read_dir("..")? {
        let entry = entry?;
        let path = entry.path();

        if let Some(file_name) = path.file_name().and_then(|f| f.to_str()) {
            // Match file name against the pattern
            if let Some(captures) = file_pattern.captures(file_name) {
                // Extract day number (e.g., "01", "25")
                if let Some(day_no) = captures.get(1) {
                    let day_number = day_no.as_str();

                    // Construct the binary name (e.g., "day01")
                    let binary_name = format!("day{}", day_number);

                    // Execute the corresponding binary with the file content as input
                    let output = Command::new("cargo")
                        .args(&["run", "-p", &binary_name, "--"])
                        .arg(file_name.trim())
                        .output();

                    match output {
                        Ok(result) if result.status.success() => {
                            let output_str = String::from_utf8_lossy(&result.stdout);
                            println!("Day {}, part 1: {}", day_number, output_str.trim().split("\n").nth(0).unwrap()); 
                            println!("Day {}, part 2: {}", day_number, output_str.trim().split("\n").nth(1).unwrap()); 
                        }
                        Ok(result) => {
                            eprintln!(
                                "Failed to execute {} for {}. Error: {}",
                                binary_name,
                                file_name,
                                String::from_utf8_lossy(&result.stderr)
                            );
                        }
                        Err(e) => eprintln!("Error executing {}: {}", binary_name, e),
                    }
                }
            }
        }
    }
    Ok(())
}

fn main() {
    if let Err(e) = run_day_binaries() {
        eprintln!("Error: {}", e);
    }
}
