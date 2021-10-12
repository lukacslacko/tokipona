from dataclasses import dataclass

enum Pen:
  INNER = 0
  OUTER = 1

@dataclass
class Path:
  path: str
  pen: Pen

mp = []

clear = """
def clear(expr p) = 
  fill buildcycle(p) withcolor white; 
enddef;
"""
mp.append(clear)

nasal = """
path nasal_contour;
nasal_contour :=
  (0, -2) .. (-10, -7) {down} .. (-6, -10) {right} .. {up} (-3, -6) {down} ..
  {right} (0, -10) {right} .. {up} (3, -6) {down} .. {right} (6, -10) ..
  {up} (10, -7) .. cycle;

def nasal_suffix(expr s, ys, dx, dy) =
  image(
    clear(nasal_contour tr(s, ys, dx, dy));
    draw nasal_contour tr(s, ys, dx, dy) withpen po;
  )
enddef;
"""
mp.append(nasal)

vowels = {
  "a": [
    Path("(-10, 6) {right} .. (3, 0)", INNER),
    Path("(-3, 0) {dir 45} .. (3, 0)", INNER),
    Path("(-3, 0) {dir -45} .. (3, 0)", INNER),
    Path("fullcircle scaled 0.5", INNER),
  ],
}

mp.append("""
path consonant_j_contour, consonant_j_tick;
consonant_j_contour := (5, 4) {curl 0.2} .. (-4, 9) .. (-10, 0) .. (0, -10) .. (10, 0) .. (4, 10) .. (-2, 1);
consonant_j_contour := consonant_j_contour cutafter consonant_j_contour;
consonant_j_tick := (5,7) {dir 220} .. (2,6)
""")

consonants = {
  "": [
    Path("(0, -10) .. (-10, 0) .. (0, 10) .. (10, 0) .. cycle", OUTER),
  ],
  "j": [
    Path("consonant_j_contour", OUTER),
    Path("consonant_j_tick cutafter consonant_j_contour", INNER),
    Path("consonant_j_tick shifted(-1, 1) cutafter consonant_j_contour", INNER),
  ],
}
