use std::collections::{HashMap, HashSet};

use crate::{plant::Plant, plot::Plot};

pub struct Farm {
    garden: Vec<Vec<Plant>>,
    plots: Vec<Plot>,
    plant_hash: HashMap<Plant, char>,
}

impl Farm {
    pub fn new(input: &str) -> Farm {
        let mut garden = Vec::new();
        let mut plant_hash = HashMap::new();
        for (x, line) in input.lines().enumerate() {
            let mut row = Vec::new();
            for (y, plant) in line.chars().enumerate() {
                row.push(Plant::new(x as i64, y as i64, plant));
                plant_hash.insert((x, y), 1);
            }
            garden.push(row);
        }
        let mut farm = Farm {
            garden: garden.clone(),
            plots: Vec::new(),
            plant_hash: HashMap::new(),
        };
        farm.get_plots();

        farm
    }

    pub fn get_next_pos(pos: (i64, i64)) -> Vec<(i64, i64)> {
        let directions: Vec<(i64, i64)> = vec![(-1, 0), (0, 1), (1, 0), (0, -1)];
        let mut surrounding: Vec<(i64, i64)> = Vec::new();
        for dir in directions.iter() {
            let next_pos = (pos.0 + dir.0, pos.1 + dir.1);
            surrounding.push(next_pos);
        }
        surrounding
    }

    pub fn find_plants_for_plot(
        &mut self,
        starting: (i64, i64),
        plot: &mut Plot,
        visited: &mut HashSet<(i64, i64)>,
    ) -> Option<Plant> {
        let mut stack = vec![starting]; // Use a stack to replace recursion

        while let Some(current) = stack.pop() {
            // Skip if already visited
            if !visited.insert(current) {
                continue;
            }

            if let Some(plant) = self.get_plant(current) {
                if plant.get_plant() != plot.plant_type() {
                    continue; // Skip plants that don't match the plot type
                }
                if plant.pos() != starting {
                    plot.add_plant(plant.clone());
                }

                // Add neighbors to the stack
                for neighbor in Farm::get_next_pos(current) {
                    if !visited.contains(&neighbor) {
                        stack.push(neighbor);
                    }
                }
            }
        }

        // If starting plant was valid, return it; otherwise, None
        self.get_plant(starting)
            .filter(|plant| plant.get_plant() == plot.plant_type())
            .cloned()
    }

    pub fn get_plant(&self, pos: (i64, i64)) -> Option<&Plant> {
        if pos.0 < 0 || pos.1 < 0 {
            return None;
        }
        if pos.0 >= self.garden[0].len() as i64 || pos.1 >= self.garden.len() as i64 {
            return None;
        }
        return Some(&self.garden[pos.1 as usize][pos.0 as usize]);
    }

    pub fn find_plots(&mut self) -> Vec<Plot> {
        let mut plots: Vec<Plot> = Vec::new();
        let mut plants = self.get_plants(); // Assuming this returns a Vec<Plant>

        while let Some(plant) = plants.pop() {
            // Skip plants already part of existing plots
            if !self.in_plots(&plant) {
                let mut new_plot = Plot::new(vec![plant.clone()]);
                let plot_plants = self.add_plants(&mut new_plot, plant);

                // Remove all plants in the new plot from the remaining list
                for pl in plot_plants {
                    if let Some(index) = plants.iter().position(|p| p == &pl) {
                        plants.remove(index);
                    }
                }

                plots.push(new_plot);
            }
        }

        plots
    }

    fn add_plants(&mut self, mut plot: &mut Plot, plant: Plant) -> Vec<Plant> {
        let mut visited: HashSet<(i64, i64)> = HashSet::new();
        // Find all connected plants and add them to the new plot
        self.find_plants_for_plot(plant.pos(), &mut plot, &mut visited);
        return plot.get_plants();
    }

    pub fn get_plots(&mut self) -> Vec<Plot> {
        if self.plots.is_empty() {
            self.plots = self.find_plots();
        }
        return self.plots.clone();
    }

    pub fn get_plants(&self) -> Vec<Plant> {
        let mut plants: Vec<Plant> = Vec::new();
        for row in &self.garden {
            for plant in row {
                plants.push(plant.clone());
            }
        }
        return plants;
    }

    pub fn price(&self) -> u64 {
        return self
            .plots
            .iter()
            .map(|plot: &Plot| plot.perimeter() * plot.area())
            .sum::<u64>();
    }
    fn in_plots(&mut self, plant: &Plant) -> bool {
        for plot in &mut self.plots {
            if plot.contains(plant) {
                return true;
            }
        }
        return false;
    }

    fn is_in_perimeter_of_plots_mut(&mut self, plant: &Plant) -> Option<&mut Plot> {
        for plot in &mut self.plots {
            if plot.is_in_perimeter(plant) {
                return Some(plot);
            }
        }
        return None;
    }
}
