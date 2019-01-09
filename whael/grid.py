#gid which will be the surface of the world ::25x25
from pyglet.gl import *
import numpy


class Grid:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.bool = True
        self.offset = 10
        self.EntitySize = 10

    def CreateGrid(self):
        # this will be used to control the space
        #dtype enables objects t be stored

        self.g = numpy.zeros(shape=(int((self.width+self.offset)/self.offset),int((self.height+self.offset)/self.offset)), dtype=object)
        #handles objects on the grid
        self.gridw = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)
    def initial_draw(self):
        self.CreateGrid()
        i = 0
        j = self.offset
        f = 0
        y = 0
        glBegin(GL_LINES)
        glColor3f(0, 90, 80)
        while f < 600:
            k = 0
            x = 0
            while k < 400:
                # 1x1
                # right
                glVertex2i(j + f, i + k)  # x
                glVertex2i(j + f, j + k)  # y
                # i=width/row #height+LENGTH OF WIRE
                # left
                glVertex2i(i + f, i + k)  # x
                glVertex2i(i + f, j + k)  # y
                # i=width/row #height+LENGTH OF WIRE
                # bottom
                glVertex2i(i + f, i + k)  # x
                glVertex2i(j + f, i + k)  # y
                # i=height+LENGTH OF WIRE #j=width
                # top
                glVertex2i(i + f, j + k)  # x
                glVertex2i(j + f, j + k)  # y

                self.g[y][x] = (i+f, j+f, i+k, j+k)
                x+=1
                k += self.offset
            f += self.offset
            y+=1
        glEnd()

    def update_grid(self,ptarr):
        for i, mpt in enumerate(ptarr):
            # probably replace with a macro instead
            # 1-entity 2-water 3-dirt 4-stone
            posy = int(mpt.x / self.offset)
            posx = int(mpt.y / self.offset)
            self.gridw[posy][posx] = 1
            glBegin(GL_LINES)
            glColor3f(0, 90, 0)
            # top
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][2])
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][3])
            # left
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][2])
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][3])
            # bottom
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][2])
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][2])
            # right
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][3])
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][3])


            # you would probably need to give this a specific widthx height from the entity
            if self.EntitySize > self.offset:
                #additional sqaures

                if int(self.EntitySize % self.offset) != 0:
                    width = int(self.EntitySize % self.offset)
                    height = int(self.EntitySize % self.offset)

                    #out of bounds check required
                    for i in range(width):
                        for j in range(height):
                            glVertex2i(self.g[posy+j][posx+i][1], self.g[posy+j][posx+i][2])
                            glVertex2i(self.g[posy+j][posx+i][1], self.g[posy+j][posx+i][3])
                            # left
                            glVertex2i(self.g[posy+j][posx+i][0], self.g[posy+j][posx+i][2])
                            glVertex2i(self.g[posy+j][posx+i][0], self.g[posy+j][posx+i][3])
                            # bottom
                            glVertex2i(self.g[posy+j][posx+i][0], self.g[posy+j][posx+i][2])
                            glVertex2i(self.g[posy+j][posx+i][1], self.g[posy+j][posx+i][2])
                            # right
                            glVertex2i(self.g[posy+j][posx+i][0], self.g[posy+j][posx+i][3])
                            glVertex2i(self.g[posy+j][posx+i][1], self.g[posy+j][posx+i][3])

            glEnd()



    def print_grid(self):
        print(self.g)