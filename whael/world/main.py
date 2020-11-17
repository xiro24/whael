from pyglet.gl import *
from Entity.Entities.IntelligentEntity.Vir import Vir
from whael.Utilities.Clock import Time
from whael.world.grid import Grid
from whael.world.controller import controller
from Entity.Entities.VegetationEntity.berry import berry
from whael.world.acclimatize import acclimatize

class Main(pyglet.window.Window):
    def __init__(self,width,height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = width
        self.height = height
        self.temp_intitial = True


#on_draw is not the initial draw it is in charge of drawing everything
    def on_draw(self):
        if t.run == True:
            self.clear()
            g.batch_draw(t.getTime())
            if self.temp_intitial:
                self.intelligent_entities = ptarr
                self.vegetation_entities = pvege
                self.temp_intitial = False
            ce.Display(self.width, self.height, self.intelligent_entities, g.getWorldMaps())
            #g.trackAllEntities(ptarr)

            #if t.getTime()%100 == 0:
            cv.Display(self.width, self.height, self.vegetation_entities, g.getWorldMaps())
            #g.trackAllEntities(pvege)
            #opengl
            control.circadianRhythm(t.getTime(),width,height)
                #reload the background after translation of opengl

    def update(self,dt):
        t.tick()
        t.print_time()
        wither.processTime(t,"list_biodegradables")
        print("before",len(self.intelligent_entities))
        self.intelligent_entities = wither.Floor_Item(self.intelligent_entities, g.getWorldMaps())
        print("after",len(self.intelligent_entities))
        self.vegetation_entities = wither.Floor_Item(self.vegetation_entities, g.getWorldMaps())


if __name__ == "__main__":
    width = 600
    height = 400

    #define Objects here:
    window = Main(width,height,width, height, "whael", resizable= True)
    t = Time()
    wither = acclimatize()
    g = Grid(width,height)
    g.setup_map()
    g.initial_draw()
    g.load_tiles()

    #pyglet.clock.schedule_interval(window.update,1/60)

    #entity creation
    list_biodegradables = []
    #m = BaseEntity(150, 0, 10)
    #v = BaseVegetationEntity(100, 0, 10)
    ce = Vir(width, height, 10, list_biodegradables)
    cv = berry(width, height, 5, list_biodegradables)
    ptarr = ce.createEntity(3, width, height, g.getWorldMaps(), g.getMapsDimensions())
    pvege = cv.createEntity(3, width, height, g.getWorldMaps(), g.getMapsDimensions())

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