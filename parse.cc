#include "parse.h"
#include "render.h"

#include <iostream>
#include <string>

int main() {
  std::string input = "(((jan|utala)-(pona|ni))|li[lawa]|.[])-((mi-lawa)|e[(jan|utala)-(pona|ni)]|.[])";
  Render render;
  std::cout << input << std::endl;
  
  parse(input, 7, render);
}
