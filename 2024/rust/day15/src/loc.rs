#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Loc {
    pub x: i64,
    pub y: i64,
}
impl Loc {
    pub fn new(x: i64, y: i64) -> Self {
        Self { x, y }
    }

    pub fn update(&mut self, p: (i64, i64)) -> Loc {
        self.x = p.0;
        self.y = p.1;
        return self.clone();
    }

    pub fn up(&mut self) -> Loc {
        self.y -= 1;
        return self.clone();
    }

    pub fn down(&mut self) -> Loc {
        self.y += 1;
        return self.clone();
    }

    pub fn left(&mut self) -> Loc {
        self.x -= 1;
        return self.clone();
    }

    pub fn right(&mut self) -> Loc {
        self.x += 1;
        return self.clone();
    }

    pub fn as_tuple(&self) -> (i64, i64) {
        (self.x, self.y)
    }

    pub(crate) fn add(&mut self, v: &Loc) -> Loc {
        self.x += v.x;
        self.y += v.y;
        self.clone()
    }

    pub fn add_teleport(&mut self, v: &Loc, min: &Loc, max: &Loc) -> Loc {
        let width: i64 = max.x - min.x + 1;
        let height: i64 = max.y - min.y + 1;
        self.add(v);
        self.x = (self.x - min.x) % width + min.x;
        if self.x < min.x {
            self.x += width;
        }
        self.y = (self.y - min.y) % height + min.y;
        if self.y < min.y {
            self.y += height;
        }
        self.clone()
    }

    pub(crate) fn gps(&self) -> i64 {
        self.x + self.y * 100
    }
}
