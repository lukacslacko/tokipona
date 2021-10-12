from dataclasses import dataclass

@dataclass
class Glyph:
  name: str
  x: float
  y: float
  size: float
  yscale: float

@dataclass
class Container:
  name: str
  x: float
  y: float
  w: float
  h: float

class Render:
  def __init__(self):
    self._glyphs = []
  
  def valid_word(self, word: str) -> bool:
    return True
  
  def valid_container(self, word: str) -> bool:
    return True
  
  def width(self, word: str) -> float:
    return 1.0
  
  def height(self, word: str) -> float:
    return 1.0
  
  def word(self, word: str, x: float, y: float, w: float, h: float) -> None:
    self._glyphs.append(Glyph(word, x, y, w / self.width(word), h/w / (self.height(word)/self.width(word))))
  
  def container(self, word: str, x: float, y: float, w: float, h: float) -> None:
    self._glyphs.append(Container(word, x, y, w, h))
  
  def render(self):
    for glyph in reversed(self._glyphs):
      if isinstance(glyph, Glyph):
        print(f"draw logo_{glyph.name}({glyph.size}, {glyph.yscale}, {glyph.x}, {glyph.y});")
      if isinstance(glyph, Container):
        print(f"draw container_{glyph.name}({glyph.x}, {glyph.y}, {glyph.w}, {glyph.h});")
