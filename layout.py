from render import Render

class Block:
  def __init__(self, word: str, width: float, height: float, x: float, y: float, blocks: list[Block]):
    self._word = word
    self._width = width
    self._height = height
    self._x = x
    self._y = y
    self._blocks = blocks
    
  def scale(self, scale: float) -> None:
    self._width *= scale
    self._height *= scale
    self._x *= scale
    self._y *= scale
    for block in self._blocks:
      block.scale(scale)
      
  def shift(self, dx: float, dy: float) -> None:
    self._x += dx
    self._y += dy
    for block in self._blocks:
      block.shift(dx, dy)
      
  def width(self) -> float:
    return self._width
  
  def height(self) -> float:
    return self._height
  
  def x(self) -> float:
    return self._x
  
  def y(self) -> float:
    return self._y
  
  def debug(self) -> None:
    print(f"{self._word}: x={self._x}, y={self._y}, width={self._width}, height={self._height}")
    for block in self._blocks:
      block.debug()
  
def layout(s: str, render: Render) -> Block:
  s.replace(" ", "")
  pieces, dir = self._split(s)
  if len(pieces) == 1:
    word = pieces[0]
    if "[" in word:
      i = word.index("[")
      block = layout(word[i+1:-1], render)
      return Block(word, block.width(), block.height(), block.x(), block.y(), [block])
    else:
      w = render.width(word)
      h = render.height(word)
      return Block(word, w, h, w/2, h/2, [])
  blocks = [layout(piece, render) for piece in pieces]
  if dir == "-":
    for block in blocks:
      block.scale(1 / block.height())
    w = 0
    for block in blocks:
      block.shift(w + block.width() / 2 - block.x(), block.height() / 2 - block.y())
      w += block.width()
    return Block(word, w, 1, w/2, 0.5, [blocks])
  else:
    for block in blocks:
      block.scale(1 / block.width())
    h = 0
    for block in blocks:
      block.shift(block.width() / 2 - block.x(), h + block.height() / 2 - block.y())
      h += block.height()
    return Block(word, 1, h, 0.5, h/2, [blocks])
    
def _split(s: str) -> tuple[list[str], char]:
  depth = 0
  brack = 0
  res = []
  sep = ""
  part = ""
  for c in s:
    if c == "(":
      depth += 1
      part += c
    elif c == ")":
      depth -= 1
      part += c
    elif c == "[":
      brack += 1
      part += c
    elif c == "]":
      brack -= 1
      part += c
    elif c in "-|" and depth == 0 and brack == 0:
      if sep != "" and sep != c:
        throw Error(f"- | in {s}")
      sep = c
      res.append(part)
      part = ""
    else:
      part += c
  if depth == 0 and brack == 0:
    res.append(part)
  else:
    throw Error(f"depth {depth}, brack {brack}")
  return res, sep

render = Render()
layout("(a - b) | c", render).debug()
layout("(x | y) - z", render).debug()
