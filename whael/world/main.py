from pyglet.gl import *
from whael.Entity.BaseEntity import BaseEntity
from whael.Utilities.CreateEntity import CreateEntity
from whael.Utilities.Clock import Time
from whael.world.grid import Grid
from whael.Particles.Sun import Sun
from whael.world.controller import controller


class Main(pyglet.window.Window):
    def __init__(self,width,height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height

#on_draw is not the initial draw it is in charge of drawing everything
    def on_draw(self):
        if t.run == True:
            self.clear()
            g.batch_draw(t.getTime())
            m.Display(self.width, self.height, ptarr, g.getWorldMaps())
            g.update_grid(ptarr)
            #opengl
            control.circadianRhythm(t.getTime(),width,height)
                #reload the background after translation of opengl

    def update(self,dt):
        t.print_time()

if __name__ == "__main__":
    width = 600
    height = 400
    window = Main(width,height,width, height, "whael", resizable= True)
    m = BaseEntity(150, 0, 10)
    ce = CreateEntity()
    ptarr = ce.Particle(width,height,3)
    t = Time()
    g = Grid(width,height)
    g.setup_map()
    g.initial_draw()
    g.load_tiles()

    #pyglet.clock.schedule_interval(window.update,1/60)
    #create controller for weather
    control = controller()
    control.initializer()

    glEnable(GL_BLEND)
    glEnable(GL_POINT_SMOOTH)
    glEnable(GL_LIGHTING)
    glColorMaterial(GL_FRONT_AND_BACK, GL_EMISSION)
    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glDisable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pyglet.clock.schedule_interval(window.update,0.1)
    pyglet.clock.set_fps_limit(60)


    pyglet.app.run()


#seems to get weird fps spikes