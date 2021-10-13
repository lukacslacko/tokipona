#include "render.h"

#include <iostream>
#include <string>

Render::Render() {}

float Render::width(const std::string& word) const { return 1.0; }
float Render::height(const std::string& word) const { 
  if (word == ".") {
    return 0.0;
  }
  return 1.0;
}

void Render::word(const std::string& word, float x, float y, float width, float height) {
  std::cout << "word " << word << " x=" << x << " y=" << y << " width=" << width << " height=" << height << std::endl;
}

void Render::container(const std::string& word, float x, float y, float width, float height) {
  std::cout << "container " << word << " x=" << x << " y=" << y << " width=" << width << " height=" << height << std::endl;
}

void Render::render() {
  std::cout << "render." << std::endl;
}
