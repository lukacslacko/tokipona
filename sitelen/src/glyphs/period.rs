use crate::glyph::{Glyph, Rect, SVG};

const SIDE_MARGIN: f32 = 0.1;
const BOTTOM_MARGIN: f32 = 0.2;

pub struct PeriodGlyph {
    child: Box<dyn Glyph>,
}

impl PeriodGlyph {
    pub fn new(child: Box<dyn Glyph>) -> Self {
        PeriodGlyph { child }
    }
}

impl Glyph for PeriodGlyph {
    fn layout_within(&self, rect: &Rect) -> SVG {
        let child_width = rect.width / (1.0 + 2.0 * SIDE_MARGIN);
        let child_height = rect.height / (1.0 + BOTTOM_MARGIN);
        let child_rect = Rect {
            x: rect.x + SIDE_MARGIN * child_width,
            y: rect.y,
            width: child_width,
            height: child_height,
        };

        let period_height = rect.height - child_height;

        let mut result = Vec::new();
        result.push(String::from("<g>"));

        result.push(format!(
            "<rect x='{}' y='{}' width='{}' height='{}' rx='{}' ry='{}' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' fill='white' />",
            rect.x,
            rect.y + child_height,
            rect.width,
            period_height,
            period_height / 2.0,
            period_height / 2.0
        ));
        result.push(format!(
            "<rect x='{}' y='{}' width='{}' height='{}' rx='{}' ry='{}' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' fill='white' />",
            rect.x,
            rect.y + child_height - period_height / 2.0,
            rect.width,
            period_height,
            period_height / 2.0,
            period_height / 2.0
        ));

        result.extend(self.child.layout_within(&child_rect));
        result.push(String::from("</g>"));
        result
    }

    fn aspect_ratio(&self) -> f32 {
        let width = self.child.aspect_ratio() + 2.0 * SIDE_MARGIN;
        let height = 1.0 + BOTTOM_MARGIN;
        width / height
    }
}
