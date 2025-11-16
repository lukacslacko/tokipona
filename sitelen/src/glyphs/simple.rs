use crate::glyph::{Glyph, Rect, SVG};

pub struct SimpleGlyph {
    shape: SVG,
    aspect_ratio: f32,
}

impl SimpleGlyph {
    // shape is expected to be drawn for width 100.
    pub fn new(shape: SVG, aspect_ratio: f32) -> Self {
        SimpleGlyph {
            shape,
            aspect_ratio,
        }
    }
}

impl Glyph for SimpleGlyph {
    fn layout_within(&self, rect: &Rect) -> SVG {
        let mut result = Vec::new();
        result.push(format!(
            "<g transform='translate({}, {}) scale({})'>",
            rect.x,
            rect.y,
            rect.width / 100.0
        ));
        result.extend(self.shape.iter().cloned());
        result.push(String::from("</g>"));
        result
    }

    fn aspect_ratio(&self) -> f32 {
        self.aspect_ratio
    }
}
