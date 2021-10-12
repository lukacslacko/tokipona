class Render:
  def __init__(self):
    pass
  
  def valid_word(self, word: str) -> bool:
    return True
  
  def valid_container(self, word: str) -> bool:
    return True
  
  def width(self, word: str) -> float:
    return 1.0
  
  def height(self, word: str) -> float:
    return 1.0
  
  def word(self, word: str, x: float, y: float, size: float) -> None:
    pass
  
  def container(self, word: str, x: float, y: float, w: float, h: float) -> None:
    pass
  
  def render(self):
    pass
