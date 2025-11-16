use crate::glyph::{Glyph, Rect, SVG};

const MARGIN: f32 = 0.1;
const CROWN: f32 = 0.1;

pub struct EGlyph {
    child: Box<dyn Glyph>,
}

impl EGlyph {
    pub fn new(child: Box<dyn Glyph>) -> Self {
        EGlyph { child }
    }
}

impl Glyph for EGlyph {
    fn layout_within(&self, rect: &Rect) -> SVG {

        let child_width = rect.width / (1.0 + 2.0 * MARGIN + CROWN);
        let child_height = rect.height / (1.0 + 2.0 * MARGIN);
        let child_rect = Rect {
            x: rect.x + MARGIN * child_width,
            y: rect.y + MARGIN * child_height,
            width: child_width,
            height: child_height,
        };

        let mut result = Vec::new();
        result.push(String::from("<g>"));

        // Draw the box and the crown.
        result.push(format!["<g transform='translate({}, {}) scale({}, {})'>", rect.x, rect.y, rect.width / 100.0, rect.height / 100.0]);
        result.push(String::from("<path d='' fill='white' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />"));
        result.push(String::from("<path d='' fill='white' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />"));
        result.push(String::from("<path d='' fill='white' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />"));
        result.push(String::from("<path d='' fill='white' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />"));
        result.push(String::from("<path d='' fill='white' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />"));
        result.push(String::from("</g>"));

        result.extend(self.child.layout_within(&child_rect));

        result.push(String::from("</g>"));
        result
    }

    fn aspect_ratio(&self) -> f32 {
        let width = self.child.aspect_ratio() + 2.0 * MARGIN + CROWN;
        let height = 1.0 + 2.0 * MARGIN;
        width / height
    }
}