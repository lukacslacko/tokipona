use crate::glyph::Direction;
use crate::glyph::Glyph;
use crate::glyph::GlyphTr;

pub struct Pona {
    glyph: Glyph,
}

impl Pona {
    pub fn new() -> Self {
        Pona { glyph: Glyph::square() }
    }
}

impl GlyphTr for Pona {
    fn svg(&self) -> String {
        String::from("")
    }

    fn wrap(&mut self, glyphs: Vec<Box<dyn GlyphTr>>, direction: Direction) {
        panic!("pona cannot wrap other glyphs");
    }
}
