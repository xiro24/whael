from pyglet.gl import *
from Entity import Entity

class main(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        window.clear()
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        m.Display(600, 400)

    def update(self,dt):
        m.Display(600, 400)
        print(pyglet.clock.get_fps())

if __name__ == "__main__":
    window = main(600,400, "whael",resizable= False)
    m = Entity(150,0,15)
    m.Particle(600,400)
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.app.run()


