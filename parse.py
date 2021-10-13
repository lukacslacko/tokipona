# ((toki | pona) - li[toki | pona]) | .[]
# (toki - pona) | li[toki - pona] | .[]
# (mi - nimi) | (jan - cart[La Si]) | .[]
# (mi - nimi - jan) | cart[La Si] | .[]
# (Ka - La - (Ma | Pa)) | (lili) | (((Ke - Le) | Me) - (Ki | (Li - Mi)))
# (nasin mani) | li[ike] | .[]
#
# class Render:
#  def valid_word(self, word: str) -> bool:
#  def valid_container(self, word: str) -> bool:
#  def width(self, word: str) -> float:
#  def height(self, word: str) -> float:
#  def word(self, word: str, x: float, y: float, w: float, h: float) -> None:
#  def container(self, word: str, x: float, y: float, w: float, h: float) -> None:
#  def render(self):

import render
from dataclasses import dataclass
from copy import deepcopy

def parse(text: str, render: Render):
  @dataclass
  class Block:
    c: list[type["Block"]]
    ic: bool
    t: str
    ct: str
    ctp: bool
    w: float
    h: float
    d: bool
    i: int
  @dataclass
  class Pa:
    c: type["Pa"]
    i: int
  pa=Pa(None,0)
  text = ''.join(text.split())
  m=dc([], True, '', text, False, 0, 0, False, 0)
  while not m.d:
    i=m
    p=Pa
    while len(i.c):
      if not i.d:
        i=i.c[i.d]
        
      else:
        
  #draw
  render.render()
