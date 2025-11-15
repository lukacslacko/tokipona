pub struct Glyph {
    pub x: f32,
    pub y: f32,
    pub width: f32,
    pub height: f32,
    pub glyphs: Vec<Box<dyn GlyphTr>>,
}

impl Glyph {
    pub fn new(x: f32, y: f32, width: f32, height: f32) -> Self {
        Glyph {
            x,
            y,
            width,
            height,
            glyphs: Vec::new(),
        }
    }

    pub fn square() -> Self {
        Glyph::new(0.0, 0.0, 1.0, 1.0)
    }

    pub fn aspect_ratio(ratio: f32) -> Self {
        Glyph::new(0.0, 0.0, 1.0, 1.0 / ratio)
    }
}

pub enum Direction {
    Horizontal,
    Vertical,
}

pub trait GlyphTr {
    fn svg(&self) -> String {
        String::from("")
    }

    fn wrap(&mut self, glyphs: Vec<Box<dyn GlyphTr>>, direction: Direction) {}

    fn mut_glyph(&self) -> &mut Glyph;

    fn scale_width_to(&mut self, new_width: f32) {
        let mut_glyph = self.mut_glyph();
        let scale_factor = new_width / mut_glyph.width;
        mut_glyph.width *= scale_factor;
        mut_glyph.height *= scale_factor;
        
    }
}
