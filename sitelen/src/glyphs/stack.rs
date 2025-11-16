use crate::glyph::{Direction, Glyph, Rect, SVG};

pub struct StackGlyph {
    children: Vec<Box<dyn Glyph>>,
    direction: Direction,
}

impl StackGlyph {
    pub fn new(children: Vec<Box<dyn Glyph>>, direction: Direction) -> Self {
        StackGlyph {
            children,
            direction,
        }
    }
}

impl Glyph for StackGlyph {
    fn layout_within(&self, rect: &Rect) -> SVG {
        let mut result = Vec::new();
        result.push(String::from("<g>"));

        match self.direction {
            Direction::Horizontal => {
                let total_aspect: f32 =
                    self.children.iter().map(|child| child.aspect_ratio()).sum();
                let mut current_x = rect.x;
                for child in &self.children {
                    let child_width = rect.width * (child.aspect_ratio() / total_aspect);
                    let child_rect = Rect {
                        x: current_x,
                        y: rect.y,
                        width: child_width,
                        height: rect.height,
                    };
                    // Instead of extend, prepend, for nicer overlap.
                    result.splice(0..0, child.layout_within(&child_rect));
                    current_x += child_width;
                }
            }
            Direction::Vertical => {
                let total_inverse_aspect: f32 = self
                    .children
                    .iter()
                    .map(|child| 1.0 / child.aspect_ratio())
                    .sum();
                let mut current_y = rect.y;
                for child in &self.children {
                    let child_height =
                        rect.height * ((1.0 / child.aspect_ratio()) / total_inverse_aspect);
                    let child_rect = Rect {
                        x: rect.x,
                        y: current_y,
                        width: rect.width,
                        height: child_height,
                    };
                    // Instead of extend, prepend, for nicer overlap.
                    result.splice(0..0, child.layout_within(&child_rect));
                    current_y += child_height;
                }
            }
        }

        result.push(String::from("</g>"));
        result
    }

    fn aspect_ratio(&self) -> f32 {
        match self.direction {
            Direction::Horizontal => self.children.iter().map(|child| child.aspect_ratio()).sum(),
            Direction::Vertical => {
                (1.0 / self
                    .children
                    .iter()
                    .map(|child| 1.0 / child.aspect_ratio())
                    .sum::<f32>()) as f32
            }
        }
    }
}
