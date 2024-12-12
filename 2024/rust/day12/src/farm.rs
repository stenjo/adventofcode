use crate::{plant::Plant, plot::Plot};

pub struct Farm {
    garden: Vec<Vec<Plant>>,
    plots: Vec<Plot>,
}

impl Farm {
    pub fn new(input: &str) -> Farm {
        let mut garden = Vec::new();
        for (y, line) in input.lines().enumerate() {
            let mut row = Vec::new();
            for (x, plant) in line.chars().enumerate() {
                row.push(Plant::new(x as i64, y as i64, plant));
            }
            garden.push(row);
        }
        let mut farm = Farm {
            garden: garden.clone(),
            plots: Vec::new(),
        };
        farm.plots = farm.get_plots();

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

    pub fn get_plots(&self) -> Vec<Plot> {
        let mut plots: Vec<Plot> = Vec::new();
        let plants = self.get_plants();
        for plant in plants {
            let mut found = false;
            if in_plots(&mut plots, &plant) {};
            if found {
                continue;
            }

            for pos in get_next_pos(plant.pos()) {
                if Some(p = self.get_plant(pos)) = &&p.get() == plant.get() {
                    plot.add_plant(plant.clone());
                }
                if self.plants().contains(&pos) {
                    continue;
                }
                for plot in &mut plots {
                    if plot.connecting_positions().contains(&p)
                        && plot.plant_type() == plant.get_plant()
                    {
                        plot.add_plant(plant.clone());
                    }
                }
            }
            for plot in &mut plots {
                if plot.connecting_positions().contains(&plant.pos())
                    && plot.plant_type() == plant.get_plant()
                {
                    plot.add_plant(plant.clone());
                    found = true;
                }
            }
            if !found {
                let new_plot = Plot::new(vec![plant.clone()]);
                plots.push(new_plot);
            }
        }
        return plots;
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
}

fn in_plots(plots: &mut Vec<Plot>, plant: &Plant, found: &mut bool) {
    for plot in plots {
        if plot.plants().contains(plant) {
            *found = true;
        }
    }
}
