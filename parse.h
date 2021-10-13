/*
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
*/
#include <string>
#include <vector>
#include <regex>

std::string parse(std::string text, float width) {
  std::string out;
  text=regex_replace(text,regex("\\s"),"");
  class Block;
  class Block {
    public:
      bool ic;
      std::string t;
      std::string cc;
      int pi;
      int di;
      Block* p;
      std::vector<Block*> c;
      float w;
      float h;
      float x;
      float y;
    Block(bool ic, std::string t, std::string cc, Block* p, float w, float h, float x, float y) {
      this.ic=ic;
      this.t=t;
      this.cc=cc;
      this.p=p;
      this.w=w;
      this.h=h;
      this.x=x;
      this.y=y;
    }
    ~Block() {
      for (Block* b : this.c) {
        delete b;
      }
    }
    void scale(float s) {
      this.w*=s;
      this.h*=s;
      for (Block* b : this.c) {
        b->scale(s);
        b->shift(this.x+(b->x-this.x)*s-b->x,this.y+(b->y-this.y)*s-b->y);
      }
    }
    void shift(float x, float y) {
      this.x+=x;
      this.y+=y;
      for (Block* b : this.c) {
        b->shift(x, y);
      }
    }
  };
  Block* m=new Block(true, "block", text, nullptr, 1, 0, 0, 0);
  //parse
  m->scale(width/m->w);
  //draw
  Block* cdb=m;
  while true {
    if (cdb->di==cdb->c.size()) {
      if (cdb->ic) {
        out+="render.container('"+cdb->t+"', "+std::to_string(cdb->x)+", "+std::to_string(cdb->y)+", "+std::to_string(cdb->w)+", "+std::to_string(cdb->h)+")\n";
      } else {
        out+="render.word('"+cdb->t+"', "+std::to_string(cdb->x)+", "+std::to_string(cdb->y)+", "+std::to_string(cdb->w)+", "+std::to_string(cdb->h)+")\n";
      }
      cdb=cdb->p;
      if (cdb==nullptr) {
        break;
      }
      cdb->di++;
      continue;
    }
    cdb=cdb->c[cdb->di];
  }
  out+="render.render()\n";
  delete m;
  return out;
}
