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
  "e": [
    Path("(-4, 0) -- (4, 0)", INNER),
    Path("(0, -4) -- (0, 4)", INNER),
  ],
}

mp.append("""
path consonant_j_contour, consonant_j_tick;
consonant_j_contour := (5, 4) {curl 0.2} .. (-4, 9) .. (-10, 0) .. (0, -10) .. (10, 0) .. (4, 10) .. (-2, 1);
consonant_j_contour := consonant_j_contour cutafter consonant_j_contour;
consonant_j_tick := (5,7) {dir 220} .. (2,6)

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
  "j": [
    Path("consonant_j_contour", OUTER),
    Path("consonant_j_tick cutafter consonant_j_contour", INNER),
    Path("consonant_j_tick shifted(-1, 1) cutafter consonant_j_contour", INNER),
  ],
  "k": [
    Path("consonant_k_contour", OUTER),
    Path("consonant_k_a", INNER),
    Path("consonant_k_b", INNER),
  ],
}

for consonant in consonants:
  for vowel in vowels:
    mp.append(f"""
      def syllable_{consonant}{vowel}(expr 
    """)