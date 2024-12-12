use crate::loc::Loc;

#[derive(Debug, Clone, Eq, Hash, PartialEq, PartialOrd, Ord)]
pub struct Plant {
    loc: Loc,
    plant: char,
}

impl Plant {
    pub fn new(x: i64, y: i64, plant: char) -> Plant {
        Plant {
            loc: Loc::new(x, y),
            plant,
        }
    }

    pub fn get_loc(&self) -> &Loc {
        &self.loc
    }

    pub fn get_plant(&self) -> char {
        self.plant
    }

    pub(crate) fn pos(&self) -> (i64, i64) {
        self.loc.as_tuple().clone()
    }
}
