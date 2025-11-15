pub fn ellipse(x: f32, y: f32, width: f32, height: f32) -> String {
    // Fill with white, draw with black, stroke width 1
    format!(
        r#"<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="white" stroke="black" stroke-width="1" />"#,
        cx = x + width / 2.0,
        cy = y + height / 2.0,
        rx = width / 2.0,
        ry = height / 2.0
    )
}
