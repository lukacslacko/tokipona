#include "parse.h"
#include "render.h"

#include <string>

int main() {
  std::string input = "(((jan|utala)-(pona|ni))|li[lawa]|.[])-((mi-lawa)|e[(jan|utala)-(pona|ni)]|.[])";
  Render render;
  
  parse(input, 7, render);
}
