from render import Render;

render = Render();

render.word("mi", 0, 0, 1/3, 1/3)
render.word("moku", 1/3, 0, 1/3, 1/3)
render.word("telo", 2/3, 0, 1/3, 1/3)
render.render()
