from dataclasses import dataclass

show_grid = True
show_syls = True

INNER = 0
OUTER = 1
  
pens = {
  INNER: "inner_pen",
  OUTER: "outer_pen",
}

@dataclass
class Path:
  path: str
  pen: int
    
@dataclass
class Transform:
  scale: float
  dx: float
  dy: float

mp = []

mp.append(f"""

pen outer_pen, inner_pen, grid_pen;
outer_pen := pencircle scaled 1.5bp yscaled 0.2 rotated 30;
inner_pen := pencircle scaled 0.7bp yscaled 0.2 rotated 30;
grid_pen := pencircle scaled 0.2bp;

def clear(expr p) = 
  fill buildcycle(p) withcolor white; 
enddef;

picture grid;
grid := image(
"""
if show_grid:
  mp.append("""
    for a = -10 step 5 until 10:
      draw (a, -10) -- (a, 10) withpen grid_pen withcolor .5white;
      draw (-10, a) -- (10, a) withpen grid_pen withcolor .5white;
    endfor;
  """)
mp.append("""
);
path nasal_contour;
nasal_contour :=
  (0, -2) .. (-10, -7) {down} .. (-6, -10) {right} .. {up} (-3, -6) {down} ..
  {right} (0, -10) {right} .. {up} (3, -6) {down} .. {right} (6, -10) ..
  {up} (10, -7) .. cycle;
""")

vowels = {
  "a": [
    Path("(-10, 6) {right} .. (3, 0)", INNER),
    Path("(-3, 0) {dir 45} .. (3, 0)", INNER),
    Path("(-3, 0) {dir -45} .. (3, 0)", INNER),
    Path("fullcircle scaled 0.5", INNER),
  ],
  "e": [
    Path("(-4, 0) -- (4, 0)", INNER),
    Path("(0, -4) -- (0, 4)", INNER),
  ],
}

mp.append("""
path consonant_j_contour, consonant_j_tick;
consonant_j_contour := (5, 4) {curl 0.2} .. (-4, 9) .. (-10, 0) .. (0, -10) .. (10, 0) .. (4, 10) .. (-2, 1);
consonant_j_contour := consonant_j_contour cutafter consonant_j_contour;
consonant_j_tick := (5,7) {dir 220} .. (2,6);

path consonant_k_contour, consonant_k_a, consonant_k_b;
consonant_k_contour :=
  (-2, 10) .. (-10, 4) {down} .. tension 1.2 .. {right} (-6, -10) .. {up} (-2, -3) {right} 
  .. (10, 0) {up} .. tension 0.8 .. cycle;
consonant_k_a := (-5, -5) .. (0, -10) .. {curl 0} (5, 0);
consonant_k_b := consonant_k_a shifted (4, 0);
consonant_k_a := (consonant_k_a shifted (-1, 0) cutafter consonant_k_contour) cutbefore consonant_k_contour;
consonant_k_b := (consonant_k_b cutafter consonant_k_contour) cutbefore consonant_k_a;
""")

consonants = {
  "": [
    Path("(0, -10) .. (-10, 0) .. (0, 10) .. (10, 0) .. cycle", OUTER),
  ],
  "J": [
    Path("consonant_j_contour", OUTER),
    Path("consonant_j_tick cutafter consonant_j_contour", INNER),
    Path("consonant_j_tick shifted(-1, 1) cutafter consonant_j_contour", INNER),
  ],
  "K": [
    Path("consonant_k_contour", OUTER),
    Path("consonant_k_a", INNER),
    Path("consonant_k_b", INNER),
  ],
}

vowel_transform = {
  "": Transform(1, 0, 0),
  "J": Transform(0.8, -1, 0),
  "K": Transform(0.7, 0, 3),
}

row = 0
for consonant in consonants:
  row += 1
  col = 0
  for vowel in vowels:
    col += 1
    if show_syls:
      mp.append(f"draw syllable_{consonant}{vowel}(1, 0, {row*25}, {col*50});");
      mp.append(f"draw syllable_{consonant}n{vowel}(1, 0, {row*25}, {25+col*50});");
    con = consonants[consonant]
    vow = vowels[vowel]
    mp.append(f"""
      def syllable_{consonant}{vowel}(expr scale, yscale, x, y) =
        image(
          clear({con[0].path});
    """)    
    for path in con:
      mp.append(f"      draw {path.path} withpen {pens[path.pen]};")
    mp.append(f"""
          picture tmp;
          tmp = image(
    """); 
    for path in vow:
      mp.append(f"        draw {path.path} withpen {pens[path.pen]};")
    mp.append(f"""
          );
          clip tmp to buildcycle({con[0].path});
          draw tmp;
          draw grid;
        ) scaled scale yscaled yscale shifted (x, y)
      enddef;
    """)

    mp.append(f"""
      def syllable_{consonant}{vowel}n(expr scale, yscale, x, y) =
        image(
          clear(nasal_suffix);
          draw nasal_suffix withpen outer_pen;
          clear({con[0].path} yscaled 0.75 shifted (0, 2.5));
    """)    
    for path in con:
      mp.append(f"      draw {path.path} yscaled 0.75 shifted (0, 2.5) withpen {pens[path.pen]};")
    mp.append(f"""
          picture tmp;
          tmp = image(
    """); 
    transform = vowel_transform[consonant]
    for path in vow:
      mp.append(f"        draw {path.path} scaled {transform.scale} shifted ({transform.dx}, {transform.dy}) withpen {pens[path.pen]};")
    mp.append(f"""
          );
          clip tmp to buildcycle({con[0].path});
          draw tmp;
          draw grid;
        ) scaled scale yscaled yscale shifted (x, y)
      enddef;
    """)
          
print("\n".join(mp))
