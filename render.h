#ifndef RENDER_H
#define RENDER_H

#include <string>

class Render {
  public:
  Render();
  
  float width(const std::string& word) const;
  float height(const std::string& word) const;
  
  void word(const std::string& word, float x, float y, float width, float height);
  void container(const std::string& word, float x, float y, float width, float height);
  void render();
};

#endif // RENDER_H
