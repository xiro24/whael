#gid which will be the surface of the world ::25x25
from pyglet.gl import *
from array import array
import numpy


class Grid:

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def CreateGrid(self):
        # this will be used to control the space
        self.g = numpy.zeros(shape=(int(self.width/25),int(self.height/25)))

    def initial_draw(self):
        self.CreateGrid()
        glBegin(GL_LINES)
        glColor3f(0, 50, 80)
        i = 0
        j = 25
        #combined
        while i < 625:
            while j < 425:
                #top
                glVertex2i(i, j)
                glVertex2i(j, j)
                # bottom
                glVertex2i(i, 0)
                glVertex2i(i, j)
                if j < 400:
                    #right
                    glVertex2i(i, j)
                    glVertex2i(j, j)
                elif i < 600:
                    # left
                    glVertex2i(i, 25)
                    glVertex2i(i, j)
                #add one square space to the numpy grid
                numpy.insert(self.g, 1, [i, j])
                j += 25
            j = 25
            i += 25
        glEnd()

    #def update_grid(self,entity):
        #check if the value exists in the numpy array
        #if it does then redraw the square as stepped
        #you'll then need to register as the particle's
        #own private space

    def print_grid(self):
        print(self.g)