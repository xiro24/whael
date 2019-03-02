#gid which will be the surface of the world ::25x25
from pyglet.gl import *
from whael.whael.Utilities.Utilities import Utilities
from whael.whael.Elements.Generate import Generate
import numpy
#include air later
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
        self.gridO = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)
        #self.create_map()
        #this grid is in charge of entity placement
        self.gride = numpy.zeros(shape=(int(self.width / self.offset), int(self.height / self.offset)), dtype=object)

    def getMaps(self):
        maps = [self.gridw,self.gridO,self.gride,self.g]
        return maps

    def initial_draw(self):
        i = 0
        j = self.offset
        f = 0
        y = 0
        while f < 600:
            k = 0
            x = 0
            while k < 400:
                self.g[y][x] = (i+f, j+f, i+k, j+k)
                x+=1
                k += self.offset
            f += self.offset
            y+=1
        self.load_map(self.gridw)

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
                    self.gridw[i][j] = c
                    i += 1

#####################
# OK THIS IS STUPID UR WASTING RESOURCES HERE
                #try to separate it
    def load_tiles(self):
        img = self.u.load_image("assets/tex1.png")
        self.batch = pyglet.graphics.Batch()
        self.imgs = []
        i=0
        while i < self.width:
            j=0
            while j < self.height:
                #yo this is prone to duplication
                self.p = self.u.place_image(img, i, j , self.batch)
                if self.gridw[int((i/self.offset))][int((j/self.offset))] == "0": #sea
                    self.u.color(self.p, 0, 90, 170)
                    #have a random generator to determine concentration of resource (fish schools)
                    self.gridO[int((i/self.offset))][int((j/self.offset))] = Generate().ConjureAqua()
                    self.gridO[int((i / self.offset))][int((j / self.offset))].setLightIntensity(0,90,170)
                    self.imgs.append(self.p)
                elif self.gridw[int((i/self.offset))][int((j/self.offset))] == "1": #ground
                    self.u.color(self.p, 0, 120, 50)
                    # have a random generator to determine concentration of resource (crops/food)
                    # following certain conditions such as range from water add - sunlight later
                    self.gridO[int((i/self.offset))][int((j/self.offset))] = Generate().ConjureTerra()
                    self.gridO[int((i / self.offset))][int((j / self.offset))].setLightIntensity(0, 120, 50)
                    self.imgs.append(self.p)
                elif self.gridw[int((i / self.offset))][int((j / self.offset))] == "2": #sand
                    self.u.color(self.p, 255, 200, 46)
                    self.gridO[int((i/self.offset))][int((j/self.offset))] = Generate().ConjureTerra()
                    self.gridO[int((i / self.offset))][int((j / self.offset))].setLightIntensity(255, 200, 46)
                    self.imgs.append(self.p)
                j+=self.offset
            i+=self.offset










#perhaps try using a particle than just hovers over the map and it has a radius (only select the particles around it via the gridO system)


    #a time parameter is required
    def batch_draw(self,time):
        #draw the original grid then the sun
        self.batch.draw()
        sunBatch = pyglet.graphics.Batch()
        img = self.u.load_image("assets/tex1.png")
        #not that happy with the sun maybe fix later..
        x = 0
        #there might be a potential overlap here
        sunpos = 150
        colorAdjust = 0
        imgss =[]
        radius =100
        i=0
        stretch = 100
        j=0
        d=0
        while d < 200:
            x=0
            stretch-=d
            while x <= stretch:
                # controls the width of the sun it's position moving accross the board
                # use the grido
                # you must consider all angles
                # radius also means width
                for j in range(radius-d):
                    if int(int(j + time) / self.offset) >= 0 and int(int(j + time) / self.offset) < 60:
                        # top right side
                        grido = self.gridO[int(int(j + time) / self.offset)][int(int(sunpos + x) / self.offset)]
                        p = self.u.place_image(img, int(j + time), int(sunpos + x), sunBatch)
                        self.u.color(p, grido.getLightIntensity()[0] + int(d), grido.getLightIntensity()[1],
                                     grido.getLightIntensity()[2])
                        grido.setLightIntensity(grido.getLightIntensity()[0] + int(d),
                                                grido.getLightIntensity()[1], grido.getLightIntensity()[2])
                        # edit colour here
                        imgss.append(p)

                        grido = self.gridO[int(int(j + time) / self.offset)][int(int(sunpos - x) / self.offset)]
                        p = self.u.place_image(img, int(j + time), int(sunpos - x), sunBatch)
                        self.u.color(p, grido.getLightIntensity()[0] + int(d), grido.getLightIntensity()[1],
                                     grido.getLightIntensity()[2])
                        grido.setLightIntensity(grido.getLightIntensity()[0] + int(d),
                                                grido.getLightIntensity()[1], grido.getLightIntensity()[2])
                        # edit colour here
                        imgss.append(p)
                x += 10
            d+=20
        sunBatch.draw()

#just use images

#make a square instead!!!!!!!!!!!!!!!!!!

    def drawSun(self,lineX,lineY,time,sunpos,sunBatch,img):
        #for this you can just shorten it here
        x = lineX
        y = lineY
        colorAdjust = 0
        switchColor = False
        initialColor =10
        j= lineX
        while j < lineY:
            self.drawSunTile(int(j + time), sunpos-15, sunBatch, img, self.gridw, self.u, self.imgs, colorAdjust,switchColor,initialColor/255)
            if colorAdjust <= int(y / 2) - 30:
                initialColor += colorAdjust
                colorAdjust += 10
            elif switchColor == False:
                switchColor = True
                colorAdjust = 0
            if switchColor == True:
                initialColor -= colorAdjust
                colorAdjust += 10
            j += self.offset
        colorAdjust = 0
        initialColor=10
        switchColor = False
        i = y
        while i > int(lineX):
            self.drawSunTile(int(i + time - 10), sunpos-int(x*2)+15, sunBatch, img, self.gridw, self.u, self.imgs,colorAdjust,switchColor,initialColor/255)
            if colorAdjust <= int(y/2)-30:
                initialColor += colorAdjust
                colorAdjust += 10
            elif switchColor == False:
                switchColor = True
                colorAdjust = 0
            if switchColor == True:
                initialColor -= colorAdjust
                print(initialColor)
                colorAdjust += 10
            i -= self.offset

#the color keeps resetting
    def drawSunTile(self,sunoffsetX,sunpos,sunBatch,img,grid,util,images,colorAdjust,switchColor,initialColor):
        p = util.place_image(img,sunoffsetX,sunpos,sunBatch)
        if sunoffsetX > 0 and int((sunoffsetX / self.offset)) < 60:
            if grid[int((sunoffsetX / self.offset))][int((sunpos / self.offset))] == "0":  # sea
                if switchColor == False:
                    initialColor +=colorAdjust
                    util.color(p, initialColor, 20, 60)
                else:
                    #keeps giving me a zero
                    initialColor -= colorAdjust
                    util.color(p, initialColor, 20, 60)
                images.append(p)
            elif grid[int((sunoffsetX / self.offset))][int((sunpos / self.offset))] == "1":  # ground
                if switchColor == False:
                    initialColor += colorAdjust
                    util.color(p, initialColor, 112, 147)
                else:
                    initialColor -= colorAdjust
                    util.color(p, initialColor, 112, 147)
                images.append(p)
            elif grid[int((sunoffsetX / self.offset))][int((sunpos / self.offset))] == "2":  # sand
                if switchColor == False:
                    initialColor += colorAdjust
                    util.color(p, initialColor, 69, 0)
                else:
                    initialColor -= colorAdjust
                    util.color(p, initialColor, 69, 0)
                images.append(p)

    def load_map(self,map):
        for i in range(int(self.width / self.offset)):
            for j in range(int(self.height / self.offset)):
                self.gridw[i][j] = map[i][j]

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