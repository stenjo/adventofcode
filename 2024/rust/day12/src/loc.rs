#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Loc {
    x: i64,
    y: i64,
}
impl Loc {
    pub(crate) fn new(x: i64, y: i64) -> Self {
        Self { x, y }
    }

    pub(crate) fn as_tuple(&self) -> (i64, i64) {
        (self.y, self.x)
    }
}
