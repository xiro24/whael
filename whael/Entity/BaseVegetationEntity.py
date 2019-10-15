from pyglet.gl import *
import math
from whael.world.grid import Grid
from whael.Elements.Elementario.Terra import Terra
from whael.Elements.Elementario.Aqua import Aqua
import random

class BaseVegetationEntity:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.size = size

    #shold be drawing sprites
    def DrawCircle(self,numPoints):
        verts = []
        for i in range(numPoints):
            angle = math.radians(float(i) / numPoints * 360.0)
            x = self.size * math.cos(angle) + self.x
            y = self.size * math.sin(angle) + self.y
            verts += [x, y]
        self.circle = pyglet.graphics.vertex_list(numPoints, ('v2f', verts))
        self.draw()

    def draw(self):
        glColor3f(0, 255, 0)
        self.circle.draw(GL_LINE_LOOP)

    def Display(self,width,height,ptarr,map):
        for i, mpt in enumerate(ptarr):
            mpt.DrawCircle(20)

    def set_map(self,map):
        self.map = map[0]