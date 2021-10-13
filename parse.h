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
#include "render.h"
#include <cstring>

void parse(std::string text, float width, Render render) {
  text=regex_replace(text,regex("\\s"),"");
  class Block;
  class Block {
    public:
      bool ic;
      std::string t;
      std::string cc;
      bool cp;
      char d;
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
  Block* m=new Block(true, "block", text, nullptr, 1, 1, 0, 0);
  //parse
  Block* cpb=m;
  while (true) {
    if (cpb->ic) {
      if (cpb->cp) {
        if (cpb->pi==cpb->c.size()) {
          if (cpb->d=='-') {
            float h;
            for (Block* b : cpb->c) {
              if (b->h>h) {
                h=b->h;
              }
            }
            this.w=0;
            for (Block* b : cpb->c) {
              b->scale(h/b->h);
              this.w+=b->w;
            }
            this.h=h;
            float n=-this.w/2;
            for (Block* b : cpb->c) {
              n+=b->w/2;
              b->shift(n, 0);
              n+=b->w/2;
            }
          } else if (cpb->d=='|') {
            float w;
            for (Block* b : cpb->c) {
              if (b->w>w) {
                w=b->w;
              }
            }
            this.h=0;
            for (Block* b : cpb->c) {
              b->scale(w/b->w);
              this.h+=b->h;
            }
            this.w=w;
            float n=-this.h/2;
            for (Block* b : cpb->c) {
              n+=b->h/2;
              b->shift(0, n);
              n+=b->h/2;
            }
          }
          cpb=cpb->p;
          if (cpb==nullptr) {
            break;
          }
          cpb->pi++;
        } else {
          cpb=cpb->c[cpb->pi];
        }
      } else {
        char* c=cpb->cc.data();
        c--;
        bool woo;
        string t;
        int d;
        string coc;
        while (true) {
          c++;
          if (woo) {
            if (strchr("[(",*c)) {d++;}
            if (strchr("])",*c)) {d--;}
            if (d) {
              if (*c==0) {delete m;return;}
              coc+=*c;
              continue;
            }
            woo=false;
            cpb->c.push_back(new Block(true, t, coc, cpb, 1, 0, 0, 0));
            t="";
          } else {
            if (*c==0) {
              if (t.size()) {
                cpb->c.push_back(new Block(false, t, "", cpb, render.width(t), render.height(t), 0, 0));
              }
              break;
            }
            if (*c=='|') {
              if (cpb->d=='-') { delete m; return; }
              if (t.size()) {
                cpb->c.push_back(new Block(false, t, "", cpb, render.width(t), render.height(t), 0, 0));
              }
              cpb->d='|';
              t="";
              continue;
            }
            if (*c=='-') {
              if (cpb->d=='|') { delete m; return; }
              if (t.size()) {
                cpb->c.push_back(new Block(false, t, "", cpb, render.width(t), render.height(t), 0, 0));
              }
              cpb->d='-';
              t="";
              continue;
            }
            if (*c=='[') {
              d=1;
              woo=true;
              coc="";
              continue;
            }
            t+=*c;
          }
        }
        cpb->cp=true;
      }
    } else {
      cpb=cpb->p;
      cpb->pi++;
    }
  }
  m->scale(width/m->w);
  //draw
  Block* cdb=m;
  while (true) {
    if (cdb->di==cdb->c.size()) {
      if (cdb->ic) {
        render.container(cdb->t, cdb->x, cdb->y, cdb->w, cdb->h);
      } else {
        render.word(cdb->t, cdb->x, cdb->y, cdb->w, cdb->h);
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
  render.render()
  delete m;
}
