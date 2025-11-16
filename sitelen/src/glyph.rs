pub struct Rect {
    // Top-left corner
    pub x: f32,
    pub y: f32,
    pub width: f32,
    pub height: f32,
}

impl Rect {
    pub fn as_svg(&self) -> String {
        format!(
            "<rect x='{}' y='{}' width='{}' height='{}' fill='none' stroke='grey' stroke-dasharray='4' stroke-width='1' />",
            self.x, self.y, self.width, self.height
        )
    }
}

pub enum Direction {
    Horizontal,
    Vertical,
}

pub type SVG = Vec<String>;

pub trait Glyph {
    fn layout_within(&self, rect: &Rect) -> SVG;

    fn aspect_ratio(&self) -> f32;
}
