pub use std::{
    collections::{HashMap, HashSet},
    fmt,
    sync::OnceLock,
};

pub type ParseIntResult<T> = Result<T, std::num::ParseIntError>;
pub type ParseFloatResult<T> = Result<T, std::num::ParseFloatError>;

pub use anyhow::{anyhow, Error};
pub use colored::Colorize;
pub use itertools::{self, Itertools};
pub use rayon::prelude::*;
pub use regex::{self, Regex};
pub use rustc_hash::{FxHashMap, FxHashSet, FxHasher};

pub type Anyhow<T> = anyhow::Result<T>;

pub trait Solver
where
    Self: std::marker::Sized,
{
    fn new(input: &str) -> Anyhow<Self>;
    fn part1(&mut self) -> Anyhow<impl fmt::Display>;
    fn part2(&mut self) -> Anyhow<impl fmt::Display>;
}
