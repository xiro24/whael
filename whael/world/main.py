from pyglet.gl import *
from Entity import Entity
from CreateEntity import CreateEntity
from Clock import Time
from grid import Grid


class Main(pyglet.window.Window):
    def __init__(self,width,height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

#on_draw is not the initial draw it is in charge of drawing everything
    def on_draw(self):
        if t.run == True:
            self.clear()
            glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
            g.batch_draw(t.getTime())
            m.Display(self.width, self.height,ptarr,g.getMaps())
            g.update_grid(ptarr)

    def update(self,dt):
        t.print_time()

if __name__ == "__main__":
    width = 600
    height = 400
    window = Main(width,height,width, height, "whael", resizable= True)
    m = Entity(150,0,10)
    ce = CreateEntity()
    ptarr = ce.Particle(width,height,3)
    t = Time()
    g = Grid(width,height)
    g.setup_map()
    g.initial_draw()
    g.load_tiles()

    pyglet.clock.schedule_interval(window.update,1/60)
    pyglet.clock.set_fps_limit(60)

    pyglet.app.run()


#seems to get weird fps spikes