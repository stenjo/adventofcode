use regex::Regex;
use std::error::Error;
use std::fs;
use std::process::Command;

fn run_day_binaries() -> Result<(), Box<dyn Error>> {
    // Regex to match files like day01.txt, day25.txt, etc.
    let file_pattern = Regex::new(r"^input(\d{2})\.txt$")?;

    // Read parent directory and collect matching file names
    let mut files: Vec<String> = fs::read_dir("../data")?
        .filter_map(|entry| {
            entry.ok().and_then(|e| {
                let path = e.path();
                path.file_name()
                    .and_then(|f| f.to_str())
                    .map(|s| s.to_string())
            })
        })
        .filter(|file_name| file_pattern.is_match(file_name))
        .collect();

    // Sort files alphabetically
    files.sort();

    // Process each file in sorted order
    for file_name in files {
        // Match file name against the pattern
        if let Some(captures) = file_pattern.captures(&file_name) {
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
                        println!(
                            "Day {}, part 1: {}",
                            day_number,
                            output_str.trim().split("\n").nth(0).unwrap_or("No output")
                        );
                        println!(
                            "Day {}, part 2: {}",
                            day_number,
                            output_str.trim().split("\n").nth(1).unwrap_or("No output")
                        );
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
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        run_day_binaries();
    }
}

fn main() {
    if let Err(e) = run_day_binaries() {
        eprintln!("Error: {}", e);
    }
}
