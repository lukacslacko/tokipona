use crate::glyph::Direction;
use crate::glyph::Glyph;
use crate::glyph::GlyphTr;
use crate::svg::ellipse;

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
        let x = self.glyph.x;
        let y = self.glyph.y;
        let width = self.glyph.width;
        let height = self.glyph.height;
        format!(
            "{}{}",
            ellipse(x, y, width, height * 0.6),
            ellipse(x, y + height * 0.4, width, height * 0.6)
        )
    }

    fn wrap(&mut self, glyphs: Vec<Box<dyn GlyphTr>>, direction: Direction) {}
}
