from pyglet.gl import *
from Entity import Entity
from Clock import Time


class Main(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_draw(self):
        window.clear()
        glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
        m.Display(600, 400)

    def update(self,dt):
        m.Display(600, 400)
        t.print_time()


if __name__ == "__main__":
    window = Main(600, 400, "whael", resizable= False)
    m = Entity(150,0,15)
    m.Particle(600,400)
    t = Time()
    pyglet.clock.schedule_interval(window.update,1/60.0)
    pyglet.clock.set_fps_limit(60)

    pyglet.app.run()


