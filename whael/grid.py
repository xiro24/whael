#gid which will be the surface of the world ::25x25
from pyglet.gl import *
import numpy


class Grid:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.bool = True

    def CreateGrid(self):
        # this will be used to control the space
        #dtype enables objects t be stored

        self.g = numpy.zeros(shape=(int((self.width+25)/25),int((self.height+25)/25)), dtype=object)
        #handles objects on the grid
        self.gridw = numpy.zeros(shape=(int(self.width / 25), int(self.height / 25)), dtype=object)
    def initial_draw(self):
        self.CreateGrid()
        glBegin(GL_LINES)
        glColor3f(0, 50, 80)
        i = 0
        j = 25
        y = 0
        #combined
        while i < 625:
            x=0
            while j < 425:
                #top
                glVertex2i(i, j)
                glVertex2i(j, j)
                #left
                glVertex2i(i, 0)
                glVertex2i(i, j)
                if j < 400:
                    #bottom
                    glVertex2i(i, j)
                    glVertex2i(j, j)
                elif i < 600:
                    # right
                    glVertex2i(i, 25)
                    glVertex2i(i, j)
                self.g[y][x] = (i,j)
                #add one square space to the numpy grid
                #ignore the last column
                x+=1
                j += 25
            j = 25
            i += 25
            y+=1
        glEnd()
        #if self.bool == True:
        #    print("hey")
        #    print(self.g)
        #    self.bool = False
        #    print(self.g[5][5])
        #    print(self.g[5][5][1])

    def update_grid(self,ptarr):
        for i, mpt in enumerate(ptarr):
            # probably replace with a macro instead
            # 1-entity 2-water 3-dirt 4-stone
            posy = int(mpt.x / 25)
            posx = int(mpt.y / 25)
            self.gridw[posy][posx] = 1
            glBegin(GL_LINES)
            glColor3f(0, 90, 0)
            # top
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][1])
            # left
            glVertex2i(self.g[posy][posx][0], 0)
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            # bottom
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            glVertex2i(self.g[posy][posx][1], self.g[posy][posx][1])
            # right
            glVertex2i(self.g[posy][posx][0], 25)
            glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            #print(posy)
            #print(posx)
#####################################################################
            # top
            #glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            #glVertex2i(self.g[posy][posx][1], self.g[posy][posx][1])
            # left
            #glVertex2i(self.g[posy][posx][0], 0)
            #glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            # bottom
            #glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])
            #glVertex2i(self.g[posy][posx][1], self.g[posy][posx][1])
            # right
            #glVertex2i(self.g[posy][posx][0], 25)
            #glVertex2i(self.g[posy][posx][0], self.g[posy][posx][1])

            #needs to be percise
            #3x3
######################################
            #right
            glVertex2i(75, 50)
            glVertex2i(75, 75)
                    #i=width #height+LENGTH OF WIRE
            # left
            glVertex2i(50, 50)
            glVertex2i(50, 75)
                # i=width #height+LENGTH OF WIRE
            # bottom
            glVertex2i(75, 50)
            glVertex2i(50, 50)
                # i=height+LENGTH OF WIRE #j=width
            # top
            glVertex2i(75, 75)
            glVertex2i(50, 75)
                    #i=height+LENGTH OF WIRE #j=width

######################################
            # 3x4
            # right
            glVertex2i(125, 50)
            glVertex2i(125, 75)
            # i=width/row #height+LENGTH OF WIRE
            # left
            glVertex2i(100, 50)
            glVertex2i(100, 75)
            # i=width/row #height+LENGTH OF WIRE
            # bottom
            glVertex2i(100, 50)
            glVertex2i(125, 50)
            # i=height+LENGTH OF WIRE #j=width
            # top
            glVertex2i(100, 75)
            glVertex2i(125, 75)
            # i=height+LENGTH OF WIRE #j=width
            #i=translation to the right

            glEnd()
    def print_grid(self):
        print(self.g)