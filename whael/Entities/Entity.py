from pyglet.gl import *
import math
from whael.world.grid import Grid
from whael.Elements.Elementario.Terra import Terra
from whael.Elements.Elementario.Aqua import Aqua
import random





class Entity:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.size = size
        self.speed = 0.01
        self.angle = 0
        self.elasticity = 0.75

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
        glColor3f(255, 255, 255)
        self.circle.draw(GL_LINE_LOOP)

    def Move(self,map):
        #gravity = (math.pi, 0.002)
        posy = int(self.x / 10)
        posx = int(self.y / 10)

        #may need to check which angle it's facing and then use that as the sight
        if isinstance(map[1][posy][posx],Terra):
            self.x += math.sin(self.angle) * self.speed+0.03
            self.y -= math.cos(self.angle) * self.speed+0.03
        else:
            # check boundaries
            # may want to chanage the if statement so entity will walk slower in sand
            #or extremely slow in water / perhaps ahve a checker to check if has a swim trait etc.
            self.angle = random.uniform(0, math.pi * 2)
            self.x += math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed

    #just focus on the AI movement later
    def Display(self,width,height,ptarr,map):
        for i, mpt in enumerate(ptarr):
            mpt.Move(map)
            #mpt.bounce(map)
            for mpt2 in ptarr[i+1:]:
                self.collide(mpt,mpt2)
            mpt.DrawCircle(20)

    def set_map(self,map):
        self.map = map[0]

    def collide(self,p1,p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y

        distance = math.hypot(dx,dy)
        if distance < p1.size + p2.size:
            tangent = math.atan2(dy,dx)
            p1.angle = 2 * tangent - p1.angle
            p2.angle = 2 * tangent - p2.angle

            angle = 0.5 * math.pi + tangent
            p1.x += math.sin(angle)
            p1.y -= math.cos(angle)
            p2.x -= math.sin(angle)
            p2.y += math.cos(angle)

    def bounce(self,map):
        posy = int(self.x / 10)
        posx = int(self.y / 10)
        if posy > 60:
            posy = 59
        elif posx > 40:
            posx = 39
        aa=0
        while map[posy][posx] == "0":
            self.angle = random.uniform(0,math.pi*2)
            self.x += math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed
            if self.y > 0:
                temp = self.y
            else:
                self.y = temp
            if self.x > 0:
                tempx = self.x
            else:
                self.x = tempx
            posy = int(self.x / 10)
            posx = int(self.y / 10)
            print("x2:", posy)
            print("y2:", posx)
            if posy > 59:
                posy=59
            if posx > 39:
                posx = 39
            print("xv:", posy)
            print("yv:", posx)
            print("temp:",aa)




                #don't really need boucne anymore
    def bouncey(self,width,height,map):
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = - self.angle
        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle =- self.angle

        if self.y > height - self.size:
            self.y =2*(height-self.size) - self.y
            self.angle = math.pi - self.angle
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle