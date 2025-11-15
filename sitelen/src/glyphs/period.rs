use crate::glyph::Direction;
use crate::glyph::Glyph;
use crate::glyph::GlyphTr;

pub struct Period {
    glyph: Glyph,
}

impl Period {
    pub fn new() -> Self {
        Period {
            glyph: Glyph::aspect_ratio(5.0),
        }
    }
}

impl GlyphTr for Period {
    fn svg(&self) -> String {
        String::from("")
    }

    fn wrap(&mut self, glyphs: Vec<Box<dyn GlyphTr>>, direction: Direction) {}
}
