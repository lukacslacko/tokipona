use sitelen::glyph::Direction;
use sitelen::glyph::GlyphTr;
use sitelen::glyphs::mi::Mi;
use sitelen::glyphs::period::Period;
use sitelen::glyphs::pona::Pona;

fn main() {
    let mut sentence = Period::new();
    sentence.wrap(vec![Box::new(Mi::new()), Box::new(Pona::new())], Direction::Horizontal);
    println!("<svg>{}</svg>", sentence.svg());
}
