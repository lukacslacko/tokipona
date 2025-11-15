use crate::glyph::Direction;
use crate::glyph::Glyph;
use crate::glyph::GlyphTr;

pub struct Mi {
    glyph: Glyph,
}

impl Mi {
    pub fn new() -> Self {
        Mi { glyph: Glyph::square() }
    }
}

impl GlyphTr for Mi {
    fn svg(&self) -> String {
        String::from("")
    }

    fn wrap(&mut self, glyphs: Vec<Box<dyn GlyphTr>>, direction: Direction) {
        panic!("mi cannot wrap other glyphs");
    }
}
