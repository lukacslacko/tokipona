from render import Render

class Block:
  def __init__(self, word: str, width: float, height: float, x: float, y: float, blocks: list[type["Block"]]):
    self._word = word
    self._width = width
    self._height = height
    self._x = x
    self._y = y
    self._blocks = blocks
    
  def set_word(self, word: str) -> None:
    self._word = word;
    
  def render(self, render: Render) -> None:
    if len(self._blocks) == 0:
      render.word(self._word, self._x, self._y, self._width, self._height)
    else:
      for block in self._blocks:
        block.render(render)
      if self._word != "":
        render.container(self._word, self._x, self._y, self._width, self._height)
    
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
  
  def __str__(self) -> str:
    result = f"{self._word}: x={self._x}, y={self._y}, width={self._width}, height={self._height}"
    for block in self._blocks:
      result += "\n" + str(block)
    return result
  
def layout(s: str, render: Render) -> Block:
  s = s.replace(" ", "")
  s = s.replace("\n", "")
  pieces, dir = _split(s)
  if len(pieces) == 1:
    word = pieces[0]
    if word == "":
      return None  # empty container's content, like after the period in "(mi-toki)|.[]".
    if word[0] == "(":
      block = layout(word[1:-1], render)
      return Block("", block.width(), block.height(), block.x(), block.y(), [block])
    elif "[" in word:
      i = word.index("[")
      block = layout(word[i+1:-1], render)
      cmd = word[:i]
      if block is None:
        return Block(word[:i], 1, 0, 0.5, 0, [])
      else:
        new_block = Block(word[:i], block.width(), block.height(), block.x(), block.y(), [block])
        if cmd[0] == "=":
          new_block.set_word("")
          new_block.scale(float(cmd[1:]) / block.width())
        return new_block
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
    return Block("", w, 1, w/2, 0.5, blocks)
  else:
    for block in blocks:
      block.scale(1 / block.width())
    h = 0
    for block in blocks:
      block.shift(block.width() / 2 - block.x(), h + block.height() / 2 - block.y())
      h += block.height()
    return Block("", 1, h, 0.5, h/2, blocks)
    
def _split(s: str) -> tuple[list[str], str]:
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
        raise Error(f"- | in {s}")
      sep = c
      res.append(part)
      part = ""
    else:
      part += c
  if depth == 0 and brack == 0:
    res.append(part)
  else:
    raise Error(f"depth {depth}, brack {brack}")
  return res, sep

import sys

if __name__ == "__main__":
  f = open(sys.argv[1], "r")
  render = Render()
  layout(f.read(), render).render(render)
  render.render()
