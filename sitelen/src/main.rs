use sitelen::glyph::{Direction, Glyph, Rect};
use sitelen::glyphs::simple::SimpleGlyph;
use sitelen::glyphs::stack::StackGlyph;

fn circ(color: &str) -> Box<dyn Glyph> {
    Box::new(SimpleGlyph::new(
        vec![format!(
            "<circle cx='50' cy='50' r='50' stroke='black' stroke-width='2' vector-effect='non-scaling-stroke' fill='{}' />",
            color
        )],
        1.0,
    ))
}

fn horiz(children: Vec<Box<dyn Glyph>>) -> Box<dyn Glyph> {
    Box::new(StackGlyph::new(children, Direction::Horizontal))
}

fn vert(children: Vec<Box<dyn Glyph>>) -> Box<dyn Glyph> {
    Box::new(StackGlyph::new(children, Direction::Vertical))
}

fn main() {
    let glyph = vert(vec![
        horiz(vec![circ("red"), circ("green"), circ("blue")]),
        horiz(vec![
            circ("yellow"),
            circ("purple"),
            vert(vec![circ("cyan"), circ("magenta")]),
        ]),
    ]);
    let width = 100.0;
    let height = width / glyph.aspect_ratio();
    let gap = 20.0;
    let rect = Rect {
        x: gap,
        y: gap,
        width,
        height,
    };
    let svg_content = glyph.layout_within(&rect);
    let svg_header = format!(
        "<svg xmlns='http://www.w3.org/2000/svg' width='{}' height='{}'>",
        width + 2.0 * gap,
        height + 2.0 * gap
    );
    println!(
        "{}{}{}{}",
        svg_header,
        rect.as_svg(),
        svg_content.join("\n"),
        "</svg>"
    );
}
