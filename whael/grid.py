#gid which will be the surface of the world ::25x25
from pyglet.gl import *
from Utilities import Utilities
import numpy

class Grid:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.bool = True
        self.offset = 10
        self.EntitySize = 10
        self.u = Utilities()
        # this will be used to control the space
        #dtype enables objects t be stored

        self.g = numpy.zeros(shape=(int((self.width+self.offset)/self.offset),int((self.height+self.offset)/self.offset)), dtype=object)
        #handles tile placement
        self.gridw = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)
        #replace this one with gridw
        self.currentMap = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)
        #self.create_map()
        #this grid is in charge of entity placement
        self.gride = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)

    def initial_draw(self):
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
        self.load_map(self.currentMap)

    def update_grid(self,ptarr):

        for i, mpt in enumerate(ptarr):
            # probably replace with a macro instead
            # 1-entity 2-water 3-dirt 4-stone
            posy = int(mpt.x / self.offset)
            posx = int(mpt.y / self.offset)
            self.gride[posy][posx] = "3"
            self.Draw(0,90,0,posy,posx)

            # you would probably need to give this a specific width x height from the entity
            if self.EntitySize > self.offset:
                #additional sqaures

                if int(self.EntitySize % self.offset) != 0:
                    width = int(self.EntitySize % self.offset)
                    height = int(self.EntitySize % self.offset)

                    #out of bounds check required
                    for i in range(width):
                        for j in range(height):
                            self.Draw(0,90,0(posy+j),(posx+i))
    def create_map(self):
        file = open("mapv1","w")
        for j in range(int(self.height / self.offset)):
            for i in range(int(self.width/self.offset)):
                if i > 15 and i < 50 and j < 30 and j > 10:
                    file.write("1")
                else:
                    file.write("0")
            file.write("\n")
        file.close()

    def setup_map(self):
        with open("mapv1") as file:
            i = 0
            j = 0
            while True:
                c = file.read(1)
                if not c:
                    #end of file
                    return
                if c == "\n":
                    j+=1
                    i=0
                else:
                    self.currentMap[i][j] = c
                    i += 1

#####################
# OK THIS IS STUPID UR WASTING RESOURCES HERE
#you should try resizing them
    def load_tiles(self):
        img = self.u.load_image("assets/tex1.png")
        batch = pyglet.graphics.Batch()
        imgs = []
        i=0
        while i < self.width:
            j=0
            while j < self.height:
                #yo this is prone to duplication
                p = self.u.place_image(img, i, j , batch)
                if self.gridw[int((i/self.offset))][int((j/self.offset))] == "0":
                    self.u.color(p, 0, 90, 90)
                    imgs.append(p)
                elif self.gridw[int((i/self.offset))][int((j/self.offset))] == "1":
                    self.u.color(p, 0, 120, 50)
                    imgs.append(p)
                elif self.gridw[int((i / self.offset))][int((j / self.offset))] == "2":
                    self.u.color(p, 255, 242, 46)
                    imgs.append(p)
                j+=self.offset
            i+=self.offset
        batch.draw()

    def load_map(self,map):
        self.load_tiles()
        for i in range(int(self.width / self.offset)):
            for j in range(int(self.height / self.offset)):
                self.gridw[i][j] = map[i][j]
        for i in range(int(self.width / self.offset)):
            for j in range(int(self.height / self.offset)):
                if self.gridw[i][j] == "0":
                    self.Draw(0,80,90,i,j)
                elif self.gridw[i][j] == "1":
                    self.Draw(0,0.5,0,i,j)
                elif self.gridw[i][j] == "2":
                    self.Draw(1,1,0,i,j)

    def Draw(self,r,g,b,i,j):
        glBegin(GL_LINES)
        glColor3f(r, g, b)
        # top
        glVertex2i(self.g[i][j][1], self.g[i][j][2])
        glVertex2i(self.g[i][j][1], self.g[i][j][3])
        # left
        glVertex2i(self.g[i][j][0], self.g[i][j][2])
        glVertex2i(self.g[i][j][0], self.g[i][j][3])
        # bottom
        glVertex2i(self.g[i][j][0], self.g[i][j][2])
        glVertex2i(self.g[i][j][1], self.g[i][j][2])
        # right
        glVertex2i(self.g[i][j][0], self.g[i][j][3])
        glVertex2i(self.g[i][j][1], self.g[i][j][3])
        glEnd()

    def print_grid(self):
        print(self.g)