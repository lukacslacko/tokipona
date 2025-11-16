use crate::glyph::{Glyph, Rect, SVG};

const MARGIN: f32 = 0.1;

pub struct LiGlyph {
    child: Box<dyn Glyph>,
}

impl LiGlyph {
    pub fn new(child: Box<dyn Glyph>) -> Self {
        LiGlyph { child }
    }
}

impl Glyph for LiGlyph {
    fn layout_within(&self, rect: &Rect) -> SVG {
        let mut result = Vec::new();
        result.push(String::from("<g>"));

        // Draw a rounded rectangle as the border matching the `rect`.
        let radius = rect.width.min(rect.height) * MARGIN;
        result.push(format!(
            "<rect x='{}' y='{}' width='{}' height='{}' rx='{}' ry='{}' fill='lightgrey' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' />",
            rect.x,
            rect.y,
            rect.width,
            rect.height,
            radius,
            radius
        ));

        let child_width = rect.width / (1.0 + 2.0 * MARGIN);
        let margin = (rect.width - child_width) / 2.0;
        let child_height = rect.height - 2.0 * margin;

        let inner_rect = Rect {
            x: rect.x + margin,
            y: rect.y + margin,
            width: child_width,
            height: child_height,
        };

        // Layout the child glyph within the same rectangle
        result.extend(self.child.layout_within(&inner_rect));

        result.push(String::from("</g>"));
        result
    }

    fn aspect_ratio(&self) -> f32 {
        let margin = MARGIN;
        let width = self.child.aspect_ratio() + 2.0 * margin;
        let height = 1.0 + 2.0 * margin;
        width / height
    }
}
